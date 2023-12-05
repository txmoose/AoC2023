#!/usr/bin/env python3
"""
Solution to Day 1, star 2 of
Advent of Code 2023

read each line left to right
if character is a numeral, capture and exit
if character is a letter, decide if that letter is 
  the beginning of a number spelled out
  if it is, capture that numeral and exit
  if not, go on to the next character
do the same process but backwards from right to left

append 2 numerals together
cast to int
append to list
sum list
"""

def find_numeral(line: str) -> int:
    numerals = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for i in range(len(line)):
        holding = []
        if line[i].isnumeric():
            holding.append(str(line[i]))
            break
        else:
            for numeral in numerals.keys():
                if "".join(line[i:]).startswith(numeral):
                    holding.append(numerals[numeral])
                    break

            if len(holding) == 1:
                break
            else:
                continue

    len_line = len(line) - 1
    for i in range(len_line):
        if line[len_line - i].isnumeric():
            holding.append(str(line[len_line - i]))
            break
        else:
            for numeral in numerals.keys():
                print(line[:len_line+1-i])
                line = "".join(line[:len_line+1-i])
                if line.endswith(numeral):
                    holding.append(numerals[numeral])
                    break
            if len(holding) == 2:
                break
            else:
                continue

    if len(holding) == 1:
        number = str(holding[0] + holding[0])
    else:
        number = str(holding[0] + holding[1])
    print(f'Number => {number}')
    return int(number)
        
if __name__ == "__main__":
    with open("Day-01/input.txt", "r") as f:
        lines = f.readlines()
    
    sum = 0
    for line in lines:
        input = line.strip()
        sum += find_numeral(input)

    print(sum)

