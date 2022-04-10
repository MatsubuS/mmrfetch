import requests
import json
import tkinter as tk
from tkinter import *
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta

#icon base64 code
icon =  "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"

#setglobal empty username
username = ""

def setusername():
    global username
    username = Usernamebox.get("1.0", "end-1c")
    mainupdate()
    
def setserver():
    pass

def mainupdate():
    try:
        headers = {
            'User-Agent': 'Windows:desktopmmrcheck:alpha',
        }
        global username
        text_box.config(state=NORMAL)
        text_box1.config(state=NORMAL)
        text_box.delete('1.0', END)
        text_box1.delete('1.0', END)
        page = requests.get("https://eune.whatismymmr.com/api/v1/summoner?name="+username, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        site_json = json.loads(soup.text)        
        aram = site_json['ARAM']['avg']
        err = site_json['ARAM']['err']
        timestamp = site_json['ARAM']['timestamp']
        procent = site_json['ARAM']['percentile']
        timestamp = site_json['ARAM']['timestamp']
        math = round(100 - procent,2)
        rank = site_json['ARAM']['closestRank']
        dt_object = datetime.fromtimestamp(timestamp)
        timenow = datetime.now()
        math2 = timenow - dt_object
        text_box.insert("end-1c", username+"'s mmr on aram is: "+str(aram)+" (+/-"+str(err)+"). top "+str(math)+"% Approximate rank: "+str(rank))
        text_box.config(state=DISABLED)
        if math2.days > 0:
            text_box1.insert("end-1c", "Last updated "+str(math2.days)+" days ago")
            text_box1.config(state=DISABLED)
        else:
            text_box1.insert("end-1c", "Last upated "+str(round(math2 / timedelta(minutes=1)))+" minutes ago")
            text_box1.config(state=DISABLED)
    except KeyError:
        text_box.insert("end-1c", "there has been some kind of an error... wrong username perhaps?")
        text_box.config(state=DISABLED)
        text_box1.insert("end-1c", "Input a valid username.")
        text_box1.config(state=DISABLED)
    except TypeError:
        text_box.insert("end-1c", "⣠⣾⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀ ⠀⣠⣾⣿⣿⣿⣿⣷⣄" +'\n'+ "⣿⣿⡇⠀⠀⢸⣿⢰⣿⡆⠀⣾⣿⡆⠀⣾⣷⠀ ⣿⣿⡇⠀⠀ ⢸⣿⣿" +'\n'+ "⣿⣿⡇⠀⠀⢸⣿⠘⣿⣿⣤⣿⣿⣿⣤⣿⡇⠀⢻⣿⡇⠀⠀ ⢸⣿⣿" +'\n'+ "⣿⣿⡇⠀⠀⢸⡿⠀⢹⣿⣿⣿⣿⣿⣿⣿⠁⠀⢸⣿⣇⠀⠀ ⢸⣿⣿" +'\n'+ "⠙⢿⣷⣶⣶⡿⠁⠀⠈⣿⣿⠟⠀⣿⣿⠇⠀⠀⠈⠻⣿⣿⣿⣿⡿⠋")
        text_box.config(state=DISABLED)
        text_box1.insert("end-1c", "no mmr data for "+str(username))
        text_box1.config(state=DISABLED)

#window configuration
root = tk.Tk()
root.title("MMR checker")
img = tk.PhotoImage(data=icon)
root.tk.call('wm', 'iconphoto', root._w, img)
root.resizable(False, False)
root.configure(bg="#C72C41")

text_box = tk.Text(root, width=35, height=4)
text_box.grid(row=1, column=0, sticky=W, pady=4)
text_box.config(state=DISABLED, bg="#801336", fg="white")

text_box1 = tk.Text(root, width=35, height=1)
text_box1.grid(row=2, column=0, sticky=W, pady=4)
text_box1.config(state=DISABLED, bg="#801336", fg="white")

Button(root, text='check mmr', command=setusername, bg="#C72C41", fg="white").grid(row=3, column=0, sticky=W, pady=1)

Usernamebox = tk.Text(root, width=15, height=1)
Usernamebox.grid(row=3,column=0,sticky=SE,pady=4,padx=4)
Usernamebox.insert(INSERT, "Username Here")
Usernamebox.config(bg="#801336", fg="white")

mainloop()
