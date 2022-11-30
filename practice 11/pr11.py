# -- coding: utf-8 --
from tkinter import*
import json
import requests
def clicked():
    username=txt.get()
    url=f"https://api.github.com/users/{username}"
    user_data=requests.get(url).json()
    with open(r"C:\Users\user\Desktop\Galushka.txt","w") as file:
        if 'company' in user_data:
            file.write(f"'company': {user_data['company']}" + '\n')
        else:
            file.write(f"'company': None" + '\n')
        if 'created_at' in user_data:
            file.write(f"'created_at':{user_data['created_at']}" + '\n')
        else:
            file.write(f"'created_at': None" + '\n')
        if 'email' in user_data:
            file.write(f"'email':{user_data['email']}" + '\n')
        else:
            file.write(f"'email': None")
        if 'id' in user_data:
            file.write(f"'id':{user_data['id']}" + '\n')
        else:
            file.write(f"'id': None")
        if 'name' in user_data:
            file.write(f"'name':{user_data['name']}" + '\n')
        else:
            file.write(f"'name': None")
        if 'url' in user_data:
            file.write(f"'url':{user_data['url']}" + '\n')
        else:
            file.write(f"'url': None")
    lbl.configure(text = 'данные записаны в файл')
root=Tk()
root.title('Галушка Павел')
root.geometry('500x50')
lbl=Label(root,text = 'введите имя пользователя github',font = ('Arial',15))
lbl.grid(column=0,row=0)
btn=Button(root,text = 'выполнить',command = clicked)
btn.grid(column=2,row=0)
txt=Entry(root,width=10)
txt.grid(column=1,row=0)
root.mainloop()