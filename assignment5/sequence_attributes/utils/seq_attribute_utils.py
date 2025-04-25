"""
File:  seq_attribute_utils.py
Author: Liz Kiefer

Contains utility functions for processing sequences
"""

from collections import namedtuple
from typing import Union
import pandas as pd


def gc_content(sequence: Union[str, list, tuple], round_to: int = 2, percentage: bool = True):
    """Returns the percentage of a sequence consisting of G or C
    Has options for how many decimals to round to and if a percentage should be returned"""
    nucleotide_c = sequence.count('C')
    nucleotide_g = sequence.count('G')
    sequence_length = len(sequence)
    if percentage:
        return_val = ((nucleotide_c + nucleotide_g) / sequence_length) * 100
    else:
        return_val = (nucleotide_c + nucleotide_g) / sequence_length
    return round(return_val, round_to)


def lookup_by_ccds(ccds_id: str, chrom: str, df: pd.DataFrame):
    """ This function takes in two arguments ccds_id and chrom, and returns a dataframe that where
    the 'ccds_id' column matches a specified 'ccds_id' value and the 'chrom' column matches a
    specified 'chrom' value"""
    return df[(df['ccds_id'] == ccds_id) & (df['chrom'] == chrom)]


def get_tm_from_dna_sequence(sequence: Union[str, list, tuple], round_to: int = 2):
    """ Returns the melting temperature for a sequence based on the nearest-neighbor model """
    tm_parameters = {
        "AA": 2.3,
        "AT": 2.0,
        "TA": 2.0,
        "TT": 2.3,
        "CG": 3.0,
        "GC": 3.1,
        "GA": 3.1,
        "GG": 3.3,
        "CT": 3.3,
        "TC": 3.3,
        "AC": 2.4,
        "CA": 2.4,
        "GT": 3.4,
        "TG": 3.4,
        "AG": 2.5,
        "CC": 4.0
    }
    return round(sum(tm_parameters[sequence[i:i + 2]] for i in range(len(sequence) - 1)), round_to)


def get_sequence_composition(sequence: Union[str, list, tuple]):
    """
    Returns a dictionary of the numbers of occurrences of each unique entry in the input
    """
    return_dict = {}
    for i in sequence:
        if i not in return_dict:
            return_dict[i] = 1
        else:
            return_dict[i] += 1
    return return_dict


def calculate_amino_acid_content(amino_acid: str, sequence: Union[str, list, tuple],
                                 round_to: int = 2, percentage: bool = True):
    """
    Calculates the percentage of a given sequence that consists of the given amino acid
    Can specify the rounding and if the return should be a percentage or not
    """
    amino_count = sequence.count(amino_acid)
    sequence_length = len(sequence)

    if percentage:
        return_val = (amino_count / sequence_length) * 100
    else:
        return_val = amino_count / sequence_length
    return round(return_val, round_to)


def extract_kmers(sequence: Union[str, list, tuple], kmer_size: int = 3):
    """
    Returns a list of kmers from the given sequence, with size based on kmer_size
    """
    kmers_list = []
    for i in range(0, len(sequence) - kmer_size + 1):
        kmers_list.append(sequence[i:i + kmer_size])
    return kmers_list


def return_standard_genetic_code():
    """
    Returns a dictionary for the standard genetic code
    """
    return {
        "UUU": "F", "UUC": "F", "UCU": "S", "UCC": "S", "UAU": "Y", "UAC": "Y",
        "UGU": "C", "UGC": "C", "UUA": "L", "UCA": "S", "UAA": None, "UGA": None,
        "UUG": "L", "UCG": "S", "UAG": None, "UGG": "W", "CUU": "L", "CUC": "L",
        "CCU": "P", "CCC": "P", "CAU": "H", "CAC": "H", "CGU": "R", "CGC": "R",
        "CUA": "L", "CUG": "L", "CCA": "P", "CCG": "P", "CAA": "Q", "CAG": "Q",
        "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "ACU": "T", "ACC": "T",
        "AAU": "N", "AAC": "N", "AGU": "S", "AGC": "S", "AUA": "I", "ACA": "T",
        "AAA": "K", "AGA": "R", "AUG": "M", "ACG": "T", "AAG": "K", "AGG": "R",
        "GUU": "V", "GUC": "V", "GCU": "A", "GCC": "A", "GAU": "D", "GAC": "D",
        "GGU": "G", "GGC": "G", "GUA": "V", "GUG": "V", "GCA": "A", "GCG": "A",
        "GAA": "E", "GAG": "E", "GGA": "G", "GGG": "G"
    }


