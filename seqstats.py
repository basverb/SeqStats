# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 11:33:12 2015

@author: Bas Verbruggen
"""
from sys import argv
from query_ncbi import *
from fasta import *
import GC_content_calculator

# Parse arguments
query = argv[1]
db = argv[2]

query = 'VP28'
db = 'nucleotide'
# Run scripts
query_ncbi(query, db)
sequences = fasta('query_result.fa')
# GC_content_calulator(sequences)
