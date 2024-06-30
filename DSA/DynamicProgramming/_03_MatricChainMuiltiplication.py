"""
Suppose we want to multiply n matrices defined as follows:

    A_1,n = A_1 * A_2 * ... * A_n

Now, matrix multiplication is associative, as a result we can parenthesise the matrices above in whatever way we want,
and in doing so, we can change the number of scaler multiplications that occur, while still resulting in the same
output answer.

    Matrices:

        Let A be a (p x q) matrix and B be a (q x r) matrix, then A.B will be a (p x r) matrix that has undergone
        p.q.r scalar multiplications.

        Now consider:
            A is (10 x 100)
            B is (100 x 5)
            C is (5 x 50)

            A.B will be (10 x 5) and undergone 10.100.5= 5000 operations, hence (A.B).C will be 5000 + 10.5.50 = 7500
            scalar operations total.

            Now take B.C, results in (100 x 50) with 100.5.50=25000 operations, and A.(B.C) will be 2500 + 10.100.50
            = 75000 operations.

            Clearly by doing (A.B).C we result in significantly fewer scalar multiplications.


Our goal is to minimise the number of scalar multiplications in a chain of matrix multiplications by choosing the
optimal parenthesis.


Approach:

    Consider the multiplication chain A_i,j = A_i * A_(i+1) * ... * A_j, i <= j, to parenthesise this we must find some
    k where i <= k < j such that A_i,j = A_i,k * A_(k+1),j . The cost of this will be:

        A_i,k + A_(k+1),j + the cost of multiplying both to form A_i,j

    Now, suppose k formed the optimal  parenthesis, then the way the sub-chains A_i,k and A_(k+1),j are parenthesised
    must also be optimal, otherwise in the formation of A_i,j we would have substituted in the more optimal parenthesis.

    Let m(i,j) be the minimum number of scalar multiplications to compute A_i,j

        - if i=j, m(i, i) = 0 since it is just one matrix

        - if i < j, we use the optimal substructure m(i, j) = m(i, k) + m(k+1, j) + p_(i-1)*p_k*p_j where a matrix A_i
        is (p_(i-1) x p_i) rows by columns

    Now our task is to find the value k=i, i+1, ..., j-1 which makes m(i,j) a minimum

"""


def matrix_chain_multiplication(row_col_list, show=False):
    """
    row_col_list is an iterable (r, c) giving the row and column lengths of matrices A_0, ..., A_n in order
    """
    n = len(row_col_list)
    k_pos = [[0]*n for _ in range(n)]
    opt_val = [[float("inf")]*n for _ in range(n)]
    for i in range(n):
        opt_val[i][i] = 0
    for chain_length in range(2, n+1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            for k in range(i, j):
                temp = opt_val[i][k] + opt_val[k+1][j] + (row_col_list[i][0] * row_col_list[k][1] * row_col_list[j][1])
                if temp < opt_val[i][j]:
                    opt_val[i][j] = temp
                    k_pos[i][j] = k
    if show:
        print("Opt_val:")
        for row in range(n):
            print("  row:", row, opt_val[row])
        print("K-pos")
        for row in range(n):
            print("  row:", row, k_pos[row])
    return k_pos, opt_val


def show_solution(k_pos, i, j):
    if i == j:
        print("A_" + str(i), end=" ")
    else:
        print("(", end=" ")
        show_solution(k_pos, i, k_pos[i][j])
        show_solution(k_pos, k_pos[i][j]+1, j)
        print(")", end=" ")


def example():
    r_c = [(30, 35),
           (35, 15),
           (15, 5),
           (5, 10),
           (10, 20),
           (20, 25)
           ]
    k, opt = matrix_chain_multiplication(r_c, show=True)
    print("\nStarting matrices:", r_c)
    print("\nOptimal Solution m(0, 5):", opt[0][5])
    print("Parenthesis at k pos:", k[0][5])
    print("\nBecause we know their is a break at k=2, we know optimal solution has the form (A_0,2)*(A_3,5)"
          " we can check the optimal solutions for A_0,2 and A_3,5")
    print("\nOptimal Solution m(0, 2):", opt[0][2])
    print("Parenthesis at k pos:", k[0][2])
    print("\nOptimal Solution m(3, 5):", opt[3][5])
    print("Parenthesis at k pos:", k[3][5])
    print("\nWe can now write  A_0,5 as ((A_0) * (A_1,2)) * ((A_3,4) * A_5) which is effectively, the fully "
          "parenthesised optimal solution")
    print("\n-----SOLUTION-----")
    show_solution(k, 0, len(k)-1)


example()