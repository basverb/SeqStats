# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 13:14:10 2015

@author: Bas Verbruggen
"""
# packages and modules
import urllib2
import xmltodict

def query_ncbi(query='', db='nucleotide', fileout='query_result.fa', raw_query=False):
    """
    Search NCBI with a query and retrieve files in fasta format
    
    Arguments:
    query = The search query (e.g. 'VP28')
    db = The NCBI database (either 'nucleotide' or 'protein')
    fileout = The output file (e.g. 'VP28.fa')
    raw_query = Do you want to use query raw or use the build-in modification
                that remove complete genomes, chromosomes and add appropriate 
                lables (True / False)
        
    """
    # Test the query 
    query = str(query)
    assert len(query) > 1, 'The query was empty'
    assert db == 'nucleotide' or db == 'protein', 'Please use either db=nucleotide or db=protein'
    print 'query accepted: %s' % query
    
    if not raw_query:
        # NCBI might return complete genomes / chromosomes, this is not informative
        if db == 'nucleotide':
            term = query + '[Gene+Name]+NOT+genome+NOT+chromosome'
        else:
            term = query + '[Protein+Name]'
    else:
        term = query
    
    # Build the NCBI search query
    base_url = 'http://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    # esearch query
    search_url = base_url + 'esearch.fcgi?db=' + db + '&term=' + term + '&usehistory=y'
    # get response from server
    file = urllib2.urlopen(search_url)
    data = file.read()
    file.close()
    
    # parse xml into a dictionary
    data = xmltodict.parse(data)
    
    # Test if the query was valid
    assert data['eSearchResult'].get('ErrorList') is None, 'Error in query: ' + ' '.join(data['eSearchResult'].get('ErrorList').keys())
    
    # get the WebEnv and QueryKey
    query_key = str(data['eSearchResult'].get('QueryKey'))
    web_env = str(data['eSearchResult'].get('WebEnv'))
    
    # esearch produces WebEnv value ($web1) and QueryKey value ($key1), use this to download results in fasta format
    fetch_url = base_url + 'efetch.fcgi?db=' + db +'&query_key=' + query_key + '&WebEnv=' + web_env + '&rettype=fasta&retmode=text'
    
    file = urllib2.urlopen(fetch_url)
    data = file.read()
    file.close()
    
    # Write to output file
    fileout_handle = open(fileout, 'w')
    fileout_handle.write(data)
    fileout_handle.close()
    print 'output written to: %s' % fileout
    

# Run for DEBUG:
# Succesful query
# query_ncbi(query='VP28', db='nucleotide', fileout='sequence.fasta', raw_query=False)
# Bad query
# query_ncbi(query='VP28232333', db='nucleotide', fileout='sequence.fasta', raw_query=False)



