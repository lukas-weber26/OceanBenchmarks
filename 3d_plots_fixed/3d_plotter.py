import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data_a100 = pd.read_csv("./a100_3d.csv", delimiter=",",index_col=None)
hydrostatic_a100 = data_a100[(data_a100["Model"] == "Hydrostatic")]

data_h100 = pd.read_csv("./h100_3d.csv", delimiter=",",index_col=None)
hydrostatic_h100 = data_h100[(data_h100["Model"] == "Hydrostatic")]
 
data_cpu = pd.read_csv("./cpu_3d.csv", delimiter=",",index_col=None)
hydrostatic_cpu = data_cpu[(data_cpu["Model"] == "Hydrostatic")]

grid_sizes = np.array([32,64,128])

#comparison of the gpus
plt.loglog(grid_sizes, hydrostatic_a100["MeanTime"][:3])
plt.loglog(grid_sizes, hydrostatic_h100["MeanTime"][:3])
plt.loglog(grid_sizes, hydrostatic_cpu["MeanTime"][:3])
plt.title("Hydrostatic Model A100 vs H100 3D vs CPU")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["A100","H100","CPU"])
plt.savefig("NonHydrostatic_Comparison.png")
plt.clf()


data_a100 = pd.read_csv("./a100_3d.csv", delimiter=",",index_col=None)
hydrostatic_a100 = data_a100[(data_a100["Model"] == "Nonhydrostatic")]

data_h100 = pd.read_csv("./h100_3d.csv", delimiter=",",index_col=None)
hydrostatic_h100 = data_h100[(data_h100["Model"] == "Nonhydrostatic")]
 
data_cpu = pd.read_csv("./cpu_3d.csv", delimiter=",",index_col=None)
hydrostatic_cpu = data_cpu[(data_cpu["Model"] == "Nonhydrostatic")]

grid_sizes = np.array([32,64,128])

#comparison of the gpus
plt.loglog(grid_sizes, hydrostatic_a100["MeanTime"][:3])
plt.loglog(grid_sizes, hydrostatic_h100["MeanTime"][:3])
plt.loglog(grid_sizes, hydrostatic_cpu["MeanTime"][:3])
plt.title("Hydrostatic Model A100 vs H100 3D vs CPU")
plt.xlabel("Grid Size")
plt.ylabel("Mean Time")
plt.legend(["A100","H100","CPU"])
plt.savefig("Hydrostatic_Comparison.png")
plt.clf()

