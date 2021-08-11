import pandas as pd
import numpy as np
import math as math
import numpy as np
from numpy import *
from scipy.stats import bartlett
def main():
    df=pd.read_csv("Data\\BigData.csv")
    df = df[list(['a{}'.format(i) for i in range(1,9)])]
    df2=df.copy()

    # 皮尔森相关系数
    df2_corr=df2.corr()
    print("\n相关系数:\n",df2_corr)

    # KMO测度
    def kmo(dataset_corr):
        corr_inv = np.linalg.inv(dataset_corr)
        nrow_inv_corr, ncol_inv_corr = dataset_corr.shape
        A = np.ones((nrow_inv_corr, ncol_inv_corr))
        for i in range(0, nrow_inv_corr, 1):
            for j in range(i, ncol_inv_corr, 1):
                A[i, j] = -(corr_inv[i, j]) / (math.sqrt(corr_inv[i, i] * corr_inv[j, j]))
                A[j, i] = A[i, j]
        dataset_corr = np.asarray(dataset_corr)
        kmo_num = np.sum(np.square(dataset_corr)) - np.sum(np.square(np.diagonal(A)))
        kmo_denom = kmo_num + np.sum(np.square(A)) - np.sum(np.square(np.diagonal(A)))
        kmo_value = kmo_num / kmo_denom
        return kmo_value

    print("\nKMO测度:", kmo(df2_corr))

    # 巴特利特球形检验
    df2_corr1 = df2_corr.values
    print("\n巴特利特球形检验:", bartlett(df2['a1'], df2['a2'], df2['a3'], df2['a4'], df2['a5'], df2['a6'], df2['a7'], df2['a8']))

    # 偏度系数与峰度系数
    for i in list(df2):
        print(i, df2[i].skew(), df[i].kurt())

if __name__ == '__main__':
    main()