#! /usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description="This script produces a parse.GFF")

parser.add_argument("gff", help="", type=str)

args = parser.parse_args()

g = open(args.gff, 'r') 

for line in g:
	line = line.rstrip("\n")
	split = line.split("\t")
	length = int(split[4]) - int(split[3])
	length += 1
	print(split[2], str(len))

print('done!')

