import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data_a100 = pd.read_csv("./A100.csv", delimiter=",",index_col=None)
hydrostatic_a100 = data_a100[(data_a100["Model"] == "Hydrostatic")]
non_hydrostatic_a100 = data_a100[(data_a100["Model"] == "Nonhydrostatic")]
shallow_water_a100 = data_a100[(data_a100["Model"] == "ShallowWater")]
shallow_water_conservative_a100 = data_a100[(data_a100["Model"] == "ShallowWaterConservative")]

data_h100 = pd.read_csv("../../Oceananigans_Benchmark:2024-08-13T18:48:46.040.csv", delimiter=",",index_col=None)
hydrostatic_h100 = data_h100[(data_h100["Model"] == "Hydrostatic")]
non_hydrostatic_h100 = data_h100[(data_h100["Model"] == "Nonhydrostatic")]
shallow_water_h100 = data_h100[(data_h100["Model"] == "ShallowWater")]
shallow_water_conservative_h100 = data_h100[(data_h100["Model"] == "ShallowWaterConservative")]

grid_sizes = np.array([32,64,128,256,512,1024,2048,4096,4096*2])

#comparison of the gpus
plt.loglog(grid_sizes, hydrostatic_a100["MeanTime"])
plt.loglog(grid_sizes, hydrostatic_h100["MeanTime"])
plt.title("Hydrostatic Model A100 vs H100")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["A100","H100"])
plt.savefig("Hydrostatic_A100_H100.png")
plt.clf()

plt.loglog(grid_sizes, non_hydrostatic_a100["MeanTime"])
plt.loglog(grid_sizes, non_hydrostatic_h100["MeanTime"])
plt.title("Non Hydrostatic Model A100 vs H100")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["A100","H100"])
plt.savefig("Non_Hydrostatic_A100_H100.png")
plt.clf()

plt.loglog(grid_sizes, shallow_water_a100["MeanTime"])
plt.loglog(grid_sizes, shallow_water_h100["MeanTime"])
plt.title("Shallow Water Model A100 vs H100")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["A100","H100"])
plt.savefig("Shallow_water_A100_H100.png")
plt.clf()

plt.loglog(grid_sizes, shallow_water_conservative_a100["MeanTime"])
plt.loglog(grid_sizes, shallow_water_conservative_h100["MeanTime"])
plt.title("Shallow Water Model (Conservative) A100 vs H100")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["A100","H100"])
plt.savefig("Conservative_shallow_water_A100_H100.png")
plt.clf()

#model comparison
plt.loglog(grid_sizes, hydrostatic_a100["MeanTime"])
plt.loglog(grid_sizes, non_hydrostatic_a100["MeanTime"])
plt.loglog(grid_sizes, shallow_water_a100["MeanTime"])
plt.loglog(grid_sizes, shallow_water_conservative_a100["MeanTime"])
plt.title("A100 Model Comparison")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["Hydrostatic","Non Hydrostatic", "Shallow Water", "Shallow water (conservative)"])
plt.savefig("Model_comparison_a100.png")
plt.clf()

plt.loglog(grid_sizes, hydrostatic_h100["MeanTime"])
plt.loglog(grid_sizes, non_hydrostatic_h100["MeanTime"])
plt.loglog(grid_sizes, shallow_water_h100["MeanTime"])
plt.loglog(grid_sizes, shallow_water_conservative_h100["MeanTime"])
plt.title("H100 Model Comparison")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["Hydrostatic","Non Hydrostatic", "Shallow Water", "Shallow water (conservative)"])
plt.savefig("Model_comparison_h100.png")
plt.clf()
