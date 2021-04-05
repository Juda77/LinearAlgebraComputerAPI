import math
#**************MATRIX MULTIPLCATION START***************************

#function which multiplies a matrix by a scalar
def matrix_multiply_scalar(scalar : int, matrix : list):
  product = []

  for row in range(len(matrix)):
    product_row = []

    for col in range(len(matrix[0])):
      product_row.append(matrix[row][col] * scalar)

    product.append(product_row)

  return product

#function which multiplies two matrices together
def matrix_multiply(matrix_a, matrix_b):
  #first, verify that it's possible to multiply the two matrices together

  #example matrix: [[1,2],[3,4],[5,6]]

  col_count_a = len(matrix_a[0])
  row_count_b = len(matrix_b)

  if (col_count_a != row_count_b):
    return "This matrix product cannot be computed"

  AB = [] #final matrix

  for a_row in range(len(matrix_a)):

    curr_ab_row = []

    #loop through each column in B
    for b_col in range(len(matrix_b[0])):

      new_element = 0
      #loop through each column element in B
      for b_index_in_col in range(len(matrix_b)):

        new_element += matrix_a[a_row][b_index_in_col] * matrix_b[b_index_in_col][b_col]
      curr_ab_row.append(new_element)

    AB.append(curr_ab_row)

  return AB

def test_multiplication():
  test_cases_a = [

    [[2,0,-1],[4,-5,2]],
    [[-1,2],[5,4],[2,-3]],
    [[1,2],[-2,1]]

  ]

  test_cases_b = [

    [[3,5],[-1,4]],
    [[3,-2],[-2,1]],
    [[3,5],[-1,4]],

  ]

  for i in range(len(test_cases_a)):

    print(matrix_multiply(test_cases_a[i], test_cases_b[i]))

#**************MATRIX MULTIPLCATION END***************************

#**************DETERMINANT START***************************
def compute_determinant(matrix):

  determinant = 0
  if (len(matrix) == 2 and len(matrix[0]) == 2):
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    return determinant

  for top_row_index in range(len(matrix[0])):#loop through top row elements
    num = matrix[0][top_row_index] * int(math.pow(-1, top_row_index))

    if (num == 0): #don't bother recursing, since coefficient is zero
      continue

    sub_matrix = []

    for row in range(1, len(matrix)):#loop through every row(except the top)
      sub_matrix_row = []

      for col in range(len(matrix[0])):#loop through each element(column) in the row
        if (col != top_row_index):
          sub_matrix_row.append(matrix[row][col])

      sub_matrix.append(sub_matrix_row)
    #print(sub_matrix)
    determinant += num * compute_determinant(sub_matrix)

  return determinant

def test_compute_determinant():

  test_cases = [

    [ [3,0,4], [2,3,2], [0,5,-1]    ],
    [  [2,-2,3],  [3,1,2],  [1,3,-1]  ],
    [   [4,0,0,5],  [1,7,2,-5], [3,0,0,0],  [8,3,1,7]   ],
    [  [4,0,-7,3,-5], [0,0,2,0,0],  [7,3,-6,4,-8],  [5,0,5,2,-3], [0,0,9,-1,2]      ]

  ]

  for i in range(len(test_cases)):
    print(compute_determinant(test_cases[i]))

#**************MATRIX ADDITION START***************************
def add_matrices(matrix_a, matrix_b):
  if (len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0])):
    return "Cannot add these matrices together"

  sum_matrix = []

  for row in range(len(matrix_a)):
    sum_matrix_curr_row = []
    for col in range(len(matrix_a[0])):
      sum_matrix_curr_row.append(matrix_a[row][col] + matrix_b[row][col])
    sum_matrix.append(sum_matrix_curr_row)

  return sum_matrix


def transpose_matrix(matrix):

  transposed_matrix = []

  for element in range(len(matrix[0])):
    transposed_matrix_row = []
    transposed_matrix_row.append(matrix[0][element])
    transposed_matrix.append(transposed_matrix_row)

  for row in range(1, len(matrix)):

    for col in range(len(matrix[0])):
      transposed_matrix[col].append(matrix[row][col])



  return transposed_matrix


def test_transpose_matrix():
  test_cases = [

    [ [-5,2], [1,-3], [0,4]  ],
    [  [1,1,1,1], [-3,5,-2,7]   ]

  ]

  for i in range(len(test_cases)):
    print(transpose_matrix(test_cases[i]))

test_transpose_matrix()