def protein_translation(sequence: Union[str, list, tuple], genetic_code: dict):
    """
    Converts a DNA sequence into a protein sequence using the inputted genetic code dictionary
    """
    protein_sequence = ''
    for i in range(0, len(sequence), 3):
        current_sequence = sequence[i:i + 3].replace('T', 'U')
        if len(current_sequence) == 3:
            current_protein_sequence = genetic_code[current_sequence]
            if not current_protein_sequence:
                break
            protein_sequence += current_protein_sequence
    return protein_sequence


def get_additional_sequence_attributes(header: str = None,
                                       dna_sequence: str = None,
                                       genetic_code: dict = None,
                                       attribute_df: pd.DataFrame = None) -> namedtuple:
    """
    Get the additional attributes for the Header and DNA sequence passed in
    @param header: FASTA header
    @param dna_sequence: FASTA sequence
    @param genetic_code: dictionary where key = codon and key = amino acid
    @param attribute_df: The attribute data frame (gene level information)
    @return: namedtuple
    """

    ccds_id, _, chrom = header.split("|")
    ccds_id = ccds_id.lstrip('>')
    chrom = chrom.replace('chr', '')
    ccds_entry_df = lookup_by_ccds(ccds_id=ccds_id, chrom=chrom, df=attribute_df)
    assert len(ccds_entry_df) == 1, f"Data frame for ccds {ccds_id} is not length of 1"

    # Define the attributes for the named tuple
    ccds_attributes_to_get = ['nc_accession', 'gene', 'refseq_gene_id', 'biotype',
                              'ensembl_gene_id', 'ensembl_canonical_transcript_id', 'description']
    tuple_fields = (['ccds', 'chrom', 'header', 'dna_sequence', 'dna_sequence_len',
                     'protein_sequence', 'protein_sequence_len', 'nucleotide_comp',
                     'amino_acid_comp', 'kmers_comp', 'proline_comp', 'tm', 'gc'] +
                    ccds_attributes_to_get)

    # Create the named tuple type
    FastaTuple = namedtuple("FastaTuple", tuple_fields)

    # 1. Extract 3-mers from the DNA sequence
    kmers = extract_kmers(dna_sequence, 3)

    # 2. Translate the DNA sequence to a protein sequence
    protein_sequence = protein_translation(dna_sequence, genetic_code)
    # 3. Get the TM of the DNA sequence
    tm_val = get_tm_from_dna_sequence(dna_sequence)

    # 4. Compute compositions for nt, amino acids, and kmers
    nucleotide_comp = get_sequence_composition(dna_sequence)
    amino_acid_comp = get_sequence_composition(protein_sequence)
    kmers_comp = kmers
    # 5. Get GC content
    gc_val = gc_content(dna_sequence)  # pylint: disable=invalid-name
    # 6. get CCDS attributes from the DF
    ccds_attributes = [ccds_entry_df[val].iloc[0] for val in ccds_attributes_to_get]
    # 7. find proline composition
    proline_comp = calculate_amino_acid_content('P', protein_sequence)

    # Instantiate and return the named tuple
    return FastaTuple(ccds_id, chrom, header, dna_sequence, len(dna_sequence), protein_sequence,
                      len(protein_sequence), nucleotide_comp, amino_acid_comp, kmers_comp,
                      proline_comp, tm_val, gc_val, *ccds_attributes)
