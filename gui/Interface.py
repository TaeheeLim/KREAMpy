import tkinter as tk
from tkinter import *

def submitForm():
    print('폼 제출')

popTitle = 'KREAM 보관판매 매크로'

window = tk.Tk()
window.title(popTitle)
window.geometry('640x400+100+100')
window.resizable(True, True)

tk.Label(window, text="로그인 EMAIL 주소").pack()
entry_product_name = tk.Entry(window)
entry_product_name.pack()

tk.Label(window, text="비밀번호").pack()
entry_product_price = tk.Entry(window)
entry_product_price.pack()

submit_button = tk.Button(window, text="Submit", command=submitForm)
submit_button.pack()

window.mainloop()