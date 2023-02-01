#  File: WordSearch.py

#  Description: This Program searches for words in a square grid of letters

#  Student Name: Abdulateef Oyegbefun

#  Student UT EID: Afo296

#  Partner Name: Jesus Marcos

#  Partner UT EID: Jam27482

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 01/18/2023

#  Date Last Modified: 01/21/2023

import sys


# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    num_of_lines = sys.stdin.readline().strip()
    num_of_lines = int(num_of_lines)
    word_grid =[]

    newline = sys.stdin.readline().strip()
    for i in range(num_of_lines):
        grid_row = sys.stdin.readline().strip()
        as_list=grid_row.split(sep=' ')
        word_grid.append(as_list)

    newline = sys.stdin.readline()
    
    num_of_words = sys.stdin.readline().strip()
    num_of_words = int(num_of_words)
    word_list = []

    for i in range(num_of_words):
        word = sys.stdin.readline().strip()
        word_list.append(word)
        


    return word_grid,word_list


# Creating Lists of letters for which to search the words in the word list
def horizontal_list_forwards_backwards(word_grid):
    horizontal_forwards=[]
    length_of_grid = len(word_grid)
    for i in range(length_of_grid):
      string=''
      for j in range(length_of_grid):
        #print(f'{i},{j}  ')
        #print(f'{word_grid[i][j]}',end='')
        string=string+word_grid[i][j]
        #horizontal_forwards.append(word_grid[i][j])
      #print()
      horizontal_forwards.append(string)
    #print(horizontal_forwards)
    # Listing the list of words backwards
    horizontal_backwards=[]
    for horizontal in horizontal_forwards:
      string=horizontal[::-1]
      horizontal_backwards.append(string)
    #print(horizontal_backwards)
    #horizontal_list=horizontal_forwards+horizontal_backwards
    #print(horizontal_list)
    return horizontal_forwards , horizontal_backwards


def vertical_list_forwards_backwards(word_grid):
    vertical_forwards=[]
    length_of_grid = len(word_grid)
    for i in range(length_of_grid):
      string=''
      for j in range(length_of_grid):
        #print(f'{i},{j}  ')
        #print(f'{word_grid[i][j]}',end='')
        string=string+word_grid[j][i]
        #horizontal_forwards.append(word_grid[i][j])
      #print()
      vertical_forwards.append(string)
    #print(horizontal_forwards)
    # Listing the list of words backwards
    vertical_backwards=[]
    for vertical in vertical_forwards:
      string=vertical[::-1]
      vertical_backwards.append(string)
    #print(horizontal_backwards)
    #horizontal_list=vertical_forwards+horizontal_backwards
    #print(horizontal_list)
    return vertical_forwards, vertical_backwards


def diagonal_list_bottom_left(word_grid):
  length_of_grid = len(word_grid)
  diagonal_forward = []

  for k in range(length_of_grid):
    string=''
    for i in range(length_of_grid - k):
      for j in range(length_of_grid - k):
        if i==j:
          #print(f'{i + k},{j}')
          string=string+word_grid[i+k][j]
    diagonal_forward.append(string)
    #print()
  #print(diagonal_forward)

  diagonal_backwards=[]
  for diagonal in diagonal_forward:
    string=diagonal[::-1]
    diagonal_backwards.append(string)
  #print(diagonal_backwards)

  return diagonal_forward,diagonal_backwards


def diagonal_list_upper_right(word_grid):
  length_of_grid = len(word_grid)
  diagonal_forward = []

  for k in range(length_of_grid):
    string=''
    for i in range(length_of_grid - k):
      for j in range(length_of_grid - k):
        if i==j:
          #print(f'{i},{j+k}')
          string=string+word_grid[i][j+k]
    diagonal_forward.append(string)
    #print()
  #print(diagonal_forward)

  diagonal_backwards=[]
  for diagonal in diagonal_forward:
    string=diagonal[::-1]
    diagonal_backwards.append(string)
  #print(diagonal_backwards)

  return diagonal_forward, diagonal_backwards


def diagonal_list_upper_left(word_grid):
  length_of_grid = len(word_grid)
  diagonal_forward = []

  for k in range(length_of_grid):
    string=''
    #print(k)
    #print()
    for i in range(length_of_grid - k):
      for j in range(length_of_grid - k,0,-1):
        if (i+j-1)==length_of_grid-1-k:
          #print(f'{i},{j-1}')
          string=string+word_grid[i][j-1]
    diagonal_forward.append(string)
    #print()
  #print(diagonal_forward)

  diagonal_backwards=[]
  for diagonal in diagonal_forward:
    string=diagonal[::-1]
    diagonal_backwards.append(string)
  #print(diagonal_backwards)

  return diagonal_forward, diagonal_backwards


def diagonal_list_bottom_right(word_grid):
  length_of_grid = len(word_grid)
  diagonal_forward = []

  for k in range(length_of_grid):
    string=''
    #print(k)
    #print()
    for i in range(k,length_of_grid):
      for j in range(length_of_grid,k,-1):
        if (i+j-1)==length_of_grid-1+k:
          #print(f'{i},{j-1}')
          string=string+word_grid[i][j-1]
    diagonal_forward.append(string)
    #print()
  #print(diagonal_forward)

  diagonal_backwards=[]
  for diagonal in diagonal_forward:
    string=diagonal[::-1]
    diagonal_backwards.append(string)
  #print(diagonal_backwards)

  return diagonal_forward, diagonal_backwards

# We have finished Creating the Lists of letters for which to search the words in the word list


