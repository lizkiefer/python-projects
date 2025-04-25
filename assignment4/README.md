# Project Title

Assignment 4

## Description

Provides 3 different ways to analyze gene files.

### Dependencies

* Python3 

### Installing

* Run the script in place after unzipping

### Executing program

gene_names_from_chr21.py:
* Run the script with Python3. One argument is optional:
The path to a gene data file
```
python3 gene_names_from_chr21.py
```
The program will ask for the name of a gene. If the gene is found in the data file, the description for the gene will be found.
The program can be exited by typing "quit" and pressing enter when prompted.

find_common_cats.py:
* Run the script with Python3. Two arguments are optional:
The path to a gene data file
The path to a gene category data file
```
python3 find_common_cats.py
```
The program will print the counts of genes per category in the console.

intersection_of_gene_names.py:
* Run the script with Python3. two arguments are optional:
The path to the first gene data file
The path to the second gene data file
```
python3 intersection_of_gene_names.py
```
The program will print which genes are unique the file, which genes are unique to the second file, and which genes are shared between the files.
The genes shared between the files will be printed to an output file at "OUTPUT/intersection_output.txt". 

## Authors

Liz Kiefer

## Version History

* 1.0 Release

## License

This project is not licensed.

## Acknowledgments
.