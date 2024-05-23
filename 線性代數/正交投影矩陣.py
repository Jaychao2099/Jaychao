import numpy as np
import tkinter as tk
from tkinter import messagebox
from fractions import Fraction
from sympy import sqrt, Rational

def calculate_expression():
    try:
        rows = int(rows_entry.get())
        cols = int(cols_entry.get())
    except ValueError:
        messagebox.showerror("錯誤", "請輸入有效的行數和列數。")
        return

    matrix_input = matrix_text.get("1.0", tk.END)
    matrix_rows = matrix_input.strip().split(";")
    
    if len(matrix_rows) != rows:
        messagebox.showerror("錯誤", "輸入的 Rows 不符。")
        return

    input_matrix = []
    for row in matrix_rows:
        row_values = row.strip().split()
        if len(row_values) != cols:
            messagebox.showerror("錯誤", "輸入的 Columns 不符。")
            return
        input_matrix.append([float(val) for val in row_values])
    input_matrix = np.array(input_matrix)
    
    result = calculate_result(input_matrix)

    result_str = format_result(result)

    result_label.config(text="正交投影運算矩陣：\n" + result_str)

def calculate_result(A):
    AT = np.transpose(A)
    ATA = np.dot(AT, A)
    ATA_inverse = np.linalg.inv(ATA)
    A_times_ATA_inverse = np.dot(A, ATA_inverse)
    result = np.dot(A_times_ATA_inverse, AT)
    return result

def format_result(result):
    formatted = []
    col_widths = [0] * result.shape[1]
    
    # Format each value and find the maximum width for each column
    for row in result:
        formatted_row = []
        for i, val in enumerate(row):
            if np.isclose(val, int(val)):
                formatted_val = str(int(val))
            else:
                frac = Fraction(val).limit_denominator()
                if np.isclose(float(frac), val):
                    formatted_val = str(frac)
                else:
                    sympy_val = Rational(val).limit_denominator()
                    sqrt_val = sympy_val**2
                    if sqrt_val == Rational(val):
                        formatted_val = f"sqrt({sqrt_val})"
                    else:
                        formatted_val = f"{val:.4f}"
            formatted_row.append(formatted_val)
            col_widths[i] = max(col_widths[i], len(formatted_val))
        formatted.append(formatted_row)
    
    # Create a properly spaced string
    result_str = ""
    for row in formatted:
        row_str = "   ".join(f"{val:^{col_widths[i]}}" for i, val in enumerate(row))
        result_str += row_str + "\n"
    
    return result_str.strip()

# 建立主視窗
root = tk.Tk()
root.title("正交投影計算器")

rows_label = tk.Label(root, text="Rows：")
rows_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
rows_entry = tk.Entry(root, width=5)
rows_entry.grid(row=0, column=1, padx=5, pady=5)

cols_label = tk.Label(root, text="Columns：")
cols_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")
cols_entry = tk.Entry(root, width=5)
cols_entry.grid(row=0, column=3, padx=5, pady=5)

matrix_label = tk.Label(root, text="請輸入正交投影目標的 subspace 的 basis\n（columns 用空格分隔，rows 用分號分隔）：")
matrix_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

matrix_text = tk.Text(root, width=40, height=10)
matrix_text.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

calculate_button = tk.Button(root, text="計算", command=calculate_expression)
calculate_button.grid(row=3, columnspan=4, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=4)

root.mainloop()
