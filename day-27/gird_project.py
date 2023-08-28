import tkinter

window = tkinter.Tk()

window.title('Grid')
window.minsize(width=800,height=600)
window.config(padx=100,pady=200)

my_label = tkinter.Label(text="I am Label")
my_label.grid(row=0,column=0)

button = tkinter.Button(text= 'Button')
button.grid(row=1,column=1)

new_button = tkinter.Button(text='New Button')
new_button.grid(row=0,column=2)

entry = tkinter.Entry()
entry.grid(row=2,column=3)








window.mainloop()