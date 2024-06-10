import tkinter as tk
from tkinter import ttk
import numpy as np
from sympy import nsimplify, sympify, Abs

# 顯示模式函數
def matrix_float(M):    #浮點模式
    M = np.array(M, dtype=float)
    M[np.abs(M) < 1e-15] = 0
    return M

def matrix_readable(M):
   formatted = []
   max_rows, max_columns = np.shape(M)

   for _, row in enumerate(M[row,:] for row in range(max_rows)):  # row0 row1 row2 ...
      row_formatted = []
      for _, elem in enumerate(row):   # elem(0,1) elem(0,2) ... elem(1,1) elem(1,2) ...     
         coeff, _, _ = str(nsimplify(elem)).partition('^')
         if Abs(sympify(coeff)) < 1e-15:
            row_formatted.append('0')
         else:
            row_formatted.append(str(coeff))
      formatted.append(row_formatted)

   formatted = np.asarray(formatted, dtype=object)

   max_lengths = [max(len(str(elem)) for elem in formatted[:,col]) for col in range(max_columns)]
   
   formatted_done = []
   for i, row in enumerate(formatted[rows,:] for rows in range(max_rows)):
      formatted_space = ['{:>{width}}'.format(elem, width=max_lengths[j]) for j, elem in enumerate(row)]
      formatted_done.append(formatted_space)
    
   formatted_done = np.asarray(formatted_done, dtype=object)
   
   return formatted_done

# 特徵分解函數
def eigen_decomposition(A):
    A = matrix_float(A)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    D = np.diag(eigenvalues)

    # 確保特徵向量矩陣是正交矩陣
    Q, _ = np.linalg.qr(eigenvectors)
    P = Q

    # 根據特徵值的大小重新排列P的column
    idx = np.argsort(eigenvalues)[::-1]
    P = P[:, idx]

    return A, P, D

# 事件處理函數
def calculate():
    matrix_input = input_matrix.get("1.0", "end-1c")
    A = np.array([float(x) for x in matrix_input.split()])
    n = int(np.sqrt(len(A)))
    A = A.reshape(n, n)

    display_mode = display_var.get()
    if display_mode == "Float":
        display_func = matrix_float
    else:
        display_func = matrix_readable

    A, P, D = eigen_decomposition(A)

    output_matrix.delete("1.0", "end")
    output_matrix.insert("end", "Input Matrix (A):\n")
    output_matrix.insert("end", str(display_func(A)) + "\n\n")
    output_matrix.insert("end", "Eigenvalues (D):\n")
    output_matrix.insert("end", str(display_func(D)) + "\n\n")
    output_matrix.insert("end", "Eigenvectors (P):\n")
    output_matrix.insert("end", str(display_func(P)) + "\n\n")

# 創建GUI
root = tk.Tk()
root.title("矩陣特徵分解")

# 輸入矩陣
input_frame = ttk.LabelFrame(root, text="輸入矩陣 (用空格分開)")
input_frame.pack(pady=10, padx=10, fill="x")

input_matrix = tk.Text(input_frame, height=5, width=40)
input_matrix.pack(side="left", padx=5)

# 顯示模式
display_frame = ttk.LabelFrame(root, text="顯示模式")
display_frame.pack(pady=10, padx=10, fill="x")

display_var = tk.StringVar(value="Readable")
float_radio = ttk.Radiobutton(display_frame, text="浮點", variable=display_var, value="Float")
readable_radio = ttk.Radiobutton(display_frame, text="易讀", variable=display_var, value="Readable")

float_radio.pack(side="left", padx=5)
readable_radio.pack(side="left", padx=5)

# 計算按鈕
calculate_button = ttk.Button(root, text="計算", command=calculate)
calculate_button.pack(pady=10)

# 輸出結果
output_frame = ttk.LabelFrame(root, text="結果")
output_frame.pack(pady=10, padx=10, fill="both", expand=True)

output_matrix = tk.Text(output_frame, height=20, width=50)
output_matrix.pack(side="left", padx=5, fill="both", expand=True)

root.mainloop()