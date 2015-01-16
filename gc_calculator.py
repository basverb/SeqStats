# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 12:55:21 2015

@author: Bas Verbruggen
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def getGCcontent(dna):
    length = len(dna)
    g_count = dna.count('G')
    c_count = dna.count('C')
    GC_content  = ((g_count + c_count)/length) * 100
    return GC_content

def calculate_all_gc(sequences):
    headers = sequences[0]
    gc_contents = []
    
    for header in headers:
        gc =  getGCcontent(sequences[1].get(header))
        gc_contents.append(gc)
    
    return headers, gc_contents
    
def plot_histogram(gc_contents, query):
    plt.hist(gc_contents)
    plt.xlabel('GC content (%)')
    plt.ylabel('Frequency')
    plt.title('GC content in %s' % query)
    plt.show()
    
    