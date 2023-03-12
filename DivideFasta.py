#!/usr/bin/env python3
### requires SeqIO

from Bio import SeqIO
import math
import sys

def divide_sequences(fasta_file, number_files, prefix_new):
    '''Divides sequences in a fasta file in given number of files.
    Usage: divide_sequences(fasta_file, number_files, prefix_new)
    writes new fasta files with the given prefix'''
    Seqs = list(SeqIO.parse(str(fasta_file), 'fasta'))
    num_files = int(number_files)
    pref_str = str(prefix_new)

    while num_files != 0:
            num_seqs = (len(Seqs)/num_files)
            new_seqs_file = []
            while math.floor(num_seqs) != 0:
                test = Seqs.pop(0)
                new_seqs_file.append(test)
                num_seqs = num_seqs - 1

            SeqIO.write(new_seqs_file, pref_str + str(num_files), 'fasta')

            num_files = num_files - 1


divide_sequences(sys.argv[1], sys.argv[2], sys.argv[3])
