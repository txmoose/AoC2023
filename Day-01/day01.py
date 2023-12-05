#!/usr/bin/env python3
"""
Solution to Day 1, star 1 of
Advent of Code 2023

read each line left to right, stop and capture first numeral
reach each line right to left, stop and capture first numeral
append 2 numerals together
cast to int
append to list
sum list
"""

def find_numeral(line: str) -> str:
    for i in line:
        if i.isnumeric():
            return i
        
if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
    
    sums = []
    for line in lines:
        holding = []
        input = line.strip()
        holding.append(find_numeral(input))
        input = reversed(line.strip())
        holding.append(find_numeral(input))
        sums.append(int(holding[0] + holding[1]))

    print(sum(sums))