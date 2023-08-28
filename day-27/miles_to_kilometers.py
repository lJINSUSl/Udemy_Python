import tkinter

window = tkinter.Tk()

window.title('Mile to Km Converter')
window.minsize(width=800,height=600)
window.config(padx=100,pady=200)



Entry_miles = tkinter.Entry()
Entry_miles.grid(row=0,column=1)

Label_Miles = tkinter.Label(text='Miles')
Label_Miles.grid(row=0,column=2)

Label_is_equal_to = tkinter.Label(text='is equal to')
Label_is_equal_to.grid(row=1,column=0)

Label_Calculated = tkinter.Label(text='0')
Label_Calculated.grid(row=1,column=1)

Label_Km = tkinter.Label(text='Km')
Label_Km.grid(row=1,column=2)

def calculate():
    Label_Calculated.config(text=round(float(Entry_miles.get())*1.6))

Button_Calculate = tkinter.Button(text='Calculate', command = calculate)
Button_Calculate.grid(row=2,column=1)




window.mainloop()
