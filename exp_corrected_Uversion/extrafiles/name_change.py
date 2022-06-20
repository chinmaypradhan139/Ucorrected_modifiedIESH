import shuttil as sh
import os

folders=10
for i in range(1,folders+1):
    sh.move("csq_no_"+str(i),"dcsq_no_"+str(i))
    sh.move("r_no_"+str(i),"dr_no_"+str(i))



