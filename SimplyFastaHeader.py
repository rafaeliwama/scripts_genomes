#!/usr/bin/env python
from Bio import SeqIO
import sys

def rename_scaffolds(genome, prefix):
    """Substitutes seq.id with prefix + seq_number.
    Arguments - genome - SeqIO genome object
              - prefix - string with prefix
              returns seqs with new header and a map in list form"""
    genome_seqs = SeqIO.parse(genome, 'fasta')

    contig_count = 0 # loop counter
    list_map = [] # list object for list_map
    seqs_new_header = [] #seqs with new header
    
    for s in genome_seqs:
        map_holder = [s.name, prefix + '_' + str(contig_count)]
        list_map.append(map_holder)
        s.id = prefix + '_' + str(contig_count)
        s.description = ''
        s.features = ''
        s.dbxrefs = ''
        seqs_new_header.append(s)
        contig_count = contig_count + 1
        
    return seqs_new_header, list_map
        


renamed_gen = rename_scaffolds(sys.argv[1], sys.argv[2])[0]

SeqIO.write(renamed_gen, str(str(sys.argv[2]) + '_genome_renamed.fa'), 'fasta')


