#! /usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description="This script produces a parse.GFF")

parser.add_argument("gff_name", help="", type=str)
parser.add_argument("FASTA_file", help="", type=str)

args = parser.parse_args()

g = open(args.gff_name, 'r') 
lines = g.readlines()

g.close()
