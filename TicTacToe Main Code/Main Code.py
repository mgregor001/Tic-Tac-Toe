import tkinter as tk 
window = tk.Tk()
frame = tk.Frame(master=window)
frame.columnconfigure([0, 1, 2], weight=1, minsize=50)
frame.rowconfigure([0, 1, 2], weight=1, minsize=50)

btn_1 = tk.Button(master=frame)
btn_2 = tk.Button(master=frame)
btn_3 = tk.Button(master=frame)
btn_4 = tk.Button(master=frame)
btn_5 = tk.Button(master=frame)
btn_6 = tk.Button(master=frame)
btn_7 = tk.Button(master=frame)
btn_8 = tk.Button(master=frame)
btn_9 = tk.Button(master=frame)

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