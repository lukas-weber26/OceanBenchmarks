import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data_p100 = pd.read_csv("./Oceananigans_Benchmark_p100.csv", delimiter=",",index_col=None)
hydrostatic_p100 = data_p100[(data_p100["Model"] == "Hydrostatic")]
non_hydrostatic_p100 = data_p100[(data_p100["Model"] == "Nonhydrostatic")]
shallow_water_p100 = data_p100[(data_p100["Model"] == "ShallowWater")]

data_a100 = pd.read_csv("./Oceananigans_Benchmark_a100.csv", delimiter=",",index_col=None)
hydrostatic_a100 = data_a100[(data_a100["Model"] == "Hydrostatic")]
non_hydrostatic_a100 = data_a100[(data_a100["Model"] == "Nonhydrostatic")]
shallow_water_a100 = data_a100[(data_a100["Model"] == "ShallowWater")]

data = pd.read_csv("./Oceananigans_Benchmark_Headnode.csv", delimiter=",",index_col=None)
hydrostatic = data[(data["Model"] == "Hydrostatic")]
non_hydrostatic = data[(data["Model"] == "Nonhydrostatic")]
shallow_water = data[(data["Model"] == "ShallowWater")]

grid_sizes = np.array([32,64,128,256,512,1024,2048,4096])

#second = np.poly1d(np.polyfit(grid_sizes, np.array(hydrostatic_a100["MeanTime"]),2))
#third = np.poly1d(np.polyfit(grid_sizes, np.array(hydrostatic_a100["MeanTime"]),3))
#fourth = np.poly1d(np.polyfit(grid_sizes, np.array(hydrostatic_a100["MeanTime"]),4))
#fifth= np.poly1d(np.polyfit(grid_sizes, np.array(hydrostatic_a100["MeanTime"]),5))
#
#plt.loglog(grid_sizes, hydrostatic_a100["MeanTime"])
#plt.loglog(grid_sizes, second(grid_sizes))
#plt.loglog(grid_sizes, third(grid_sizes))
#plt.loglog(grid_sizes, fourth(grid_sizes))
#plt.loglog(grid_sizes, fifth(grid_sizes))
#plt.title("Comparison of Theoretical and Acutal Performance")
#plt.xlabel("Grid Size")
#plt.ylabel("Mean Time")
#plt.legend(["A100","Curve Fit"])
#plt.savefig("A100_hydrostatic_curve_fit.png")
#plt.clf()
#
#second = np.poly1d(np.polyfit(grid_sizes, np.array(non_hydrostatic_a100["MeanTime"]),2))
#third = np.poly1d(np.polyfit(grid_sizes, np.array(non_hydrostatic_a100["MeanTime"]),3))
#fourth = np.poly1d(np.polyfit(grid_sizes, np.array(non_hydrostatic_a100["MeanTime"]),4))
#fifth= np.poly1d(np.polyfit(grid_sizes, np.array(non_hydrostatic_a100["MeanTime"]),5))
#
#plt.loglog(grid_sizes, non_hydrostatic_a100["MeanTime"])
#plt.loglog(grid_sizes, second(grid_sizes))
##plt.loglog(grid_sizes, third(grid_sizes))
##plt.loglog(grid_sizes, fourth(grid_sizes))
##plt.loglog(grid_sizes, fifth(grid_sizes))
#plt.title("Comparison of Theoretical and Acutal Performance")
#plt.xlabel("Grid Size")
#plt.ylabel("Mean Time")
#plt.legend(["A100","Curve Fit"])
#plt.savefig("A100_non_hydrostatic_curve_fit.png")
#plt.clf()


