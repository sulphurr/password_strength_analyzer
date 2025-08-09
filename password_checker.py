import math
import hashlib
import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

def calculate_entropy(password):
    pool=0
    if any(c.islower() for c in password):
        pool+=26
    if any(c.isupper() for c in password):
        pool+=26
    if any(c.isdigit() for c in password):
        pool+=10
    if any(not c.isalnum() for c in password):
        pool+=32
    entropy=len(password)*math.log2(pool) if pool else 0
    return entropy

def check_breach(password):
    try:
        sha1=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix,suffix=sha1[:5],sha1[5:]
        url=f"https://api.pwnedpasswords.com/range/{prefix}"
        res=requests.get(url)
        if res.status_code!=200:
            return None
        hashes=(line.split(':') for line in res.text.splitlines())
        for h,count in hashes:
            if h==suffix:
                return int(count)
        return 0
    except:
        return None

def suggest_improvements(password):
    suggestions=[]
    if len(password)<12:
        suggestions.append("increase length to at least 12 characters.")
    if not any(c.isupper() for c in password):
        suggestions.append("add uppercase letters.")
    if not any(c.islower() for c in password):
        suggestions.append("add lowercase letters.")
    if not any(c.isdigit() for c in password):
        suggestions.append("add digits.")
    if not any(not c.isalnum() for c in password):
        suggestions.append("add special characters (!, @, #, etc).")
    return suggestions

def analyze_password():
    password=password_entry.get()
    if not password:
        messagebox.showwarning("input error","please enter a password.")
        return
    
    entropy=calculate_entropy(password)
    breaches=check_breach(password)

    # readability fixed
    if entropy<40:
        strength="weak :0"
        color="#8B0000"  #darker
    elif entropy<60:
        strength="moderate :)"
        color="#CC5500"  
    else:
        strength="strong ;3"
        color="#006400"  

    result_text.delete("1.0",tk.END)
    result_text.insert(tk.END,f"password strength: {strength}\n",("color",))
    result_text.tag_config("color",foreground=color,font=("Arial",14,"bold"))

    if breaches is not None:
        if breaches>0:
            result_text.insert(tk.END,f"found in {breaches} known breaches.\n",("breach",))
            result_text.tag_config("breach",foreground="#8B0000",font=("Arial",12,"bold"))
        else:
            result_text.insert(tk.END,"not found in known breaches.\n",("safe",))
            result_text.tag_config("safe",foreground="#006400",font=("Arial",12,"bold"))
    else:
        result_text.insert(tk.END,"could not check breach database.\n",("warn",))
        result_text.tag_config("warn",foreground="#CC5500",font=("Arial",12,"bold"))

    suggestions=suggest_improvements(password)
    if suggestions:
        result_text.insert(tk.END,"\nsuggestions to improve password:\n",("title",))
        result_text.tag_config("title",font=("Arial",12,"bold"))
        for s in suggestions:
            result_text.insert(tk.END,f"- {s}\n",("suggest",))
        result_text.tag_config("suggest",font=("Arial",11))


dusty_pink="#D8A7B1"

root=tk.Tk()
root.title("password strength analyzer")
root.geometry("520x450")
root.config(bg=dusty_pink) 

title_label=tk.Label(root,text="password strength analyzer",font=("Arial",18,"bold"),bg=dusty_pink,fg="white")
title_label.pack(pady=10)

password_entry=tk.Entry(root,show="*",font=("Arial",16),width=30,bg="#EBC3CB",fg="black",insertbackground="black")
password_entry.pack(pady=10)
password_entry.bind("<Return>",lambda event: analyze_password()) #error 1

analyze_button=tk.Button(root,text="analyze password",font=("Arial",14,"bold"),bg="#C86B85",fg="white",command=analyze_password)
analyze_button.pack(pady=10)

result_text=scrolledtext.ScrolledText(root,wrap=tk.WORD,font=("Arial",12),width=55,height=12,bg="#EBC3CB",fg="black",insertbackground="black")
result_text.pack(pady=10)

root.mainloop()
