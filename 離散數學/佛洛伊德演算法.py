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
    return reach.tolist()

# 示例
matrix = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1]
]

closure = transitive_closure(matrix)
print("Transitive closure:")
for row in closure:
    print(row)
