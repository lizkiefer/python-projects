"""
File:  main.py
Author: Liz Kiefer

Given a file name, reads it as a FASTA-formatted file and prints statistics to an output file
about the sequences present in the file.
"""

import argparse
import sys
import pandas as pd
from sequence_attributes import (get_fasta_lists, get_additional_sequence_attributes,
                                 return_standard_genetic_code)


def get_cli_args():
    """ Reads in the infile argument to a variable, confirming that it's provided. """
    parser = argparse.ArgumentParser(
        description='Provide a FASTA file to perform splitting on sequence and secondary structure')

    parser.add_argument('--infile_ccds_fasta',
                        dest='INFILE_CCDS_FASTA',
                        type=str,
                        help='The CCDS FASTA file to open',
                        required=True)

    parser.add_argument('--infile_ccds_attributes',
                        dest='INFILE_CCDS_ATTRIBUTES',
                        type=str,
                        help='The CCDS attributes file to open',
                        required=True)

    parser.add_argument('--infile_ensembl_gene',
                        dest='INFILE_ENSEMBL_GENE',
                        type=str,
                        help='The ensembl gene file to open',
                        required=True)

    parser.add_argument('--excel_outfile',
                        dest='EXCEL_OUTFILE',
                        type=str,
                        help='Path to Excel file to write out to',
                        required=True)
    return parser.parse_args()


def main():  # pragma: no cover
    """ Prints statistics about a FASTA file to an output file. """
    # Fetch commandline arguments
    args = get_cli_args()
    infile_ccds_fasta = vars(args)["INFILE_CCDS_FASTA"]
    infile_ccds_attributes = vars(args)["INFILE_CCDS_ATTRIBUTES"]
    infile_ensembl_gene = vars(args)["INFILE_ENSEMBL_GENE"]
    outfile_name = vars(args)["EXCEL_OUTFILE"]

    # Read the Ensembl data into a pandas data frame
    ccds_df = pd.read_csv(infile_ccds_attributes, delimiter='\t')
    ccds_df.rename(columns={'gene_id': 'refseq_gene_id'}, inplace=True)
    ccds_df.rename(columns={'#chromosome': 'chrom'}, inplace=True)

    ensembl_df = pd.read_csv(infile_ensembl_gene, delimiter='\t')
    ensembl_df.rename(columns={'ID': 'ensembl_gene_id'}, inplace=True)
    ensembl_df.rename(columns={'Canonical Transcript': 'ensembl_canonical_transcript_id'},
                      inplace=True)
    ensembl_df.rename(columns={'Gene': 'gene'}, inplace=True)
    ensembl_df.rename(columns={'Description': 'description'}, inplace=True)
    ensembl_df.rename(columns={'Biotype': 'biotype'}, inplace=True)

    # Merge the CCDS and Ensembl data frames
    ccds_attributes_df = pd.merge(ccds_df, ensembl_df, on='gene', how='left')

    # Get the data from the FASTA data file using get_fasta_lists
    headers, seqs = get_fasta_lists(infile_ccds_fasta)

    # Loop over seq_header and sequence data
    all_data = []
    for i, (header, dna_sequence) in enumerate(zip(headers, seqs)):
        all_data.append(
            get_additional_sequence_attributes(
                header=header,
                dna_sequence=dna_sequence,
                genetic_code=return_standard_genetic_code(),
                attribute_df=ccds_attributes_df))
        if i == sys.maxsize:  # remember to update to sys.maxsize before submitting
            break  # sys.maxsize

    # Convert those tuples into a pandas data frame
    all_data_df = pd.DataFrame(all_data)

    # Sort the data frame descending by proline_comp and ascending protein_sequence_len
    all_data_df = all_data_df.sort_values(by=['proline_comp', 'protein_sequence_len'],
                                          ascending=[False, True])

    # Write the data frame to an Excel file
    all_data_df.to_excel(outfile_name, sheet_name="proline_and_pro_seq_len", index=False)

    # Print the top 10 genes by highest proline composition and the last 10 genes by lowest
    column_list = ['ccds', 'refseq_gene_id', 'biotype', 'ensembl_gene_id', 'description',
                   'protein_sequence_len', 'proline_comp']
    ten_highest = all_data_df.nlargest(10, 'proline_comp')
    ten_lowest = all_data_df.nsmallest(10, 'proline_comp')
    ten_highest['nucleotide_comp'] = ten_highest['nucleotide_comp'].astype(str)
    ten_highest['amino_acid_comp'] = ten_highest['amino_acid_comp'].astype(str)
    ten_highest['kmers_comp'] = ten_highest['kmers_comp'].astype(str)
    ten_lowest['nucleotide_comp'] = ten_lowest['nucleotide_comp'].astype(str)
    ten_lowest['amino_acid_comp'] = ten_lowest['amino_acid_comp'].astype(str)
    ten_lowest['kmers_comp'] = ten_lowest['kmers_comp'].astype(str)
    merged_lowest_highest = pd.merge(ten_highest, ten_lowest, how='outer')
    # Sort the data again because merging loses the sort
    merged_lowest_highest = merged_lowest_highest.sort_values(by=['proline_comp',
                                                                  'protein_sequence_len'],
                                                              ascending=[False, True])
    out_filename_tsv = outfile_name.replace(".xlsx", ".tsv")
    merged_lowest_highest.to_csv(out_filename_tsv, sep='\t', index=False, columns=column_list)


if __name__ == '__main__':  # pragma: no cover
    main()
