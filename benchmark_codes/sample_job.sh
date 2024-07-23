#!/bin/bash

#SBATCH --mail-user=YOUR_EMAIL
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name="Oceananigans_benchmark"
#SBATCH --partition=gpu_a100 
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --time=1:00:00
#SBATCH --mem-per-cpu=2000
#SBATCH --gres=gpu:a100:1
#SBATCH --mem-per-gpu=80G  <MAKE SURE TO ADJUST THIS NUMBER>
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

echo "Cuda device: $CUDA_VISIBLE_DEVICES"
echo "======= Start memory test ======="
julia /work/PATH_TO_BENCHMARK
echo "done"
