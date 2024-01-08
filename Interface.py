import tkinter as tk
from tkinter import *
from tkinter import filedialog

if __name__ == '__main__':
	if __package__ is None:
		import sys
		from os import path
		print(path.dirname( path.dirname( path.abspath(__file__) ) ))
		sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))
		from store.action.actors import startRegistration
		from gui.Kream import login
		
	else:
		from store.action.actors import startRegistration
		from gui.Kream import login

def upload_action():
    filepath = filedialog.askopenfilename()
    if filepath:
        excelPath.config(state='normal')
        excelPath.delete(0, tk.END)
        excelPath.insert(0, filepath)
        excelPath.config(state='readonly')

def create_label(master, text):
    return tk.Label(master, text=text, font=('Arial', 10))

def create_entry(master, show=None):
    return tk.Entry(master, font=('Arial', 10), show=show)

def create_button(master, text, command):
    return tk.Button(master, text=text, command=command, font=('Arial', 10), bg='#4CAF50', fg='white')

def create_radiobutton(master, text, variable, value):
    return tk.Radiobutton(master, text=text, variable=variable, value=value, font=('Arial', 10))

def create_readonly_entry(master):
    entry = tk.Entry(master, font=('Arial', 10), state='readonly')
    return entry

popTitle = 'KREAM 보관판매 매크로'

window = tk.Tk()
window.title(popTitle)
window.geometry('640x480')
window.resizable(True, True)

login_frame = tk.Frame(window, pady=10)
login_frame.pack(fill='x', padx=20)

tk.Label(login_frame, text="로그인 EMAIL 주소").grid(row=0, column=0, padx=5)
entry_product_name = tk.Entry(login_frame)
entry_product_name.grid(row=0, column=1, padx=5)

tk.Label(login_frame, text="비밀번호").grid(row=0, column=2, padx=5)
entry_product_price = tk.Entry(login_frame, show="*")
entry_product_price.grid(row=0, column=3, padx=5)

loginType = tk.IntVar()
radio_frame = tk.Frame(window, pady=10)
radio_frame.pack(fill='x', padx=20)

radio1 = create_radiobutton(radio_frame, "이메일", loginType, 1)
radio1.pack(side=tk.LEFT, fill='x', expand=True)

radio2 = create_radiobutton(radio_frame, "네이버", loginType, 2)
radio2.pack(side=tk.LEFT, fill='x', expand=True)

login_button = create_button(window, "로그인", lambda: login(entry_product_name.get(), entry_product_price.get(), loginType.get()))
login_button.pack(fill='x', padx=80, pady=10)

login_result_frame = tk.Frame(window, pady=5)
login_result_frame.pack(fill='x', padx=20)

login_result_label = create_label(login_result_frame, "로그인 결과")
login_result_label.pack(side=tk.LEFT)

login_result_entry = create_readonly_entry(login_result_frame)
login_result_entry.pack(side=tk.LEFT, fill='x', expand=True)

file_frame = tk.Frame(window, pady=10)
file_frame.pack(fill='x', padx=20)

excelButton = create_button(file_frame, "파일 업로드", upload_action)
excelButton.pack(side=tk.LEFT)

excelPath = tk.Entry(file_frame, state='readonly', width=50, font=('Arial', 10))
excelPath.pack(side=tk.LEFT, fill='x', expand=True)

submit_button = create_button(window, "등록시작", lambda: startRegistration(excelPath.get()))
submit_button.pack(fill='x', padx=80, pady=10)

window.mainloop()