import tkinter as tk
from PIL import ImageTk, Image
import bot

master = tk.Tk()
def ask():
    query=textF.get()
    chat=bot.Chat(bot.pairs, bot.reflections)
    answer=chat.respond(query)
    msg.insert(tk.END, "You : " +query)
    msg.insert(tk.END, "Chatty : " + answer)
    textF.delete(0,tk.END)
    
def userText(event):
    textF.delete(0,tk.END)
    
    
master.title("ChatBot")
master.geometry("500x900")
img=ImageTk.PhotoImage(Image.open(r"C:\Users\Arun Parmar\Desktop\images.png"))
photo=tk.Label(master, image=img,width=220,height=180)
photo.grid(column=1,row=1)
photo.pack(pady=10)
master.configure(bg='lightgrey')
frame=tk.Frame(master)
sc=tk.Scrollbar(frame)
msg=tk.Listbox(frame, width=80, height=25,fg='white')
msg.configure(bg='black')
sc.pack(side=tk.RIGHT, fill=tk.Y)
msg.pack(side=tk.LEFT, fill=tk.BOTH, pady=10)
frame.pack()
textF=tk.Entry(master, font=("Verdana", 12),fg='dimgrey',bg="#E0FFFF",width=25)
textF.insert(1,"Start conversation here")
textF.bind("<Button>",userText)
textF.pack(pady=20)
button =tk.Button(master,
                   text="CLICK",
                   fg="blue",
                   command=ask)
button.pack()
master.mainloop()
