from tkinter import *
from tkinter import messagebox # messagebox는 따로 임포트 해주어야 함. 함수이기 때문
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letter

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    entry_password.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()
    #json 형식의 데이터 정렬
    new_data = {
        website:  {
                        "email" : email_username,
                        "password" : password

                    }
    }

    if not website or not email_username or not password:
        messagebox.showwarning(title="Oops",message="Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title= website, message=f"You've entered: {website}"
                                                               f"{email_username},{password}"
                                                               f"Is it ok to save?")

        #is_ok에서 확인버튼 누른다면 실행
        if is_ok:
            try:
                file =  open('data.json',"r")
                # json.dump(new_data,file,indent=4)

            except FileNotFoundError:
                file = open('data.json', "w")
                json.dump(new_data, file, indent=4)
            else:
                #데이터 읽기
                data = json.load(file)
                #데이터 업데이트 하기
                data.update(new_data)
                #업데이트 한 데이터를 다시 쓰기
                file = open('data.json', "w")
                json.dump(data, file, indent=4)
            finally:
                entry_website.delete(0,'end')
                entry_website.focus()
                entry_email_username.delete(0,'end')
                entry_email_username.insert(0, "jinhong4107@gmail.com")
                entry_password.delete(0,'end')
                file.close()


def find_password():
    website = entry_website.get()

    if not website:
        messagebox.showwarning(title="Oops",message="Please don't leave website fields empty")

    try:
        file = open('data.json', "r")
    except FileNotFoundError:
        messagebox.showwarning(title="Oops",message="There's no such file")
    else:
        data = json.load(file)
        try:
            find_email = data[website]["email"]
            find_password = data[website]["password"]
        except:
            messagebox.showwarning(title="Oops", message="No details for the website exits")
        else:
            messagebox.showinfo(title="Email/PW", message=f"Email: {find_email}\n"
                                                          f"Password: {find_password}")
            file.close()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

label_website = Label(text="Website")
label_website.grid(row=1,column=0)

label_email_username = Label(text="Email/Username")
label_email_username.grid(row=2,column=0)

label_Password = Label(text="Password")
label_Password.grid(row=3,column=0)



entry_website = Entry(width=21)
entry_website.grid(row=1,column=1)
entry_website.focus()

entry_email_username = Entry(width=35)
entry_email_username.grid(row=2,column=1,columnspan=2)
entry_email_username.insert(0,"jinhong4107@gmail.com")

entry_password = Entry(width=21,highlightthickness=0)
entry_password.grid(row=3,column=1)

button_generate_password = Button(text="Generate Password",command=generate_password,width=18)
button_generate_password.grid(row=3,column=2)

button_add = Button(text="Add",width=36,command=save)
button_add.grid(row=4,column=1,columnspan=2)

button_search = Button(text="Search",width=18,command=find_password)
button_search.grid(row = 1, column=2)

canvas = Canvas(width=200,height=200)
mypass_img = PhotoImage(file = 'logo.png')
canvas.create_image(100,100,image = mypass_img)
canvas.grid(row=0,column=1)






















window.mainloop()