---
title: "assn-03"
author: "kkasmaii"
date: "2023-03-10"
output: md_document
editor_options: 
  markdown: 
    wrap: 72
---

1.  Uploaded the mt_genomes directory
    `rsync -avz mt_genomes kkasmaii@hpc-portal2.hpc.uark.edu:/storage/kkasmaii/`

2.  Uploaded 'unknown.fa'
    `scp unknown.fa kkasmaii@hpc-portal2.hpc.uark.edu:/storage/kkasmaii/mt_genomes`

3.  Wrote a slurm script for the following actions: purge the modules,
    load a blast module, concatenate all the genomes a file named
    'genomes.fas', make a blast database of the genomes, and search the
    unknown sequence against your database `nano Assignment_3.slurm` and
    `sbatch Assignment_3.slurm`

4.  Synchronized the remote mt_genomes with the local version of
    mt_genomes
    `rsync -avz mt_genomes kkasmaii@hpc-portal2.hpc.uark.edu:~/desktop/watermelon_files/mt_genomes/`

    1.  How long did it take your job to complete? 3 seconds

    2.  What is the closest match in the database? Cucurbita

    3.  Can you tell from the coordinates which gene is in unknown.fa?
        Skipped question
