#!/usr/bin/python3
## usage: python3 select_best_sra_transcriptomes.py <SRA_RunInfo_file>
## required packages: pandas
## selects best SRA transcriptome runs of each species based on size. It gives preference for paired runs

## import python libraries
import pandas as pd
import sys

runs_df = pd.read_csv(sys.argv[1])

runs_df_sorted = runs_df.sort_values(by=['TaxID', 'size_MB'], ascending=False) ## sort by TaxID and size_MB

runs_df_sorted_illumina = runs_df_sorted.loc[runs_df_sorted['Platform'] == 'ILLUMINA'] ## select only illumina data

runs_df_sorted_illumina = runs_df_sorted_illumina.loc[runs_df_sorted['LibrarySource'] == 'TRANSCRIPTOMIC'] ## select only illumina data

runs_df_sorted_paired = runs_df_sorted_illumina.loc[runs_df_sorted_illumina['LibraryLayout'] == 'PAIRED'] ## select only paired runs

runs_df_sorted_single = runs_df_sorted_illumina.loc[runs_df_sorted_illumina['LibraryLayout'] == 'SINGLE'] ## select only single runs

paired_runs_final_set = runs_df_sorted_paired.drop_duplicates(subset=['TaxID']) # drop duplicates to get highest size

single_runs_final_set = runs_df_sorted_single.drop_duplicates(subset=['TaxID'])# drop duplicates to get highest size

## make a initial list of ncbi_tax_ids
tax_ids_lst = list(set(runs_df['TaxID']))

# create dictionary for a True or False

is_filled = {}

for tax_id in tax_ids_lst:  ## assigns False to all TaxIDs
    is_filled[tax_id] = 'NA'
is_filled

for tax_id in set(paired_runs_final_set['TaxID']):
    is_filled[tax_id] = 'Paired'


for tax_id in set(single_runs_final_set['TaxID']):
    if is_filled[tax_id] == 'NA':
        is_filled[tax_id] = 'Single'
    else:
        pass

is_filled

final_df = pd.DataFrame(columns=runs_df.columns)

for tax_id in is_filled:
    if is_filled[tax_id] == 'Paired':
        target_rows = paired_runs_final_set.loc[paired_runs_final_set['TaxID'] == tax_id]
        final_df = pd.concat([final_df, target_rows])

    if is_filled[tax_id] == 'Single':
        target_rows = single_runs_final_set.loc[single_runs_final_set['TaxID'] == tax_id]
        final_df = pd.concat([final_df, target_rows])

final_df.to_csv(sys.argv[1] + '_best.csv')

list_runs = open('lst_runs_' + sys.argv[1], 'w')

for ids in final_df['Run']:
    list_runs.write("%s\n" % ids)


print('Enjoy')