def what_list_is_the_word_in_gen(list_from_grid_dict, word,word_grid):
  initial_length_of_list = len(word_grid)
  #print(f'{horizontal_forwards}')
  location=(0,0)
  for j in list_from_grid_dict:
    for i in j:
        string_position=i.find(word)
        list_position = j.index(i)

        if (string_position!=-1):
          #print(f'{word}, \n\n{j},\n\n{list_position},\n\n{i}, \n\n{string_position}\n\n\n\n')
          location=list_from_grid_dict[j](word, list_position, string_position, initial_length_of_list)
  #print(len(word_grid))
  return location


#---------------------HORIZONTAL------------The below will be made to only find positions of words---------------------
def finding_words_horizontal_forwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  x=list_position+1
  y=string_position+1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-horizontal_forward')
    return x,y

def finding_words_horizontal_backwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  x=list_position+1
  y=(( initial_length_of_list - 1) - string_position ) + 1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-horizontal_backward')
    return x,y
#--------------------------------VERTICAL---------------------------------------------------------
def finding_words_vertical_forwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  x=string_position+1
  y=list_position+1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-vertical_forward')
    return x,y

def finding_words_vertical_backwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  x=(( initial_length_of_list - 1) - string_position ) + 1
  y=list_position+1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-vertical_backward')
    return x,y
#-----------------------------------diagonal_bottom_left-------------------------------------
def finding_diagonal_bottom_left_forwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  x=string_position + list_position + 1
  y=string_position + 1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-diagonal_bottom_left_forwards')
    return x,y

def finding_diagonal_bottom_left_backwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  current_length_list = initial_length_of_list - list_position
  string_position_new = (current_length_list - 1) - string_position
  x=string_position_new + list_position + 1
  y=string_position_new + 1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-diagonal_bottom_left_backwards')
    return x,y    
#-----------------------------------diagonal_upper_left_-------------------------------------
def finding_diagonal_upper_left_forwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  x=string_position + 1
  y=((initial_length_of_list - 1) - string_position - list_position ) + 1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-diagonal_upper_left_forwards')
    return x,y

def finding_diagonal_upper_left_backwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  current_length_list = initial_length_of_list - list_position
  string_position_new = (current_length_list - 1) - string_position
  x=string_position_new + 1
  y=((initial_length_of_list - 1) - string_position_new - list_position ) + 1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-diagonal_upper_left_backwards')
    return x,y

#-----------------------------------diagonal_bottom_right_-------------------------------------
def finding_diagonal_bottom_right_forwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  x=string_position + list_position + 1
  y=((initial_length_of_list - 1) - string_position ) + 1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-diagonal_bottom_right_forwards')
    return x,y

def finding_diagonal_bottom_right_backwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  current_length_list = initial_length_of_list - list_position
  string_position_new = (current_length_list - 1) - string_position
  x=string_position_new + list_position + 1
  y=((initial_length_of_list - 1) - string_position_new ) + 1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-diagonal_bottom_right_backwards')
    return x,y

#-----------------------------------diagonal_upper_right_-------------------------------------
def finding_diagonal_upper_right_forwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  x=string_position + 1
  y=string_position + list_position + 1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-diagonal_upper_right_forwards')
    return x,y

def finding_diagonal_upper_right_backwards(word, list_position, string_position, initial_length_of_list):
  initial_length_of_list = initial_length_of_list
  current_length_list = initial_length_of_list - list_position
  string_position_new = (current_length_list - 1) - string_position
  x=string_position_new + 1
  y=string_position_new + list_position + 1
  if (string_position!=-1):
    #print(f'x: {x},\ty:{y},\t{word}\t-diagonal_upper_right_backwards')
    return x,y



def grid_dict(word_grid):
  horizontal_forwards, horizontal_backwards =horizontal_list_forwards_backwards(word_grid)
  vertical_forwards, vertical_backwards=vertical_list_forwards_backwards(word_grid)
  diagonal_forward_bl,diagonal_backwards_bl=diagonal_list_bottom_left(word_grid)
  diagonal_forward_ul,diagonal_backwards_ul=diagonal_list_upper_left(word_grid)
  diagonal_forward_br,diagonal_backwards_br=diagonal_list_bottom_right(word_grid)
  diagonal_forward_ur,diagonal_backwards_ur=diagonal_list_upper_right(word_grid)

  list_from_grid_dict={
    tuple(horizontal_forwards):finding_words_horizontal_forwards,
    tuple(horizontal_backwards):finding_words_horizontal_backwards,
    tuple(vertical_forwards):finding_words_vertical_forwards,
    tuple(vertical_backwards):finding_words_vertical_backwards,
    tuple(diagonal_forward_bl):finding_diagonal_bottom_left_forwards,
    tuple(diagonal_backwards_bl):finding_diagonal_bottom_left_backwards,
    tuple(diagonal_forward_ul):finding_diagonal_upper_left_forwards,
    tuple(diagonal_backwards_ul):finding_diagonal_upper_left_backwards,
    tuple(diagonal_forward_br):finding_diagonal_bottom_right_forwards,
    tuple(diagonal_backwards_br):finding_diagonal_bottom_right_backwards,
    tuple(diagonal_forward_ur):finding_diagonal_upper_right_forwards,
    tuple(diagonal_backwards_ur):finding_diagonal_upper_right_backwards,

    }
  return list_from_grid_dict

def find_word(grid,word):
  word_grid = grid
  list_from_grid_dict=grid_dict(word_grid)
  location = what_list_is_the_word_in_gen(list_from_grid_dict, word,word_grid)
 
  return location




def main():
  # read the input file from stdin
  word_grid, word_list = read_input()


  # find each word and print its location
  for word in word_list:
    location = find_word (word_grid, word)
    print (word + ": " + str(location))


if __name__ == "__main__":
  main()