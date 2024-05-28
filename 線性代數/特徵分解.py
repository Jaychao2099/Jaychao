import tkinter as tk
from tkinter import messagebox
import numpy as np

def decompose_matrix():
    try:
        matrix_input = entry.get("1.0", tk.END).strip()
        matrix = np.array([float(x) for x in matrix_input.split(',')])
        n = int(np.sqrt(len(matrix)))
        if n * n != len(matrix):
            raise ValueError("錯誤, 請確認輸入為方陣.")
        matrix = matrix.reshape((n, n))

        eigenvalues, eigenvectors = np.linalg.eig(matrix)

        result_text.set(f"Eigenvalues:\n{eigenvalues}\n\nEigenvectors:\n{eigenvectors}")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

# 創建主窗口
root = tk.Tk()
root.title("矩陣特徵分解")

# 創建文本輸入框
label = tk.Label(root, text="請輸入方陣元素 rows by rows\n(用逗號分隔, 可不用換行):")
label.pack(pady=10)

entry = tk.Text(root, height=5, width=50)
entry.pack(pady=10)

# 創建結果顯示區域
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT)
result_label.pack(pady=10)

# 創建分解按鈕
button = tk.Button(root, text="特徵分解", command=decompose_matrix)
button.pack(pady=10)

# 運行主循環
root.mainloop()
