import numpy as np
import tkinter as tk
from tkinter import messagebox

def calculate_expression():
     # 從文字方塊取得使用者輸入的行數和列數
     try:
         rows = int(rows_entry.get())
         cols = int(cols_entry.get())
     except ValueError:
         messagebox.showerror("錯誤", "請輸入有效的行數和列數。")
         return

     # 從大文字方塊取得使用者輸入的矩陣
     matrix_input = matrix_text.get("1.0", tk.END)
     matrix_rows = matrix_input.strip().split(";")
    
     # 檢查輸入的行數是否與使用者指定的行數相符
     if len(matrix_rows) != rows:
         messagebox.showerror("錯誤", "輸入的 Rows 不符。")
         return

     # 將使用者輸入的矩陣轉換為NumPy數組
     input_matrix = []
     for row in matrix_rows:
         row_values = row.strip().split(" ")
         if len(row_values) != cols:
             messagebox.showerror("錯誤", "輸入的 Columns 不符。")
             return
         input_matrix.append([float(val) for val in row_values])
     input_matrix = np.array(input_matrix)
    
     # 計算表達式
     result = calculate_result(input_matrix)

     # 顯示結果
     result_label.config(text="正交投影運算矩陣：\n" + str(result))

def calculate_result(A):
     # 計算A的轉置
     AT = np.transpose(A)

     # 計算 A^T * A
     ATA = np.dot(AT, A)

     # 計算 (A^T * A)^-1
     ATA_inverse = np.linalg.inv(ATA)

     # 計算 A * (A^T * A)^-1
     A_times_ATA_inverse = np.dot(A, ATA_inverse)

     # 計算 A * (A^T * A)^-1 * A^T
     result = np.dot(A_times_ATA_inverse, AT)

     return result

# 建立主視窗
root = tk.Tk()
root.title("正交投影計算器")

# 新增輸入行數和列數的標籤和輸入框
rows_label = tk.Label(root, text="Rows：")
rows_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
rows_entry = tk.Entry(root, width=5)
rows_entry.grid(row=0, column=1, padx=5, pady=5)

cols_label = tk.Label(root, text="Columns：")
cols_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")
cols_entry = tk.Entry(root, width=5)
cols_entry.grid(row=0, column=3, padx=5, pady=5)

# 建立大的文字方塊用於輸入矩陣
matrix_label = tk.Label(root, text="請輸入正交投影目標的 subspace 的 basis\n（columns 用空格分隔，rows 用分號分隔）：")
matrix_label.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

matrix_text = tk.Text(root, width=40, height=10)
matrix_text.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

# 新增計算按鈕
calculate_button = tk.Button(root, text="計算", command=calculate_expression)
calculate_button.grid(row=3, columnspan=4, pady=10)

# 顯示結果的標籤
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=4)

# 運行主循環
root.mainloop()