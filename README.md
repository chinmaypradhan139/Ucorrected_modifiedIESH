# Ucorrected_modifiedIESH
modified IESH with proper calculation of Umatrix
Input file for both IESH and marcus result is fort.23
Tulli13_1990.f90 is the mod file for modified IESH
progTulli12_1990.f90 is the main file for modified IESH
marcus_plot.f90 is the mod_file for marcus population
main_marcus.f90 is the main file for calculating the marcus population 
In the linux terminal
To run the code of marcus compile ifort marcus_plot.f90 main_marcus.f90 and run it with ./a.out
To run modified IESH simply run chmod +x myscript.sh then ./myscript.sh
after successful run a folder called running gets created which contains different trajectories in different folders
To average the population , copy avg.py in running folder
set file in avg.py to fort.180
specify correct number of trajectories and nodes in avg.py
run avg.py to produce output.txt which is the main output
