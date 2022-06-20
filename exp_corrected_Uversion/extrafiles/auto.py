import os
import shutil
import subprocess as process
import sys
import time
import fileinput
import average
import numpy as np

src_path=os.getcwd()
indir='allinp'
dest_path=src_path+'/'+indir


class copyfiles:
    def __init__(self,folder):
        self.fil_names=['myscript.sh','Tulli13_1990.f90','progTulli12_1990.f90','gaussquad.f90','parallel_script_v4.py','average.py','job.sh']
        self.fold=folder
    def details(self):
        print(self.fold)
        for j,fils in enumerate(self.fil_names):
            shutil.copy(src_path+'/'+self.fil_names[j],dest_path+'/'+str(self.fold))
        os.chdir(dest_path)
    def average(self,ttraj):
        popfiles=['fort.150','fort.180']
        outname=['csq_no_','r_no_']
        for k in range(len(popfiles)):
            pop=average.average(popfiles[k],ttraj,'running')
            np.savetxt(dest_path+'/'+str(self.fold)+'/'+'running'+'/'+outname[k]+str(self.fold),np.c_[pop[0],pop[1]])
            print(pop)

    def main(self,tim,ttraj):
        run=copyfiles(self.fold)    
        run.details()
        os.chdir(dest_path+'/'+str(self.fold))
        process.call("(chmod +x myscript.sh)",shell=True)
        process.call("(./myscript.sh)",shell=True)
        pfiles=['fort.150','fort.180']
        for ip in pfiles:
            for iq in range(1,ttraj+1):
                file_path=dest_path+'/'+str(self.fold)+'/running'+'/'+str(iq)+'/'+str(ip)
                while not os.path.exists(file_path):
                    time.sleep(2)
        run.average(ttraj)
        os.chdir(dest_path)
        



