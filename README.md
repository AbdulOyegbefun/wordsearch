# Word Search
Given an n by n grid of letters, and a list of words, this program finds the location in the grid where the word can be found. A word matches a straight, contiguous line of letters in the grid. The match could either be done horizontally (left or right) or vertically (up or down) or along any diagonal either right to left or from left to right.

## This project is run on the command line:

On Mac or Linux:
- python3 WordSearch.py < word_grid.in

On Windows:
- python WordSearch.py < word_grid.in

## Input: 
The input will be in a file word_grid.in and will be read from stdin. Other files can be used as input but must be in the form of word_grid.in. The format of the input file is as follows:

- First line will have one integer - n, the number of lines in the grid and the number of characters in each line.
- There will be a single blank line.
- There will be n lines, where each line will have n characters, all in upper case, separated by a space.
- There will be a single blank line.
- There will be a single integer k, denoting the number of words that follow.
- There will be k lines. Each line will contain a single word in all uppercase.

## Output: 
There will be k lines in your output. Each line will have the word that you are to search, followed by a colon, followed by a single space and then the tuple giving the row and column where you found the word. In the tuple you will have two integers (i, j). The number i gives the row and the number j the column of the first letter of the word to be found. Rows and columns are numbered conventionally, i.e. the first row is 1 and the first column is 1. If the word is not present in the grid then the values for i and j will be 0 and 0. This is the output for the given input file.
