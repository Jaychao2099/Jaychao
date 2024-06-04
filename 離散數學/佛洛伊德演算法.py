import numpy as np

def transitive_closure(matrix):
    # 轉換成numpy矩陣
    reach = np.array(matrix, dtype=int)
    n = len(reach)

    # Floyd-Warshall algorithm to find the transitive closure
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
                """
                print(f"k = {k}, i = {i}, j = {j}")
                for row in reach:
                    print(row)
                print("")
            print("---------------------")
        print("---------------------")
        """
    return np.array(reach.tolist(), dtype=int)

# 示例
matrix = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0]
]

matrix_m = np.array(matrix, dtype=int)
closure = transitive_closure(matrix)
add = closure - matrix_m

print(f"\033[3;4mmatrix:\033[0m\n{matrix_m}\n\033[3;4madd:\033[0m\n{add}\n\033[3;4mTransitive closure\033[0m:\n{closure}".replace('1', '\033[34m1\033[0m'))
