push!(LOAD_PATH, joinpath(@__DIR__, ".."))

using BenchmarkTools
using CUDA
using Oceananigans
using Oceananigans.Utils: oceananigans_versioninfo, versioninfo_with_gpu
using CairoMakie
using Dates

#anything that you may wish to modify goes here
gridSizes = [(32, 32), (64, 64), (128, 128), (256, 256), (512, 512), (1024, 1024), (2048, 2048), (4096, 4096), (8192, 8192), (16384, 16384)]

#helper functions 
function writeTrial(B)

        date = string(Dates.now())
        callName = "Oceananigans_Benchmark:" * date * ".csv"

        open(callName, "w") do io
                write(io, "Model,GridType,GridSize,MinTime,MedianTime,MeanTime,MaxTime,Memory,Allocs,NumSamples\n")
                for trialDict in B
                        t = trialDict["trial"]
                        trialInfo = trialDict["model"] * "," * trialDict["gridType"] * "," * trialDict["gridSize"][1] * "," * string(minimum(t.times)) * "," * string(median(t.times)) * "," * string(mean(t.times)) * "," * string(maximum(t.times)) * "," * string(t.memory) * "," * string(t.allocs) * "," * string(t.params.samples) * "\n"

                        write(io, trialInfo)
                end
        end
end

#main code 
completedBenchmarks = []
for m in ["Hydrostatic", "Nonhydrostatic", "ShallowWater", "ShallowWaterConservative"]
        for g in gridSizes
                println("Starting Case ", string(g))

                if (m == "Nonhydrostatic")
                        grid = RectilinearGrid(GPU(), size=g, x=(0, 2 * 3.14), y=(0, 2 * 3.14), topology=(Periodic, Periodic, Flat))
                        model = NonhydrostaticModel(; grid, advection=WENO())

                        e(e, y) = 2rand() - 1
                        set!(model, u=e, v=e)
                elseif (m == "Hydrostatic")
                        grid = RectilinearGrid(GPU(), size=(g[1], g[2], 1), extent=(1, 1, 1))
                        model = HydrostaticFreeSurfaceModel(; grid)

                elseif (m == "ShallowWater")
                        grid = RectilinearGrid(GPU(), size=g, x=(0, 2 * 3.14), y=(0, 2 * 3.14), topology=(Periodic, Periodic, Flat), halo=(3, 3))
                        model = ShallowWaterModel(grid=grid, gravitational_acceleration=1.0, formulation=VectorInvariantFormulation())
                        set!(model, h=1)
                elseif (m == "ShallowWaterConservative")
                        grid = RectilinearGrid(GPU(), size=g, x=(0, 2 * 3.14), y=(0, 2 * 3.14), topology=(Periodic, Periodic, Flat), halo=(3, 3))
                        model = ShallowWaterModel(grid=grid, gravitational_acceleration=1.0, formulation=ConservativeFormulation())
                        set!(model, h=1)
                else
                        println("Invalid choice of model")
                        break
                end

                trial = @benchmark begin
                        CUDA.@sync blocking = true time_step!($model, 1)
                end samples = 10

                push!(completedBenchmarks, Dict("trial" => trial, "model" => m, "gridType" => "RectilinearGrid", "gridSize" => string(g))
                )
        end
end

writeTrial(completedBenchmarks)


