# SeqStats
Software Carpentry - Final day project
===========================================
README- seqstats.py 
===========================================

seqstats is a command line tool for retrieving data from the NCBI database (Nucleotide or protein) for any given gene 
across all database entries. 
Data is subsequently stored in a single FASTA file. The GC content is calculated per data entry and plotted on a histogram. 

This tool was created as part of  an exercise for the purposes of a software carpentry workshop... 
Use with CAUTION...

Command line execution: 
-------------------------------------------
$ python seqstats.py "gene name" "nucleotide OR protein"


Projects, sub-modules and libraries 
-------------------------------------------
- sys
- urllib2
- xmltodict
- numpy
- matplotlib.pyplot

Authors 
------------------------------------------
Bas Verbruggen, Thomasz Stawski & Lauren Laing

Author contact
------------------------------------------
bv213@exeter.ac.uk

legal notices (crypto stuff)
-----------------------------------------
GNU GENERAL PUBLIC LICENCE
