import math

class matrix_operations:

  #compute the projection of a onto b
  #formula: [(a dot b) / (b dot b)] * a
  #a vector, x, has the form x = [x1, x2, x3,..., xn]
  @staticmethod
  def compute_projection(a, b):

    a_dot_b = 0
    b_dot_b = 0
    for i in range(len(a)):
      a_dot_b += a[i] * b[i]
      b_dot_b += b[i] * b[i]

    scalar = a_dot_b / b_dot_b

    projection = []
    for i in range(len(a)):
      projection.append(scalar * b[i])

    return projection

  #input is a subspace(list of vectors)
  #output the orthonormal basis for that subspace
  #a vector, x, has the form x = [x1, x2, x3,..., xn]
  #begin with span x(input), output span v
  @staticmethod
  def gram_schmidt_process(subspace):

    v = [subspace[0]]

    for i in range(1, len(subspace)):

      x_vector = subspace[i]
      orthogonal_subspace = [0] * len(x_vector)

      for j in range(len(v)):
        subspace_component = matrix_operations.compute_projection(x_vector, v[j])

        for k in range(len(orthogonal_subspace)):
          orthogonal_subspace[k] = orthogonal_subspace[k] + subspace_component[k]


      new_v_component = []
      for x in range(len(x_vector)):
        new_v_component.append(x_vector[x] - orthogonal_subspace[x])

      v.append(new_v_component)

    return v

  #function which multiplies a matrix by a scalar
  @staticmethod
  def matrix_multiply_scalar(scalar : int, matrix : list):
    product = []

    for row in range(len(matrix)):
      product_row = []

      for col in range(len(matrix[0])):
        product_row.append(matrix[row][col] * scalar)

      product.append(product_row)

    return product

  #function which multiplies two matrices together
  @staticmethod
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

  #Euclid's algorithm for finding a common multiple
  @staticmethod
  def __find_gcd(a, b):
    if (b == 0):
      return a
    else:
      return matrix_operations.__find_gcd(b, a % b)

  #given an input matrix, perform gaussian elimination to find the solution set
  #output will be a list of integers
  #an example row: [x1, x2, x3, x4]
  @staticmethod
  def gaussian_elimination(matrix):

    solution = []
    #iterate through each column
    for col in matrix[0]:

      #iterate through each row/element in the column
      for i in range(len(matrix) - 1):

        num_1 = matrix[i][col]
        num_2 = matrix[i + 1][col]

        #find a common factor, if there is none, find a common multiple
        gcd = matrix_operations.__find_gcd(num_1, num_2)
        if (gcd != 1): #there is a common factor

          #use the scaling row reduction technique
          #scale the first row
          scale = (num_1 / gcd)




    return solution








  @staticmethod
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
      determinant += num * matrix_operations.compute_determinant(sub_matrix)

    return determinant

  @staticmethod
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

  @staticmethod
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
