The data will the in format

1 1 1 0 0 0 
0 1 0 0 0 0 
1 1 1 0 0 0
0 0 0 2 3 4 
0 0 0 0 9 0 
0 0 0 2 7 8 

This is an example, the arrays will be of different sizes and values
Here the data is taken in the format

1 1 1         2 3 4
  1             9
1 1 1    or   2 7 8

sum = 1 + 1 + 1 + 1 + 1 + 1
or sum = 2 + 3 + 4 + 9 + 2 + 7 + 8
So we take sum of these and return the one with the maximum summation value
I stored the data in a nested list format
Initially i took two loops, one for the rows and the other for the elements in the rows
Then took elements in the above format and summed them. Later i just choose the maxvalue and output that.
