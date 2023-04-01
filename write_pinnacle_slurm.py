#! /usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description="This script produces a slurm script")
parser.add_argument("job_name", help="", type=str)

parser.add_argument("-q", "--queue", help="Which queue the slurm will be sent to, default= 1", 
default="comp72")
parser.add_argument("-n", "--number_of_nodes", help="Number of nodes that will be used, default= 1", 
default="1")
parser.add_argument("-p", "--number_of_processors", help="Number of processors used, default= 1", 
default="1")
parser.add_argument("-w", "--walltime", help="Amount of time the job will take before being killed, default= 1:00:00", default="1:00:00")


print("#!/bin/bash")

args = parser.parse_args()

print("#SBATCH --job-name=", args.job_name)
print("#SBATCH --partition", args.queue)
print("#SBATCH --nodes=", args.number_of_nodes)
print("#SBATCH --tasks-per-node=", args.number_of_processors)
print("#SBATCH --time=", args.walltime)
print("#SBATCH -o %j.out")
print("#SBATCH -e %j.err")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=kkasmaii@uark.edu")

print("cd $SLURM_SUBMIT_DIR")

print("# job command here")