##section 1: comparing the models on different devices 
#plt.loglog(grid_sizes, hydrostatic_p100["MeanTime"])
#plt.loglog(grid_sizes, hydrostatic_a100["MeanTime"])
#plt.loglog(grid_sizes, hydrostatic["MeanTime"])
#plt.title("Hydrostatic Model on Three Systems")
#plt.xlabel("Grid Size")
#plt.ylabel("Mean Time")
#plt.legend(["P100","A100","CPU"])
#plt.savefig("Hydrostatic_comparison.png")
#plt.clf()
#
#plt.loglog(grid_sizes, non_hydrostatic_p100["MeanTime"])
#plt.loglog(grid_sizes, non_hydrostatic_a100["MeanTime"])
#plt.loglog(grid_sizes, non_hydrostatic["MeanTime"])
#plt.title("Non Hydrostatic Model on Three Systems")
#plt.xlabel("Grid Size")
#plt.ylabel("Mean Time")
#plt.legend(["P100","A100","CPU"])
#plt.savefig("Non_Hydrostatic_comparison.png")
#plt.clf()
#
#plt.loglog(grid_sizes, shallow_water_p100["MeanTime"])
#plt.loglog(grid_sizes, shallow_water_a100["MeanTime"])
#plt.loglog(grid_sizes, shallow_water["MeanTime"])
#plt.title("Hydrostatic Model on Three Systems")
#plt.xlabel("Grid Size")
#plt.ylabel("Mean Time")
#plt.legend(["P100","A100","CPU"])
#plt.savefig("Shallow_water_comparison.png")
#plt.clf()
#
##section 1: Repeat previous plots without cpu
#plt.loglog(grid_sizes, hydrostatic_p100["MeanTime"])
#plt.loglog(grid_sizes, hydrostatic_a100["MeanTime"])
#plt.title("Shallow Water Model on GPUs")
#plt.xlabel("Grid Size")
#plt.ylabel("Mean Time")
#plt.legend(["P100","A100"])
#plt.savefig("Hydrostatic_comparison_gpu.png")
#plt.clf()
#
#plt.loglog(grid_sizes, non_hydrostatic_p100["MeanTime"])
#plt.loglog(grid_sizes, non_hydrostatic_a100["MeanTime"])
#plt.title("Non Hydrostatic Model on GPUs")
#plt.xlabel("Grid Size")
#plt.ylabel("Mean Time")
#plt.legend(["P100","A100"])
#plt.savefig("Non_Hydrostatic_comparison_gpu.png")
#plt.clf()
#
#plt.loglog(grid_sizes, shallow_water_p100["MeanTime"])
#plt.loglog(grid_sizes, shallow_water_a100["MeanTime"])
#plt.title("Shallow Water Model on GPUs")
#plt.xlabel("Grid Size")
#plt.ylabel("Mean Time")
#plt.legend(["P100","A100"])
#plt.savefig("Shallow_water_comparison_gpu.png")
#plt.clf()
#
##do the models have considerably different performances? 
plt.loglog(grid_sizes, hydrostatic_a100["MeanTime"])
plt.loglog(grid_sizes, non_hydrostatic_a100["MeanTime"])
plt.loglog(grid_sizes, shallow_water_a100["MeanTime"])
plt.title("Comparison of Models on the A100 GPU")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["Hydrostatic","Non Hydrostatic", "Shallow Water"])
plt.savefig("model_comparison_a100.png")
plt.clf()

plt.loglog(grid_sizes, hydrostatic["MeanTime"])
plt.loglog(grid_sizes, non_hydrostatic["MeanTime"])
plt.loglog(grid_sizes, shallow_water["MeanTime"])
plt.title("Comparison of Models on the CPU")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["Hydrostatic","Non Hydrostatic", "Shallow Water"])
plt.savefig("model_comparison_cpu.png")
plt.clf()

plt.loglog(grid_sizes, hydrostatic_p100["MeanTime"])
plt.loglog(grid_sizes, non_hydrostatic_p100["MeanTime"])
plt.loglog(grid_sizes, shallow_water_p100["MeanTime"])
plt.title("Comparison of Models on the P100 GPU")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["Hydrostatic","Non Hydrostatic", "Shallow Water"])
plt.savefig("model_comparison_p100.png")
plt.clf()

