from tkinter import *

#config

def bmi_calculator():
    height = float(entry_height.get())
    height_meters = height /100
    weight = float(entry_weight.get())
    bmi = weight / (height_meters ** 2)



    if bmi < 18.5:

        label.config(text="Underweight 😭😭",fg="Blue")
    elif 18.5 <= bmi < 24.9:

        label.config(text="Normal Weight 😎😎 ",fg="Green")
    elif 24.9 <= bmi < 29.9:

        label.config(text="Over Weight 😢😢",fg="Purple")
    else:

        label.config(text="Obsesity  😭",fg="Black")





##ui

window =Tk()
window.minsize(width=300,height=200)
window.config(bg="Pink")
window.title("BMI CALCULATTOR")

#label
label = Label(text="Enter your Heiight & Weiight",fg="Red",bg="Pink",font=("Comic Sans MS", 20, "bold"))
label.grid(row=0,column=0)
#label.config(pady = 50,padx=200)

#entry_height
entry_height = Entry(width=16)
entry_height.grid(row=1,column=0)
label_for_height = Label(text="HEIGHT (CM)" ,fg = "Blue",bg="Pink")
label_for_height.grid(row=1,column = 1)
label_for_height.config(padx = 40,pady=20)

#entry_weight

entry_weight = Entry(width=16)

entry_weight.grid(row=2,column=0)
label_for_weight = Label(text=" WEIGHT (KG)" ,fg = "Blue",bg="Pink")
label_for_weight.grid(row=2,column = 1)
label_for_weight.config(padx = 40,pady=20)


#button
button_calculate = Button(text ="Calculate",command=bmi_calculator)
button_calculate.grid(row=3,column=0)
window.mainloop()