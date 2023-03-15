#! /usr/bin/env python3

print("#!/bin/bash")

job_name = "ExampleRun"
queue = "comp72"
number_of_nodes = "1"
number_of_processors = "1" 
walltime = "00:01:00"

print("#SBATCH --job-name=", job_name)
print("#SBATCH --partition", queue)
print("#SBATCH --nodes=", number_of_nodes)
print("#SBATCH --tasks-per-node=", number_of_processors)
print("#SBATCH --time=", walltime)
print("#SBATCH -o %j.out")
print("#SBATCH -e %j.err")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=kkasmaii@uark.edu")

print("cd $SLURM_SUBMIT_DIR")

print("# job command here")
