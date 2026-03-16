import tkinter as tk
from tkinter import ttk, messagebox
import json
import re
import os

FILE="contacts.json"

# LOAD DATA

def load_contacts():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return json.load(f)
    return []

contacts = load_contacts()

def save_contacts():
    with open(FILE,"w") as f:
        json.dump(contacts,f,indent=4)

# VALIDATION

def valid_phone(phone):
    return re.match(r'^\+\d{1,3}\d{10}$', phone)

def valid_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email)

# REFRESH TABLE

def refresh_table(data=None):

    for row in table.get_children():
        table.delete(row)

    dataset = data if data else contacts

    dataset.sort(key=lambda x:x["name"].lower())

    for c in dataset:
        table.insert("",tk.END,
        values=(c["name"],c["phone"],c["email"],c["address"]))

    total_label.config(text=f"Total Contacts: {len(contacts)}")

# ADD CONTACT 

def add_contact():

    name=name_entry.get()
    phone=phone_entry.get()
    email=email_entry.get()
    address=address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Error","Name and Phone required")
        return

    if not valid_phone(phone):
        messagebox.showwarning("Phone Format","Use +911234567890")
        return

    if email and not valid_email(email):
        messagebox.showwarning("Email","Enter valid Gmail")
        return

    contacts.append({
        "name":name,
        "phone":phone,
        "email":email,
        "address":address
    })

    save_contacts()
    refresh_table()
    clear_form()

# DELETE

def delete_contact():

    selected=table.selection()

    if not selected:
        return

    confirm=messagebox.askyesno("Delete","Delete this contact?")

    if confirm:
        index=table.index(selected)
        contacts.pop(index)

        save_contacts()
        refresh_table()

# EDIT

def edit_contact():

    selected=table.selection()

    if not selected:
        messagebox.showwarning("Edit","Select contact first")
        return

    index=table.index(selected)

    contact=contacts[index]

    name_entry.delete(0,tk.END)
    name_entry.insert(0,contact["name"])

    phone_entry.delete(0,tk.END)
    phone_entry.insert(0,contact["phone"])

    email_entry.delete(0,tk.END)
    email_entry.insert(0,contact["email"])

    address_entry.delete(0,tk.END)
    address_entry.insert(0,contact["address"])

    contacts.pop(index)

# SEARCH

def search(event):

    q=search_entry.get().lower()

    filtered=[]

    for c in contacts:
        if q in c["name"].lower() or q in c["phone"]:
            filtered.append(c)

    refresh_table(filtered)

# CLEAR 

def clear_form():

    name_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)

# UI 

root=tk.Tk()
root.title("Smart Contact Manager")
root.geometry("1050x600")
root.configure(bg="#f3f4f6")

# Sidebar

sidebar=tk.Frame(root,bg="#111827",width=200)
sidebar.pack(side="left",fill="y")

logo=tk.Label(sidebar,text="Contacts",
font=("Segoe UI",18,"bold"),
bg="#111827",fg="white")

logo.pack(pady=20)

total_label=tk.Label(sidebar,text="Total Contacts: 0",
bg="#111827",fg="white")

total_label.pack()

# Main

main=tk.Frame(root,bg="#f3f4f6")
main.pack(fill="both",expand=True)

title=tk.Label(main,text="Smart Contact Manager",
font=("Segoe UI",24,"bold"),
bg="#f3f4f6")

title.pack(pady=10)

# Form

form=tk.Frame(main,bg="white",bd=1,relief="solid")
form.pack(pady=10,padx=20)

tk.Label(form,text="Name",bg="white").grid(row=0,column=0,padx=10,pady=5)
tk.Label(form,text="Phone (+91)",bg="white").grid(row=1,column=0,padx=10,pady=5)
tk.Label(form,text="Email",bg="white").grid(row=2,column=0,padx=10,pady=5)
tk.Label(form,text="Address",bg="white").grid(row=3,column=0,padx=10,pady=5)

name_entry=tk.Entry(form,width=30)
phone_entry=tk.Entry(form,width=30)
email_entry=tk.Entry(form,width=30)
address_entry=tk.Entry(form,width=30)

name_entry.grid(row=0,column=1)
phone_entry.grid(row=1,column=1)
email_entry.grid(row=2,column=1)
address_entry.grid(row=3,column=1)

# Buttons

btn_frame=tk.Frame(main,bg="#f3f4f6")
btn_frame.pack(pady=10)

tk.Button(btn_frame,text="Add",width=10,bg="#2563eb",fg="white",command=add_contact).pack(side="left",padx=5)
tk.Button(btn_frame,text="Edit",width=10,bg="#2563eb",fg="white",command=edit_contact).pack(side="left",padx=5)
tk.Button(btn_frame,text="Delete",width=10,bg="#2563eb",fg="white",command=delete_contact).pack(side="left",padx=5)
tk.Button(btn_frame,text="Clear",width=10,bg="#2563eb",fg="white",command=clear_form).pack(side="left",padx=5)

# Search

search_frame=tk.Frame(main,bg="#f3f4f6")
search_frame.pack()

tk.Label(search_frame,text="Search",bg="#f3f4f6").pack(side="left")

search_entry=tk.Entry(search_frame,width=30)
search_entry.pack(side="left")

search_entry.bind("<KeyRelease>",search)

# Table

columns=("Name","Phone","Email","Address")

table=ttk.Treeview(main,columns=columns,show="headings")

for col in columns:
    table.heading(col,text=col)

table.pack(fill="both",expand=True,padx=20,pady=20)

refresh_table()

root.mainloop()