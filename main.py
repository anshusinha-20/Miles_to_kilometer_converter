"""imported tkinter module"""
import tkinter

"""creating window object"""
window = tkinter.Tk()
window.minsize(width=500, height=500)

"""setting up label"""
label1 = tkinter.Label(text="I am a label", font=("Courier", 20, "bold"))
label1.pack(expand=True)



"""main loop to keep window open"""
window.mainloop()