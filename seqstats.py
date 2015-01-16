# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 11:33:12 2015

@author: Bas Verbruggen
"""
# Parse arguments
from sys import argv
from query_ncbi import *
from fasta import *
from gc_calculator import *

query = argv[1]
db = argv[2]

#query = 'vtg1'
#db = 'nucleotide'
# Run scripts
query_ncbi(query, db)
sequences = fasta('query_result.fa')
headers, gc_contents = calculate_all_gc(sequences)
plot_histogram(gc_contents, query)