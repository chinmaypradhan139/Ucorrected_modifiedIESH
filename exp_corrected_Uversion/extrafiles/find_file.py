import os
from os.path import exists

fil_name='fort.77'

cwd=os.getcwd()

no=80
for filno in range(1,no+1):
    if exists(os.path.join(cwd,str(filno),fil_name)):
        print('The file exists in folder '+str(filno))
