# Project Title

Assignment 3

## Description

Two script for Assignment 3 
First script named secondary_structure_splitter.py: Given a file name, reads it as a FASTA-formatted file and splits it into sequence and secondary structures, printing each to a separate file. Second script
named nt_fasta_stats.py: Given a file name, reads it as a FASTA-formatted file and prints statistics to an output file
about the sequences present in the file.
## Getting Started

### Dependencies

* Python3

### Installing

* Run the script in place after unzipping

### Executing program

secondary_structure_splitter.py:
* Run the script with Python3. One argument is required:
The path to a FASTA-formatted data file
```
python3 secondary_structure_splitter.py --infile/-i ss.txt
```

nt_fasta_stats.py: 
* Run the script with Python3. Two arguments are required:
The path to a FASTA-formatted data file
The path to an output file
```
python3 nt_fasta_stats.py --infile/-i influenza.fasta --outfile/-i out.txt
```

## Authors

Liz Kiefer

## Version History

* 1.0 Release

## License

This project is not licensed.

## Acknowledgments
.