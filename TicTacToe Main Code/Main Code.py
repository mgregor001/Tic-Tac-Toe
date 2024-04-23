import tkinter as tk 
window = tk.Tk()
frame = tk.Frame(master=window, width=150,height=250, bg="black")
frame.pack()
window.columnconfigure([0, 1, 2], weight=1, minsize=50)
window.rowconfigure([0, 1, 2], weight=1, minsize=50)

Key=True

def handler_1():
    btn_1['text'] += ""
    while Key is True:
        btn_1['text'] = 'X'
        return Key==False
        break
    while Key is False:
        btn_1['text'] = 'o'
        return Key==True
        break

def handler_2():
    btn_2['text'] += " "
    while Key==True:
        btn_2['text'] = 'X'
        return Key==False
        break
    while Key is False:
        btn_2['text'] = 'o'
        Key==True
        break

def handler_3():
    btn_3['text'] += " "
    while Key is True:
        btn_3['text'] = 'X'
        Key==False
        break
    while Key is False:
        btn_3['text'] = 'o'
        Key==True
        break

def handler_4():
    btn_4['text'] = " "
    while Key is True:
        btn_4['text'] = 'X'
        Key==False
        break
    while Key is False:
        btn_4['text'] = 'o'
        Key==True
        break

def handler_5():
    btn_5['text'] = " "
    while Key is True:
        btn_5['text'] = 'X'
        Key==False
        break
    while Key is False:
        btn_5['text'] = 'o'
        Key==True
        break

def handler_6():
    btn_6['text'] = " "
    while Key is True:
        btn_6['text'] = 'X'
        Key==False
        break
    while Key is False:
        btn_6['text'] = 'o'
        Key==True
        break

def handler_7():
    btn_7['text'] = " "
    while Key is True:
        btn_7['text'] = 'X'
        Key==False
        break
    while Key is False:
        btn_7['text'] = 'o'
        Key==True
        break

def handler_8():
    btn_8['text'] = " "
    while Key is True:
        btn_8['text'] = 'X'
        Key==False
        break
    while Key is False:
        btn_8['text'] = 'o'
        Key==True
        break

def handler_9():
    btn_9['text'] = " "
    while Key is True:
        btn_9['text'] = 'X'
        Key==False
        break
    while Key is False:
        btn_9['text'] = 'o'
        Key==True
        break

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


    

window.mainloop()