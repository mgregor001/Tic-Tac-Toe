import tkinter as tk 

game_frame = None

def single_player():
    print("WIP. Please select multiplayer")

def multi_player():
    global btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9, btn_restart, game_frame, game_window
    window.withdraw() #New (untaught), hides the original window while the second window is visible
    game_window = tk.Toplevel() #tic tac toe game window. New (untaught) code that will create another tkinter window on top of the first one
    game_window.title("Tic Tac Toe")
    game_frame = tk.Frame(master = game_window, width = 150, height = 250)
    game_frame.pack()
    game_window.columnconfigure([0, 1, 2], weight=1, minsize=50)
    game_window.rowconfigure([0, 1, 2], weight=1, minsize=50)

    game_window.protocol("WM_DELETE_WINDOW", window.destroy)

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
    
    def restart():
        global Key
        btn_1.config(text="")
        btn_2.config(text="")
        btn_3.config(text="")
        btn_4.config(text="")
        btn_5.config(text="")
        btn_6.config(text="")
        btn_7.config(text="")
        btn_8.config(text="")
        btn_9.config(text="")
        Key = True

    def check():
        if btn_1['text'] == btn_2['text'] == btn_3['text']:
            if btn_1['text'] == btn_2['text'] == btn_3['text'] == 'X':
                print("Congratulations player 1 you win!!")
                print("Click 'Restart' to play again!")
            elif btn_1['text'] == btn_2['text'] == btn_3['text'] == 'o':
                print("Congratulations player 2 you win!!")
                print("Click 'Restart' to play again!")
        elif btn_4['text'] == btn_5['text'] == btn_6['text']:
            if btn_4['text'] == btn_5['text'] == btn_6['text'] == 'X':
                print("Congratulations player 1 you win!!")
                print("Click 'Restart' to play again!")
            elif btn_4['text'] == btn_5['text'] == btn_6['text'] == 'o':
                print("Congratulations player 2 you win!!")
                print("Click 'Restart' to play again!")
        elif btn_7['text'] == btn_8['text'] == btn_9['text']:
            if btn_7['text'] == btn_8['text'] == btn_9['text'] == 'X':
                print("Congratulations player 1 you win!!")
                print("Click 'Restart' to play again!")
            elif btn_7['text'] == btn_8['text'] == btn_9['text'] == 'o':
                print("Congratulations player 2 you win!!")
                print("Click 'Restart' to play again!")
        elif btn_1['text'] == btn_4['text'] == btn_7['text']:
            if btn_1['text'] == btn_4['text'] == btn_7['text'] == 'X':
                print("Congratulations player 1 you win!!")
                print("Click 'Restart' to play again!")
            elif btn_1['text'] == btn_4['text'] == btn_7['text'] == 'o':
                print("Congratulations player 2 you win!!")
                print("Click 'Restart' to play again!")
        elif btn_1['text'] == btn_4['text'] == btn_7['text']:
            if btn_1['text'] == btn_4['text'] == btn_7['text'] == 'X':
                print("Congratulations player 1 you win!!")
                print("Click 'Restart' to play again!")
            elif btn_1['text'] == btn_4['text'] == btn_7['text'] == 'o':
                print("Congratulations player 2 you win!!")
                print("Click 'Restart' to play again!")
        elif btn_2['text'] == btn_5['text'] == btn_8['text']:
            if btn_2['text'] == btn_5['text'] == btn_8['text'] == 'X':
                print("Congratulations player 1 you win!!")
                print("Click 'Restart' to play again!")
            elif btn_2['text'] == btn_5['text'] == btn_8['text'] == 'o':
                print("Congratulations player 2 you win!!")
                print("Click 'Restart' to play again!")
        elif btn_3['text'] == btn_6['text'] == btn_9['text']:
            if btn_3['text'] == btn_6['text'] == btn_9['text'] == 'X':
                print("Congratulations player 1 you win!!")
                print("Click 'Restart' to play again!")
            elif btn_3['text'] == btn_6['text'] == btn_9['text'] == 'o':
                print("Congratulations player 2 you win!!")
                print("Click 'Restart' to play again!")
        elif btn_1['text'] == btn_5['text'] == btn_9['text']:
            if btn_1['text'] == btn_5['text'] == btn_9['text'] == 'X':
                print("Congratulations player 1 you win!!")
                print("Click 'Restart' to play again!")
            elif btn_1['text'] == btn_5['text'] == btn_9['text'] == 'o':
                print("Congratulations player 2 you win!!")
                print("Click 'Restart' to play again!")
        elif btn_3['text'] == btn_5['text'] == btn_7['text']:
            if btn_3['text'] == btn_5['text'] == btn_7['text'] == 'X':
                print("Congratulations player 1 you win!!")
                print("Click 'Restart' to play again!")
            elif btn_3['text'] == btn_5['text'] == btn_7['text'] == 'o':
                print("Congratulations player 2 you win!!")
                print("Click 'Restart' to play again!")
        elif all(btn["text"] in ("X", "o") for btn in (btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9)):
            print("Tie!")
            print("Click 'Restart' to play again!")


    btn_1 = tk.Button(master=game_frame, command=handler_1, width=7, height=3, padx=5, pady=5)
    btn_2 = tk.Button(master=game_frame, command=handler_2, width=7, height=3, padx=5, pady=5)
    btn_3 = tk.Button(master=game_frame, command=handler_3, width=7, height=3, padx=5, pady=5)
    btn_4 = tk.Button(master=game_frame, command=handler_4, width=7, height=3, padx=5, pady=5)
    btn_5 = tk.Button(master=game_frame, command=handler_5, width=7, height=3, padx=5, pady=5)
    btn_6 = tk.Button(master=game_frame, command=handler_6, width=7, height=3, padx=5, pady=5)
    btn_7 = tk.Button(master=game_frame, command=handler_7, width=7, height=3, padx=5, pady=5)
    btn_8 = tk.Button(master=game_frame, command=handler_8, width=7, height=3, padx=5, pady=5)
    btn_9 = tk.Button(master=game_frame, command=handler_9, width=7, height=3, padx=5, pady=5)
    btn_restart = tk.Button(master=game_frame, text="Restart", command=restart, width=7, height=3, padx=5, pady=5)

    btn_1.grid(row=0, column=0, sticky="nsew")
    btn_2.grid(row=0, column=1, sticky="nsew")
    btn_3.grid(row=0, column=2, sticky="nsew")
    btn_4.grid(row=1, column=0, sticky="nsew")
    btn_5.grid(row=1, column=1, sticky="nsew")
    btn_6.grid(row=1, column=2, sticky="nsew")
    btn_7.grid(row=2, column=0, sticky="nsew")
    btn_8.grid(row=2, column=1, sticky="nsew")
    btn_9.grid(row=2, column=2, sticky="nsew")
    btn_restart.grid(row=3, column=1, sticky="nsew")

btn_1 = None
btn_2 = None
btn_3 = None
btn_4 = None
btn_5 = None
btn_6 = None
btn_7 = None
btn_8 = None
btn_9 = None
btn_restart = None

window = tk.Tk() #Title Window
window.title("Tic Tac Toe") #Title Window
frame1 = tk.Frame(master = window, width = 150, height = 250) #Title Window
frame1.grid(row = 0, column = 0) #Title Window
window.columnconfigure([0, 1, 2], weight = 1, minsize = 50) #Title Window
window.rowconfigure([0, 1, 2], weight =1 , minsize = 50) #Title Window

label1 = tk.Label(master = frame1, text = "Welcome to Tic Tac Toe! Please Select Your Mode:", anchor = "center") #Title Window
label1.grid(row = 0, column = 0, sticky = "nsew") #Title Window

button1 = tk.Button(master = frame1, text = "Single-Player", command = single_player) #Title Window
button2 = tk.Button(master = frame1, text = "Multiplayer", command = multi_player) #title window
button1.grid(row = 1, column = 0)
button2.grid(row = 2, column = 0)

Key = True

window.mainloop()