import tkinter as tk
from tkinter import messagebox
import numpy as np

class GramSchmidtApp:
    def __init__(self, master):
        self.master = master
        master.title("Gram-Schmidt 正交化")

        self.label = tk.Label(master, text="請輸入矩陣, 每個元素之間用空格分隔, row之間用分號(;)分隔：")
        self.label.pack()

        self.entry = tk.Text(master, height=5, width=30)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="計算", command=self.calculate)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate(self):
        try:
            input_text = self.entry.get("1.0", "end-1c")
            matrix = np.array([[float(num) for num in row.split()] for row in input_text.split(";")])
            
            Q = self.gram_schmidt(matrix)
            self.result_label.config(text="Gram-Schmidt 正交化結果：\n" + str(Q))
        except ValueError as e:
            messagebox.showerror("錯誤", str(e))

    def gram_schmidt(self, matrix):
        def normalize(v):
            return v / np.linalg.norm(v)

        def gram_schmidt_process(matrix):
            Q = []
            for i in range(matrix.shape[1]):
                q = matrix[:, i]
                for j in range(i):
                    q -= np.dot(np.dot(matrix[:, i], Q[j]), Q[j])
                if np.linalg.norm(q) < 1e-10:
                    raise ValueError("矩陣的向量是線性相關的, 請確認為linear independence後再輸入。")
                q = normalize(q)
                Q.append(q)
            return np.array(Q).T

        if np.linalg.matrix_rank(matrix) != matrix.shape[1]:
            raise ValueError("矩陣的向量是線性相關的, 請確認為linear independence後再輸入。")
        
        Q = gram_schmidt_process(matrix)
        
        for i in range(Q.shape[1]):
            non_zero_index = np.argmax(np.abs(Q[:, i]) > 1e-10)
            first_non_zero_element = Q[non_zero_index, i]
            Q[:, i] /= first_non_zero_element
        
        return Q

root = tk.Tk()
app = GramSchmidtApp(root)
root.mainloop()
