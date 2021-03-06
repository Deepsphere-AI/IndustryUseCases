import tkinter as tk
from tkinter import *
import DSAI_KB
# from DSAI_Utility import *
vAR_obj = DSAI_KB.Chatbot()

def chatbot_response(msg):
    s = vAR_obj.respond(msg)
    return s

def send_message():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, "You: " + msg + '\n\n') 
    # change font 
    ChatLog.config(foreground="#442265", font=("Verdana", 12))

    res = chatbot_response(msg) #get response for the input message
    ChatLog.insert(END, "Jothi: " + res + '\n\n') #display response message in the chatlog

    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)

if __name__=="__main__":
    # model, intents, words, classes = load_dependencies()

    base = tk.Tk() #creates tinker object
    base.title("Jothi - DeepSphere's Chatbot") #window title
    base.geometry("800x530") #window dimension
    base.resizable(width=FALSE, height=FALSE) #window is not resizable

    #Create Chat window
    ChatLog = Text(base, bd=0, bg="white", height="8", width="100", font="Arial")
    ChatLog.config(state=DISABLED)

    #Bind scrollbar to Chat window
    scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
    ChatLog['yscrollcommand'] = scrollbar.set

    #Create Button to send message
    SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                        bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                        command= send_message) #send function is event loop

    #Create the box to enter message
    EntryBox = Text(base, bd=0, bg="white", width="60", height="5", font="Arial")

    #Place all components on the screen
    scrollbar.place(x=784, y=6, height=386)
    ChatLog.place(x=6, y=6, height=386, width=780)
    EntryBox.place(x=128, y=401, height=90, width=680)
    SendButton.place(x=6, y=401, height=90)

    btn = Button(base, text='Quit!', command=base.destroy)
    # Button(base, text="Quit", command=base.destroy).pack()
    btn.pack(side='bottom')

    ChatLog.config(state = NORMAL)
    ChatLog.insert(END, "Jothi: " + chatbot_response('hi') + '\n\n')
    ChatLog.config(foreground="#442265", font=("Verdana", 12))
    ChatLog.config(state=DISABLED)
    base.mainloop()