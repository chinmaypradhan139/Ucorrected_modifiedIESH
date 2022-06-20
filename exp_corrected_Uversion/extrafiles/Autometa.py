# Automating input
import os
import shutil
import subprocess as process
import fileinput
import time
import os.path
import sys
import auto

no_orbitals=[6,10]
l_bound=-1
u_bound=1
Gamma=[1.0E-04,1.0E-05]
Band_width=[3.0E-02,5.0E-02]
omg=2.0E-04
g=[5.6097,10.6097,15.6097]
dG=[-1.0E-03,-3.8E-03,-6.0E-03]
Temp=[2.0E-04,9.5E-04,4.0E-03]
dtc=10
dtq=1
dim=1
time_steps=20
total_traj=40

def inlist(a,b,c,d,e,f):
    input=[]
    inp_str=[]

    input.append(no_orbitals[a])
    inp_str.append(' no_orbitals')

    inp_str.append(' !l_bound')
    input.append(l_bound)
    inp_str.append(' !u_bound')
    input.append(u_bound)

    inp_str.append(' !Gamma')
    input.append(Gamma[b])

    inp_str.append(' !Band_width')
    input.append(Band_width[c])

    inp_str.append(' !spacing')
    input.append(1)

    inp_str.append(' !omega')
    input.append(omg)

    inp_str.append(' !g')
    input.append(g[d])

    inp_str.append(' !dG')
    input.append(dG[e])

    inp_str.append(' !Temp')
    input.append(Temp[f])

    inp_str.append(' !dtc')
    input.append(dtc)

    inp_str.append(' !dtq')
    input.append(dtq)

    inp_str.append(' dim')
    input.append(dim)

    inp_str.append(' !time_steps')
    input.append(time_steps)


    return input,inp_str    



os.mkdir(auto.indir)
os.chdir(auto.indir)

file1='/k_marcus.f90'
file2='/marcus_plot.f90'
file3='/main_marcus.f90'

k=0
Ls=[0,0,0,0]
quant=[Gamma,g,dG,Temp]
times=[]
for j in range(len(Ls)):
    while Ls[j]<len(quant[j]):
        k=k+1
        os.mkdir(str(k))
        inp=inlist(1,Ls[0],0,Ls[1],Ls[2],Ls[3])
        f=open('fort.23', 'w')
        for i in range(len(inp[0])):
            f.write(str(inp[0][i])+inp[1][i]+'\n')
        f.close()
        shutil.move('fort.23',str(k))
        shutil.copy(auto.src_path+file1,auto.dest_path+'/'+str(k))
        shutil.copy(auto.src_path+file2,auto.dest_path+'/'+str(k))
        shutil.copy(auto.src_path+file3,auto.dest_path+'/'+str(k))
        os.chdir(str(k))
        process.call('gfortran -c marcus_plot.f90', shell=True)
        process.call('gfortran marcus_plot.f90 k_marcus.f90', shell=True)
        process.call('./a.out',shell=True)
        go=open('fort.17', 'r')
        ta=go.read()
        cao=float(ta)
        tao=int(cao)
        go.close()
       
        if (tao<1000):
            times.append(tao)
         #   print(times)
            with fileinput.FileInput('fort.23', inplace=True) as file:
                for line in file:
                    print(line.replace('20 !time_steps', str(tao)+' !time_steps'), end='')
            process.call('gfortran marcus_plot.f90 main_marcus.f90', shell=True)
            process.call('./a.out',shell=True)
            os.chdir(auto.dest_path)#You can add code after this nline for generalization
            Ls[j]=Ls[j]+1
            print(Ls)
        else:
            
            Ls[j]=Ls[j]+1
            os.chdir(auto.dest_path)
            process.call('rm -r '+str(k),shell=True)
            k=k-1
        

    Ls[j]=0

print(times)

for im,vals in enumerate(range(3),start=1):
    print(im,vals)
    run=auto.copyfiles(im)    
    run.main(times[vals],2)


