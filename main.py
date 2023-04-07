"""imported tkinter module"""
import tkinter

"""creating window object"""
window = tkinter.Tk()
window.minsize(width=500, height=500)

"""setting up label"""
label1 = tkinter.Label(text="I am a label", font=("Courier", 20, "bold"))
label1.pack(expand=True)

# """changing and configuring label"""
# label1["text"] = "I'm a new label"
# label1.config(text="I'm a new label")

"""function to print on button click"""
def buttonClicked():
    inputText = input.get()
    label1.config(text=inputText)

"""creating button object"""
button = tkinter.Button(text="Click me", command=buttonClicked)
button.pack(expand=True)

"""creating input object"""
input = tkinter.Entry(width=10)
input.pack(expand=True)

"""main loop to keep window open"""
window.mainloop()