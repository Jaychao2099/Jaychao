import tkinter as tk
from tkinter import ttk
import numpy as np
from sympy import Matrix, symbols, sqrt, nsimplify, fraction, Rational, Integer

# 显示模式函数
def matrix_float(A):
    return np.array(A, dtype=float)

def matrix_readable(A):
    syms = symbols('a:z')
    M = Matrix(A)
    formatted = []
    for elem in M:
        if elem.is_Integer:
            formatted.append(str(elem))
        elif elem.is_Rational:
            numer, denom = fraction(elem)
            if denom == 1:
                formatted.append(str(numer))
            else:
                formatted.append(f"{numer}/{denom}")
        else:
            coeff, base, exp = str(nsimplify(elem)).partition('^')
            if exp:
                if coeff == '1':
                    formatted.append(f"\sqrt{base}^({exp})")
                else:
                    formatted.append(f"{coeff}*\sqrt{base}^({exp})")
            else:
                formatted.append(str(coeff))
    return np.array(formatted, dtype=object).reshape(M.shape)

# 特征分解函数
def eigen_decomposition(A):
    A = matrix_float(A)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    D = np.diag(eigenvalues)

    # 确保特征向量矩阵是正交矩阵
    Q, R = np.linalg.qr(eigenvectors)
    P = Q

    # 根据特征值的大小重新排列P的列
    idx = np.argsort(eigenvalues)[::-1]
    P = P[:, idx]

    return A, P, D

# 事件处理函数
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
    output_matrix.insert("end", "Input Matrix A:\n")
    output_matrix.insert("end", str(display_func(A)) + "\n\n")
    output_matrix.insert("end", "Eigenvalues (D):\n")
    output_matrix.insert("end", str(display_func(D)) + "\n\n")
    output_matrix.insert("end", "Eigenvectors (P):\n")
    output_matrix.insert("end", str(display_func(P)) + "\n\n")

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