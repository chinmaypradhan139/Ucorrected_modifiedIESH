import os
import shutil

get=os.getcwd()
no_fold=10
dest='/home/chinmay/7jan2022backup11/mytemp1/'

for i in range(1,no_fold+1):
    os.chdir(str(i))
    shutil.copy('dcsq_no_'+str(i),dest+str(i))
    shutil.copy('dr_no_'+str(i),dest+str(i))
    os.chdir(get)
    print(os.getcwd())
