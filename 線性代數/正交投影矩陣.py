import numpy as np
import tkinter as tk
from tkinter import messagebox
from fractions import Fraction
from sympy import sympify

# 全局變量來跟踪結果顯示的格式
display_as_fractions = True

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
        parsed_row = []
        for val in row_values:
            try:
                parsed_val = float(sympify(val))
                parsed_row.append(parsed_val)
            except (ValueError, SyntaxError):
                messagebox.showerror("錯誤", f"無法解析輸入值: {val}")
                return
        input_matrix.append(parsed_row)
    
    input_matrix = np.array(input_matrix)
    
    result = calculate_result(input_matrix)
    display_result(result)

def calculate_result(A):
    AT = np.transpose(A)
    ATA = np.dot(AT, A)
    ATA_inverse = np.linalg.inv(ATA)
    A_times_ATA_inverse = np.dot(A, ATA_inverse)
    result = np.dot(A_times_ATA_inverse, AT)
    return result

def format_result(result, as_fractions):
    formatted = []
    col_widths = [0] * result.shape[1]
    
    # Format each value and find the maximum width for each column
    for row in result:
        formatted_row = []
        for i, val in enumerate(row):
            if np.isclose(val, int(val)):
                formatted_val = str(int(val))
            else:
                if as_fractions:
                    frac = Fraction(val).limit_denominator()
                    if np.isclose(float(frac), val):
                        formatted_val = str(frac)
                    else:
                        formatted_val = f"{val:.4f}"
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

def display_result(result):
    global display_as_fractions
    result_str = format_result(result, display_as_fractions)
    result_label.config(text="正交投影運算矩陣：\n" + result_str)

def toggle_display_format():
    global display_as_fractions
    display_as_fractions = not display_as_fractions
    current_result = result_label.cget("text").split("：\n")[1]
    if current_result:
        current_result = np.array([[float(sympify(cell)) for cell in row.split()] for row in current_result.split('\n')])
        display_result(current_result)

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
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

toggle_button = tk.Button(root, text="切換顯示格式", command=toggle_display_format)
toggle_button.grid(row=3, column=2, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=4)

root.mainloop()
