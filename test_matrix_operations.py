from MatrixOperations import matrix_operations

def test_compute_projection():

  test_cases = [

    [1,7], [-4,2],
    [7,6], [4,2]

  ]

  for i in range(0, len(test_cases), 2):
    print(matrix_operations.compute_projection(test_cases[i], test_cases[i + 1]))

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

    print(matrix_operations.matrix_multiply(test_cases_a[i], test_cases_b[i]))

def test_compute_determinant():

  test_cases = [

    [ [3,0,4], [2,3,2], [0,5,-1]    ],
    [  [2,-2,3],  [3,1,2],  [1,3,-1]  ],
    [   [4,0,0,5],  [1,7,2,-5], [3,0,0,0],  [8,3,1,7]   ],
    [  [4,0,-7,3,-5], [0,0,2,0,0],  [7,3,-6,4,-8],  [5,0,5,2,-3], [0,0,9,-1,2]      ]

  ]

  for i in range(len(test_cases)):
    print(matrix_operations.compute_determinant(test_cases[i]))

def test_transpose_matrix():

  test_cases = [

    [ [-5,2], [1,-3], [0,4]  ],
    [  [1,1,1,1], [-3,5,-2,7]   ]

  ]

  for i in range(len(test_cases)):
    print(matrix_operations.transpose_matrix(test_cases[i]))

test_transpose_matrix()


