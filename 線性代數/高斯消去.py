def swap_rows(matrix, i, j):
    matrix[i], matrix[j] = matrix[j], matrix[i]

def scale_row(matrix, i, scalar):
    matrix[i] = [scalar * x for x in matrix[i]]

def add_scaled_row(matrix, i, j, scalar):
    matrix[i] = [x + scalar * y for x, y in zip(matrix[i], matrix[j])]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def rref(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    lead = 0
    for r in range(num_rows):
        if lead >= num_cols:
            return
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == num_rows:
                i = r
                lead += 1
                if num_cols == lead:
                    return
        swap_rows(matrix, i, r)
        scale_row(matrix, r, 1 / matrix[r][lead])
        for i in range(num_rows):
            if i != r:
                add_scaled_row(matrix, i, r, -matrix[i][lead])
        lead += 1

def create_matrix(num_rows, num_cols):
    matrix = []
    print("Enter the elements of the matrix row-wise:")
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            element = float(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def main():
    num_rows = int(input("Enter the number of rows in the matrix: "))
    num_cols = int(input("Enter the number of columns in the matrix: "))

    if num_cols < num_rows:
        print("Invalid input: Number of columns cannot be less than number of rows.")
        return

    matrix = create_matrix(num_rows, num_cols)

    print("Original matrix:")
    print_matrix(matrix)
    print()

    rref(matrix)

    print("Reduced Row Echelon Form (RREF) of the matrix:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()

