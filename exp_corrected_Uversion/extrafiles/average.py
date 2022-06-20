#averager_mod
import numpy as np
from numpy.core.fromnumeric import size
import os
import math
import subprocess as process
from pathlib import Path

#cwd=os.getcwd()
#tar=cwd+'/testavg'




def average(fil_typ,folds,tar):
    ps=os.getcwd()
    print(ps,'ps')
    os.chdir(tar+'/1')
    fp=open(fil_typ,'r')
    data1=np.loadtxt(fil_typ)
    fp.close()
    os.chdir(ps)
    for i,val in enumerate(range(folds-1),start=2):

        os.chdir(tar)
        os.chdir(str(i))        
        fq=open(fil_typ,'r')
        data=np.loadtxt(fil_typ)
        data1[:,1]=data1[:,1]+data[:,1]
        fq.close()
        os.chdir(ps)
    return data1[:,0],data1[:,1]/folds




