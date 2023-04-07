# """imported tkinter module"""
# import tkinter
#
# """creating window object"""
# window = tkinter.Tk()
# window.minsize(width=500, height=500)
# window.config(padx=100, pady=100)
#
# """setting up label"""
# label1 = tkinter.Label(text="I am a label", font=("Courier", 20, "bold"))
# # label1.pack(expand=True)
# label1.grid(row=1, column=1)
# label1.config(padx=50, pady=50)
#
# # """changing and configuring label"""
# # label1["text"] = "I'm a new label"
# # label1.config(text="I'm a new label")
#
# """function to print on button click"""
# def buttonClicked():
#     inputText = input.get()
#     label1.config(text=inputText)
#
# """creating button object"""
# button = tkinter.Button(text="Click me", command=buttonClicked)
# # button.pack(expand=True)
# button.grid(row=2, column=2)
#
# """creating button2 object"""
# button2 = tkinter.Button(text="Click me again", command=buttonClicked)
# button2.grid(row=1, column=3)
#
# """creating input object"""
# input = tkinter.Entry(width=10)
# # input.pack(expand=True)
# input.grid(row=3, column=4)
#
# """main loop to keep window open"""
# window.mainloop()