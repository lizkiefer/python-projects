# Project Title

Assignment 5

## Description

Scripts for assignment 5
This module named sequence_attributes reads in gene and attributes data and produces two output file. The first is an Excel spreadsheet of the gene data.
The second output file is a TSV of the top and bottom 10 genes, sorted by proline_comp.
## Getting Started

### Dependencies

* Python3

### Installing

* Run the script in place after unzipping

### Executing program

main.py: 
* Run the script with Python3, calling the sequence_attributes.main module. Four arguments are required:
The path to a FASTA-formatted data file
The path to a CCDS attributes data file
The path to an ensembl gene data file
The path to an output file ending in .xlsx
```
python3 -m sequence_attributes.main 
    --infile_ccds_fasta sequence_attributes/inputs/CCDS_nucleotide.current.fna \
    --infile_ccds_attributes sequence_attributes/inputs/CCDS.current.txt 
    --infile_ensembl_gene sequence_attributes/inputs/ensembl_gene_data.tsv \
    --excel_outfile sequence_attributes.xlsx
```

## Authors

Liz Kiefer

## Version History

* 1.0 Release

## License

This project is not licensed.

## Acknowledgments
.