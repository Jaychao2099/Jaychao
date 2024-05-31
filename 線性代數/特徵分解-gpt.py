import tkinter as tk
from tkinter import ttk
import numpy as np
from sympy import nsimplify, sympify, Abs

# 顯示模式函數
def matrix_float(M):
    M = np.array(M, dtype=float)
    M[np.abs(M) < 1e-15] = 0
    return M

def matrix_readable(M):
    def format_element(x):
        elem = str(nsimplify(x))
        return '0' if Abs(sympify(x)) < 1e-15 else elem

    formatted = np.vectorize(format_element)(M)
    max_lengths = [max(len(elem) for elem in formatted[:, col]) for col in range(formatted.shape[1])]
    formatted_done = np.array([['{:>{}}'.format(elem, max_lengths[j]) for j, elem in enumerate(row)] for row in formatted])
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
    display_func = matrix_float if display_mode == "Float" else matrix_readable

    A, P, D = eigen_decomposition(A)

    output_matrix.delete("1.0", "end")
    output_matrix.insert("end", "Input Matrix (A):\n")
    output_matrix.insert("end", np.array2string(display_func(A), separator=' ', formatter={'str_kind': lambda x: x}) + "\n\n")
    output_matrix.insert("end", "Eigenvalues (D):\n")
    output_matrix.insert("end", np.array2string(display_func(D), separator=' ', formatter={'str_kind': lambda x: x}) + "\n\n")
    output_matrix.insert("end", "Eigenvectors (P):\n")
    output_matrix.insert("end", np.array2string(display_func(P), separator=' ', formatter={'str_kind': lambda x: x}) + "\n\n")

# 創建GUI
root = tk.Tk()
root.title("矩陣特徵分解")

# 輸入矩陣
input_frame = ttk.LabelFrame(root, text="輸入矩陣")
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
