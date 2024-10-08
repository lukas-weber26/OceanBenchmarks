import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data_a100 = pd.read_csv("./a100_3d.csv", delimiter=",",index_col=None)
hydrostatic_a100 = data_a100[(data_a100["Model"] == "Hydrostatic")]

data_h100 = pd.read_csv("./h100_3d.csv", delimiter=",",index_col=None)
hydrostatic_h100 = data_h100[(data_h100["Model"] == "Hydrostatic")]

grid_sizes = np.array([32,64,128,265,512])

#comparison of the gpus
plt.loglog(grid_sizes, hydrostatic_a100["MeanTime"])
plt.loglog(grid_sizes, hydrostatic_h100["MeanTime"])
plt.title("Hydrostatic Model A100 vs H100 3D vs CPU")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["A100","H100"])
plt.savefig("GPU_Hydrostatic_Comparison.png")
plt.clf()

data_a100 = pd.read_csv("./a100_3d.csv", delimiter=",",index_col=None)
hydrostatic_a100 = data_a100[(data_a100["Model"] == "Nonhydrostatic")]

data_h100 = pd.read_csv("./h100_3d.csv", delimiter=",",index_col=None)
hydrostatic_h100 = data_h100[(data_h100["Model"] == "Nonhydrostatic")]

grid_sizes = np.array([32,64,128,265,512])

#comparison of the gpus
plt.loglog(grid_sizes, hydrostatic_a100["MeanTime"])
plt.loglog(grid_sizes, hydrostatic_h100["MeanTime"])
plt.title("Hydrostatic Model A100 vs H100 3D vs CPU")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["A100","H100"])
plt.savefig("GPU_Non_Hydrostatic_Comparison.png")
plt.clf()
