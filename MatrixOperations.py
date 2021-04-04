
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




test_multiplication()

