import tkinter as tk 
window = tk.Tk()
frame = tk.Frame(master=window, width=150,height=250, bg="black")
frame.pack()
window.columnconfigure([0, 1, 2], weight=1, minsize=50)
window.rowconfigure([0, 1, 2], weight=1, minsize=50)

Key=True

def handler_1():
    global Key
    if Key and btn_1['text'] == '':
        btn_1['text'] = 'X'
    elif not Key and btn_1['text'] == '':
        btn_1['text'] = 'o'
    else:
        print("not available")
    Key = not Key
    check()

def handler_2():
    global Key
    if Key and btn_2['text'] == '':
        btn_2['text'] = 'X'
    elif not Key and btn_2['text'] == '':
        btn_2['text'] = 'o'
    else:
        print("not available")
    Key = not Key
    check()

def handler_3():
    global Key
    if Key and btn_3['text'] == '':
        btn_3['text'] = 'X'
    elif not Key and btn_3['text'] == '':
        btn_3['text'] = 'o'
    else:
        print("not available")
    Key = not Key
    check()

def handler_4():
    global Key
    if Key and btn_4['text'] == '':
        btn_4['text'] = 'X'
    elif not Key and btn_4['text'] == '':
        btn_4['text'] = 'o'
    else:
        print("not available")
    Key = not Key
    check()

def handler_5():
    global Key
    if Key and btn_5['text'] == '':
        btn_5['text'] = 'X'
    elif not Key and btn_5['text'] == '':
        btn_5['text'] = 'o'
    else:
        print("not available")
    Key = not Key
    check()

def handler_6():
    global Key
    if Key and btn_6['text'] == '':
        btn_6['text'] = 'X'
    elif not Key and btn_6['text'] == '':
        btn_6['text'] = 'o'
    else:
        print("not available")
    Key = not Key
    check()

def handler_7():
    global Key
    if Key and btn_7['text'] == '':
        btn_7['text'] = 'X'
    elif not Key and btn_7['text'] == '':
        btn_7['text'] = 'o'
    else:
        print("not available")
    Key = not Key
    check()

def handler_8():
    global Key
    if Key and btn_8['text'] == '':
        btn_8['text'] = 'X'
    elif not Key and btn_8['text'] == '':
        btn_8['text'] = 'o'
    else:
        print("not available")
    Key = not Key
    check()

def handler_9():
    global Key
    if Key and btn_9['text'] == '':
        btn_9['text'] = 'X'
    elif not Key and btn_9['text'] == '':
        btn_9['text'] = 'o'
    else:
        print("not available")
    Key = not Key
    check()

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
btn_2.grid(row=0, column=1, sticky="nsew")
btn_3.grid(row=0, column=2, sticky="nsew")
btn_4.grid(row=1, column=0, sticky="nsew")
btn_5.grid(row=1, column=1, sticky="nsew")
btn_6.grid(row=1, column=2, sticky="nsew")
btn_7.grid(row=2, column=0, sticky="nsew")
btn_8.grid(row=2, column=1, sticky="nsew")
btn_9.grid(row=2, column=2, sticky="nsew")

def check():
    if btn_1['text'] == btn_2['text'] == btn_3['text']:
        if btn_1['text'] == 'X':
            print("congratulations player 1 you win!!")
        elif btn_1['text'] == 'o':
            print("congratulations player 2 you win!!")


window.mainloop()