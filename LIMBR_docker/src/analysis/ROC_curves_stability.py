import pandas as pd
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import sys
import getopt
import optparse

def main(argv):
    for sub in range(9):
        parser = optparse.OptionParser()
        parser.add_option('-l','--list', dest='inputfiles', nargs=6 )
        (options, args) = parser.parse_args()
        l = pd.read_csv(options.inputfiles[3],sep='\t',header=None)[sub*10000:(sub+1)*10000]
        y = l[1].values.astype(int)
        scores = np.asarray([1-i for i in l[0].values.astype(float)])
        fpr, tpr, thresholds = metrics.roc_curve(y, scores)
        roc_auc = metrics.auc(fpr, tpr)
        yl = float(len(l[(l[0]<.05) & (l[1]==1)]))/(len(l[(l[0]<.05) & (l[1]==1)])+len(l[(l[0]>.05) & (l[1]==1)]))
        xl = float(len(l[(l[0]<.05) & (l[1]==0)]))/(len(l[(l[0]<.05) & (l[1]==0)])+len(l[(l[0]>.05) & (l[1]==0)]))

        b = pd.read_csv(options.inputfiles[2],sep='\t',header=None)[sub*10000:(sub+1)*10000]
        scoresb = np.asarray([1-i for i in b[0].values.astype(float)])
        yb = b[1].values.astype(int)
        fprb, tprb, thresholdsb = metrics.roc_curve(yb, scoresb)
        roc_aucb = metrics.auc(fprb, tprb)
        yb = float(len(b[(b[0]<.05) & (b[1]==1)]))/(len(b[(b[0]<.05) & (b[1]==1)])+len(b[(b[0]>.05) & (b[1]==1)]))
        xb = float(len(b[(b[0]<.05) & (b[1]==0)]))/(len(b[(b[0]<.05) & (b[1]==0)])+len(b[(b[0]>.05) & (b[1]==0)]))

        bl = pd.read_csv(options.inputfiles[1],sep='\t',header=None)[sub*10000:(sub+1)*10000]
        scoresbl = np.asarray([1-i for i in bl[0].values.astype(float)])
        ybl = bl[1].values.astype(int)
        fprbl, tprbl, thresholdsbl = metrics.roc_curve(ybl, scoresbl)
        roc_aucbl = metrics.auc(fprbl, tprbl)
        ybl = float(len(bl[(bl[0]<.05) & (bl[1]==1)]))/(len(bl[(bl[0]<.05) & (bl[1]==1)])+len(bl[(bl[0]>.05) & (bl[1]==1)]))
        xbl = float(len(bl[(bl[0]<.05) & (bl[1]==0)]))/(len(bl[(bl[0]<.05) & (bl[1]==0)])+len(bl[(bl[0]>.05) & (bl[1]==0)]))

        n = pd.read_csv(options.inputfiles[0],sep='\t',header=None)[sub*10000:(sub+1)*10000]
        scoresn = np.asarray([1-i for i in n[0].values.astype(float)])
        yn = n[1].values.astype(int)
        fprn, tprn, thresholdsn = metrics.roc_curve(yn, scoresn)
        roc_aucn = metrics.auc(fprn, tprn)
        yn = float(len(n[(n[0]<.05) & (n[1]==1)]))/(len(n[(n[0]<.05) & (n[1]==1)])+len(n[(n[0]>.05) & (n[1]==1)]))
        xn = float(len(n[(n[0]<.05) & (n[1]==0)]))/(len(n[(n[0]<.05) & (n[1]==0)])+len(n[(n[0]>.05) & (n[1]==0)]))

        ls = pd.read_csv(options.inputfiles[4],sep='\t',header=None)[sub*10000:(sub+1)*10000]
        scoresls = np.asarray([1-i for i in ls[0].values.astype(float)])
        yls = ls[1].values.astype(int)
        fprls, tprls, thresholdsls = metrics.roc_curve(yls, scoresls)
        roc_aucls = metrics.auc(fprls, tprls)
        yls = float(len(ls[(ls[0]<.05) & (ls[1]==1)]))/(len(ls[(ls[0]<.05) & (ls[1]==1)])+len(ls[(ls[0]>.05) & (ls[1]==1)]))
        xls = float(len(ls[(ls[0]<.05) & (ls[1]==0)]))/(len(ls[(ls[0]<.05) & (ls[1]==0)])+len(ls[(ls[0]>.05) & (ls[1]==0)]))

        plt.plot(fpr, tpr, label='Circadian ROC curve (area = %0.2f)' % roc_auc, color = 'y')
        plt.scatter(xl,yl,color='y',marker='x')

        plt.plot(fprb, tprb, label='Replicate Block ROC curve (area = %0.2f)' % roc_aucb, color='b')
        plt.scatter(xb,yb,color='b',marker='x')

        plt.plot(fprbl, tprbl, label='Baseline ROC curve (area = %0.2f)' % roc_aucbl, color='g')
        plt.scatter(xbl,ybl,color='g',marker='x')

        plt.plot(fprn, tprn, label='Noise ROC curve (area = %0.2f)' % roc_aucn, color='r')
        plt.scatter(xn,yn,color='r',marker='x')

        plt.plot(fprls, tprls, label='Time Series ROC curve (area = %0.2f)' % roc_aucls, color='black')
        plt.scatter(xls,yls,color='black',marker='x')

    plt.axvline(x=0.05,color='black',ls='dashed')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.savefig(options.inputfiles[5])
    plt.close()

if __name__ == '__main__':
    main(sys.argv[1:])
