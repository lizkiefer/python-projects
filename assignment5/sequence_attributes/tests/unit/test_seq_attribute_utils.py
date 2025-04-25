"""
File:  test_assignment4_utils.py
Author: Liz Kiefer

Contains unit tests for assignment4_utils.py
"""

import pandas as pd
from sequence_attributes import (lookup_by_ccds, get_tm_from_dna_sequence,
                                 get_additional_sequence_attributes, calculate_amino_acid_content,
                                 extract_kmers, get_sequence_composition,
                                 return_standard_genetic_code, protein_translation, gc_content)


test_df = pd.DataFrame.from_dict(
    {"chrom": {"0": "1", "1": "1"}, "nc_accession": {"0": "NC_000001.8", "1": "NC_000001.11"},
     "gene": {"0": "LINC00115", "1": "SAMD11"}, "refseq_gene_id": {"0": 79854, "1": 148398},
     "ccds_id": {"0": "CCDS1.1", "1": "CCDS2.2"}, "ccds_status": {"0": "Withdrawn", "1": "Public"},
     "cds_strand": {"0": "-", "1": "+"}, "cds_from": {"0": "801942", "1": "925941"},
     "cds_to": {"0": "802433", "1": "944152"}, "cds_locations": {"0": "[801942-802433]",
                                                                 "1": "[925941-926012, "
                                                                      "930154-930335]"},
     "match_type": {"0": "Identical", "1": "Identical"},
     "Assembly Name": {"0": "GRCh38", "1": "GRCh38"},
     "biotype": {"0": "lncRNA", "1": "protein_coding"},
     "ensembl_canonical_transcript_id": {"0": "ENST00000473798.2", "1": "ENST00000616016.5"},
     "DB Type": {"0": "core", "1": "core"}, "description": {
        "0": "long intergenic non-protein coding RNA 115 [Source:HGNC Symbol;Acc:HGNC:26211]",
        "1": "sterile alpha motif domain containing 11 [Source:HGNC Symbol;Acc:HGNC:28706]"},
     "Display Name": {"0": "LINC00115", "1": "SAMD11"}, "End": {"0": 827539, "1": 944575},
     "ensembl_gene_id": {"0": "ENSG00000225880", "1": "ENSG00000187634"},
     "Logic Name": {"0": "havana_homo_sapiens", "1": "ensembl_havana_gene_homo_sapiens"},
     "Object Type": {"0": "Gene", "1": "Gene"}, "Seq Region Name": {"0": "1", "1": "1"},
     "Source": {"0": "havana", "1": "ensembl_havana"},
     "Species": {"0": "homo_sapiens", "1": "homo_sapiens"}, "Start": {"0": 824228, "1": 923923},
     "Strand": {"0": -1, "1": 1}, "Version": {"0": 6, "1": 13}})


def test__gc_content():
    """Tests gc_content working normally"""
    sequence = "AACCGGTT"
    gc_content_val = gc_content(sequence, percentage=False)
    assert gc_content_val == 0.5, f"GC content {gc_content_val} is not a float value of 0.5"


def test__gc_content_percent():
    """Tests gc_content working normally to return a percent"""
    sequence = "AACCGGTT"
    gc_content_val = gc_content(sequence, round_to=1, percentage=True)
    assert gc_content_val == 50.0, f"GC content {gc_content_val} is not a percent value of 50.0"


def test__lookup_by_ccds():
    """Tests lookup_by_ccds working normally"""
    lookup = lookup_by_ccds('CCDS1.1', '1', test_df)
    assert len(lookup) == 1, "Data frame for is not length of 1"


def test__get_tm_from_dna_sequence():
    """Tests get_tm_from_dna_sequence working normally"""
    dna = 'AGCT'
    assert get_tm_from_dna_sequence(dna) == 8.9, \
        f"TM of {dna} is not 8.9"


def test__get_sequence_composition():
    """Tests get_sequence_composition working normally"""
    assert (get_sequence_composition('ATGCGA') == {'A': 2, 'T': 1, 'G': 2, 'C': 1})


def test__calculate_amino_acid_content():
    """Tests calculate_amino_acid_content working normally"""
    assert calculate_amino_acid_content('P', 'APPPAP') == 66.67


def test__extract_kmers():
    """Tests extract_kmers working normally"""
    assert (extract_kmers('ATGCGA', 3) ==
            ['ATG', 'TGC', 'GCG', 'CGA'])


def test__protein_translation():
    """Tests return_standard_genetic_code working normally"""
    genetic_code = return_standard_genetic_code()

    assert protein_translation(
        'ATGTCCAAGGGGATCCTGCAGGTGCATCCTCCGATCTGCGACTGCCCGGGCTGCCGAATA',
        genetic_code) == 'MSKGILQVHPPICDCPGCRI'


def test__get_additional_sequence_attributes():
    """Tests get_additional_sequence_attributes working normally"""
    header = ">CCDS2.2|Hs110|chr1"
    dna_sequence = ("TGTCCAAGGGGATCCTGCAGGTGCATCCTCCGATCTGCGACTGCCCGGGCTGCCGAATATCCTCCCCGGTGAACCG"
                    "GGGGCGGCTGGCAGACAAGAGGACAGTCGCCCTGCCTGCCGCCCGGAACCTGAAGA")
    attributes = get_additional_sequence_attributes(
        header=header,
        dna_sequence=dna_sequence,
        genetic_code=return_standard_genetic_code(),
        attribute_df=test_df)
    assert all(attributes)
