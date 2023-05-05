#!/usr/bin/python3

# python3 get_longest_cds.py <fa_file>

## import all libraries first!
from Bio import SeqIO

## read 

fa_aslist = list(SeqIO.parse(fa_file, 'fasta'))

def get_all_gene_ids(fa_aslist):

	gene_list = []

	for fa in fa_aslist:
		gene_id = fa.id.split('_i')[0]
		if gene_id not in gene_list:
			gene_list.append(gene_id)

	final_transcripts = []
	for gene in gene_list:
		transcripts_per_gene = []
		for fa in fa_aslist:
			if fa.id.split('_i')[0] == gene:
				transcripts_per_gene.append(fa)

		transcripts_len_list =[]

		for transcript in transcripts_per_gene:
			transcripts_len_list.append({'id': transcript.id, 'size' : len(str(transcript.seq))})

			transcript_len_list.sort(key=lambda x: x.get('size'), reverse=True)

			final_transcripts.append(transcript_len_list[0])

		transcripts_ids =[]

		for item in final_transcripts:
			transcripts_ids.append(item['id'])

		longest_transcripts = []

		for transcript in fa_aslist:
			if transcript.id in transcripts_ids:
				longest_transcripts.append(transcript)

		return longest_transcripts

	