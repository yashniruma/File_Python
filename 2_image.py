from tkinter import *
try:
    r=Tk()
    r.geometry("700x500")

    #  Add photo
    photo = PhotoImage(file="../Re_Prectic/GUI/dada.jpg.png")  # 1st Step
    lab = Label(image=photo)  # 2nd Step
    lab.pack()  # 3rd Step

    r.mainloop()

except Exception as e:
    print(f"Error :- {e}")