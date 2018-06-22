"""
Example

For
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9.

Here's the rooms matrix with unsuitable rooms marked with 'x':

[[x, 1, 1, 2],
 [x, 5, x, x],
 [x, x, x, x]]
Thus, the answer is 1 + 5 + 1 + 2 = 9.

For
matrix = [[1, 1, 1, 0],
          [0, 5, 0, 1],
          [2, 1, 3, 10]]
the output should be
matrixElementsSum(matrix) = 9.

Here's the rooms matrix with unsuitable rooms marked with 'x':

[[1, 1, 1, x],
 [x, 5, x, x],
 [x, 1, x, x]]
Note that the free room in the first row make the full column unsuitable for bots.

Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

A 2-dimensional array of integers representing a rectangular matrix of the building.

Guaranteed constraints:
1 ≤ matrix.length ≤ 5,
1 ≤ matrix[i].length ≤ 5,
0 ≤ matrix[i][j] ≤ 10.

[output] integer

The total price of all the rooms that are suitable for the CodeBots to live in
"""
# 9
matrix = [[1,1,1,0],
          [0,5,0,1],
          [2,1,3,10]]
haunted_room_index = []
for arr in matrix:

    for num in arr:
        if num == 0:
            haunted_room_index.append(arr.index(num))
            arr[arr.index(num)] = 'x'
    for index in haunted_room_index:
        arr[index] = 'x'
print(matrix)
num_list = []
for arr in matrix:
    for num in arr:
        if type(num) is int:
            num_list.append(num)
print(num_list)
print(sum(num_list))