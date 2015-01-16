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

def main(options):
    # Check and process commandline arguments
    assert len(options) == 3, "Provide at least two arguments: 1. gene query 2. database ('nucleotide' or 'protein')"
    query = options[1]
    db = options[2]
    
    # Run scripts
    print '#1 query NCBI'
    query_ncbi(query, db)
    print '#2 parse fasta file'
    sequences = fasta('query_result.fa')
    print '#3 calculate gc content'
    headers, gc_contents = calculate_all_gc(sequences)
    print '#4 plot histogram'
    plot_histogram(gc_contents, query)



main(argv)