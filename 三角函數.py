import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive, FloatSlider, Text, VBox, HBox
import ipywidgets as widgets
from IPython.display import display
from scipy.integrate import quad

# 定義一個函數來評估和繪製多個用戶自定義的函數
def plot_custom_functions(num_functions, *args):
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    
    num_functions = int(num_functions)
    functions = args[:num_functions]
    params = args[num_functions:]
    
    plt.figure(figsize=(10, 6))
    
    for i, func in enumerate(functions):
        try:
            # 獲取當前函數的參數
            n = params[i * 2]
            m = params[i * 2 + 1]
            
            # 解析函數並替換變量
            y = eval(func.replace('n', str(n)).replace('m', str(m)).replace('x', '(x)'))
            
            # 特殊處理積分函數
            if 'integral' in func:
                y = np.array([quad(lambda t: eval(func.replace('integral(', '').replace(')', '').replace('n', str(n)).replace('m', str(m)).replace('x', 't')), 0, xi)[0] for xi in x])
            
            plt.plot(x, y, label=f'{func}, n={n}, m={m}')
        except Exception as e:
            print(f"Error in function evaluation for '{func}': {e}")
    
    plt.title(f'Plot of Custom Functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(-10, 10)
    plt.legend()
    plt.grid(True)
    plt.show()

# 創建輸入框和滑桿來調整變數
num_functions_text = Text(value='3', description='Functions:')
function_texts = [Text(value='np.sin(2*n*x)+np.tan(m*x)', description=f'f{i}(x)=') for i in range(3)]
n_sliders = [FloatSlider(min=0.1, max=10.0, step=0.1, value=1.0, description=f'n{i}:') for i in range(3)]
m_sliders = [FloatSlider(min=0.1, max=10.0, step=0.1, value=1.0, description=f'm{i}:') for i in range(3)]

# 使用 interactive 函數來創建交互界面，將每個參數分開傳遞
interactive_plot = interactive(
    plot_custom_functions,
    num_functions=num_functions_text,
    f0=function_texts[0],
    f1=function_texts[1],
    f2=function_texts[2],
    n0=n_sliders[0],
    m0=m_sliders[0],
    n1=n_sliders[1],
    m1=m_sliders[1],
    n2=n_sliders[2],
    m2=m_sliders[2]
)

# 包裝所有小部件
function_inputs = VBox(function_texts)
n_inputs = VBox(n_sliders)
m_inputs = VBox(m_sliders)

# 顯示小部件和繪圖
display(VBox([num_functions_text, function_inputs, n_inputs, m_inputs, interactive_plot]))
