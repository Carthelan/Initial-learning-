import hashlib
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


hash_key = "5ac152b6f8bdb8bb12959548d542cb237c4a730064bf88bbb8dd6e204912baad"


def encryptPassword():
    password = entryPassword.get()
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    # Convert the password to bytes and hash it
    hash_object.update(password.encode())
    # Get the hex digest of the hash
    hash_password = hash_object.hexdigest()
    print(hash_key)
    print(hash_password)
    if(hash_password == hash_key):
        new_text = "Logged In"
        loggedInLabel.config(text=new_text)
        data_frame.pack()
    else: 
        pass
        
    


def getList():
    websites = []
    
    with open("passwords.txt", 'r') as f:
        try:
            entries = []
            for k in f:
                entries.append(k)
            entryLength = len(entries)

            infoList.config(state='normal')
            i = 0
            for entry in entries:
                if (i >= entryLength):
                    break
                websites.append({})
                entryArray = entry.split("#")
                websites[i]["website"] = entryArray[0]
                websites[i]["username"] = entryArray[1]
                websites[i]["password"] = entryArray[2]

                websiteString: str = entryArray[0] + ' ' + entryArray[1] + ' ' + entryArray[2]
                infoList.insert(tk.END, websiteString)
                i += 1
            infoList.config(state='disabled')
        except:
            infoList.config(state='disabled')
            print("no passwords")



if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("720x576")
    app.title("Password Manager")
    
    login_frame = tk.Frame(app)
    login_frame.pack()
    data_frame = tk.Frame(app)
    data_frame.pack_forget()

    # Login Frame
    labelPassword = tk.Label(login_frame, text="PASSWORD:")
    labelPassword.grid(row=1, column=1, padx=10, pady=5)
    
    entryPassword = tk.Entry(login_frame)
    entryPassword.grid(row=1, column=2, padx=10, pady=5)

    buttonPassword = tk.Button(login_frame, text="Submit Password", command=encryptPassword, )
    buttonPassword.grid(row=1, column = 3, padx=10, pady=5)
    
    loggedInLabel = tk.Label(login_frame, text="Not logged in")
    loggedInLabel.grid(row=0, column=1, padx=10, pady=5)
    
    
    
    # Data Frame
    buttonList = tk.Button(data_frame, text="List", command=getList)
    buttonList.grid(row=2, column=2, padx=15, pady=8, sticky="we")
    
    infoList = ScrolledText(data_frame, wrap=tk.WORD, state='disabled', width= 60, height = 10) 
    infoList.grid(row=3, column=2, padx=15, pady=8)
    
    

    app.mainloop()