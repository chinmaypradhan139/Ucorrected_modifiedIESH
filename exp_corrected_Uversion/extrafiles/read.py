sim_inp='fort.23'

f=open(sim_inp,'r')
lines=f.readlines()
vals=[]
for line in lines:
    v_lines=line.split()
    vals.append(v_lines[0])

print(vals[15],vals[16])

