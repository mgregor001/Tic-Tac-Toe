import tkinter as tk 
window = tk.Tk()
frame = tk.Frame(master=window, width=150,height=250, bg="black")
frame.pack()
window.columnconfigure([0, 1, 2], weight=1, minsize=50)
window.rowconfigure([0, 1, 2], weight=1, minsize=50)

lbl_amount = tk.Label(master=window, text="")
lbl_amount.pack()

def handler_1():
    btn_1['text'] += ""

def handler_2():
    lbl_amount['text'] += " "

def handler_3():
    lbl_amount['text'] += " "

def handler_4():
    lbl_amount['text'] += " "

def handler_5():
    lbl_amount['text'] += " "

def handler_6():
    lbl_amount['text'] += " "

def handler_7():
    lbl_amount['text'] += " "

def handler_8():
    lbl_amount['text'] += " "

def handler_9():
    lbl_amount['text'] += " "

btn_1 = tk.Button(master=frame, command=handler_1, width=7, height=3, padx=5, pady=5)
btn_2 = tk.Button(master=frame, command=handler_2, width=7, height=3, padx=5, pady=5)
btn_3 = tk.Button(master=frame, command=handler_3, width=7, height=3, padx=5, pady=5)
btn_4 = tk.Button(master=frame, command=handler_4, width=7, height=3, padx=5, pady=5)
btn_5 = tk.Button(master=frame, command=handler_5, width=7, height=3, padx=5, pady=5)
btn_6 = tk.Button(master=frame, command=handler_6, width=7, height=3, padx=5, pady=5)
btn_7 = tk.Button(master=frame, command=handler_7, width=7, height=3, padx=5, pady=5)
btn_8 = tk.Button(master=frame, command=handler_8, width=7, height=3, padx=5, pady=5)
btn_9 = tk.Button(master=frame, command=handler_9, width=7, height=3, padx=5, pady=5)

btn_1.grid(row=0, column=0, sticky="nsew")
btn_2.grid(row=1, column=0, sticky="nsew")
btn_3.grid(row=2, column=0, sticky="nsew")
btn_4.grid(row=0, column=1, sticky="nsew")
btn_5.grid(row=1, column=1, sticky="nsew")
btn_6.grid(row=2, column=1, sticky="nsew")
btn_7.grid(row=0, column=2, sticky="nsew")
btn_8.grid(row=1, column=2, sticky="nsew")
btn_9.grid(row=2, column=2, sticky="nsew")

bool=True
# if bool is True:
    

window.mainloop()