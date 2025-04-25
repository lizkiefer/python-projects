"""

File:  stats_in_python.py
Author: Liz Kiefer

Given a file name and column index, reads the data from the file at that column,
and provides statistical data about it.
Filters out nonnumeric strings and NaN entries.
"""

import sys

fileName = sys.argv[1]
column_to_parse = sys.argv[2]

numbers = []
INVALID_NUM = 0

# Load numbers list
with open(fileName, 'r', encoding='UTF-8') as infile:
    for i, line in enumerate(infile):
        try:
            num = line.split("\t")[int(column_to_parse)]
        except IndexError:
            print(f"Exiting: There is no valid 'list index' in column {column_to_parse} "
                  f"in line {i + 1} in file: {fileName}")
            sys.exit(1)
        try:
            if num == "NaN":
                INVALID_NUM += 1
            else:
                numbers.append(float(num))
        except ValueError:
            print(f"Skipping line number {i + 1} : could not convert string to float: '{num}'")
            print()
            INVALID_NUM += 1

if len(numbers) == 0:
    print(f"Error: There were no valid number(s) in column {column_to_parse} in file: {fileName}")
    sys.exit(1)

# Calculate length and average
LEN_NUMBERS = len(numbers)
AVG_NUMBERS = sum(numbers) / LEN_NUMBERS

# Calculate variance
varianceCalcs = []
MIN_NUM = 100000
MAX_NUM = -100000
for number in numbers:
    # Calculate max and min
    if number < MIN_NUM:
        MIN_NUM = number
    if number > MAX_NUM:
        MAX_NUM = number
    varianceCalcs.append((number - AVG_NUMBERS) ** 2)
if LEN_NUMBERS == 1:
    VARIANCE = 0
else:
    VARIANCE = (1 / (LEN_NUMBERS - 1) * sum(varianceCalcs))


# Calculate median
numbers.sort()
MEDIAN = 0
MID = LEN_NUMBERS // 2
if LEN_NUMBERS % 2 == 0:
    MEDIAN = (numbers[MID] + (numbers[MID - 1])) / 2
else:
    MEDIAN = numbers[MID]

print(f"{'Column':>10}: {column_to_parse}")
print()
print()
print(f"{'':8}{'Count':10}={INVALID_NUM + LEN_NUMBERS:>10.3f}")
print(f"{'':8}{'ValidNum':10}={LEN_NUMBERS:>10.3f}")
print(f"{'':8}{'Average':10}={AVG_NUMBERS:>10.3f}")
print(f"{'':8}{'Maximum':10}={MAX_NUM:>10.3f}")
print(f"{'':8}{'Minimum':10}={MIN_NUM:>10.3f}")
print(f"{'':8}{'Variance':10}={VARIANCE:>10.3f}")
print(f"{'':8}{'Std dev':10}={VARIANCE ** (1/2):>10.3f}")
print(f"{'':8}{'Median':10}={MEDIAN ** (1/2):>10.3f}")
