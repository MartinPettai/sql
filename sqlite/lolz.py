import tkinter as tk
import sqlite3

# Andmebaasi ühendus
conn = sqlite3.connect('epood_mpettai.db')
c = conn.cursor()

# Tkinter akna loomine
root = tk.Tk()
root.title("Andmed andmebaasist")
root.geometry("600x400")

# Funktsioon, mis kuvab andmed
def kuvaa_andmed():
    # Kõigi andmete päring
    c.execute("SELECT * FROM mpettai")
    rows = c.fetchall()
    
    # Tabeli loomine ja täitmine andmetega
    table = tk.Label(root, text="Kõik andmed")
    table.grid(row=0, column=0, sticky="W")
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            cell = tk.Label(root, text=value)
            cell.grid(row=i+1, column=j, sticky="W")

# Nupp andmete kuvamiseks
kuvaa_button = tk.Button(root, text="Kuva andmed", command=kuvaa_andmed)
kuvaa_button.grid(row=0, column=1)

root.mainloop()

# Andmebaasiühenduse sulgemine
conn.close()

from tkinter import *
from tkinter import ttk
import sqlite3

# Ühendus andmebaasiga
conn = sqlite3.connect('epood_mpettai.db')
c = conn.cursor()

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("MPettai E-pood")
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Otsingu kast
        self.search_frame = Frame(self)
        self.search_frame.pack(side=TOP, pady=5)
        self.search_label = Label(self.search_frame, text="Otsi:")
        self.search_label.pack(side=LEFT, padx=5)
        self.search_entry = Entry(self.search_frame, width=30)
        self.search_entry.pack(side=LEFT, padx=5)
        self.search_button = Button(self.search_frame, text="Otsi", command=self.search_data)
        self.search_button.pack(side=LEFT, padx=5)

        # Tabel
        self.tree_frame = Frame(self)
        self.tree_frame.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)

        self.tree = ttk.Treeview(self.tree_frame, selectmode='browse')
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Headerid
        self.tree["columns"] = ("Nimetus", "Hind", "Kogus")
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Nimetus", width=200, minwidth=200, anchor=CENTER)
        self.tree.column("Hind", width=100, minwidth=100, anchor=CENTER)
        self.tree.column("Kogus", width=100, minwidth=100, anchor=CENTER)

        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("Nimetus", text="Nimetus", anchor=CENTER)
        self.tree.heading("Hind", text="Hind", anchor=CENTER)
        self.tree.heading("Kogus", text="Kogus", anchor=CENTER)

        # Leia andmed andmebaasist ja lisa tabelisse
        self.data = []
        c.execute("SELECT * FROM mpettai")
        for row in c.fetchall():
            self.tree.insert("", END, values=row)
            self.data.append(row)

        # Lehekülje valimise kast
        self.page_frame = Frame(self)
        self.page_frame.pack(side=TOP, pady=5)
        self.page_label = Label(self.page_frame, text="Ridu leheküljel:")
        self.page_label.pack(side=LEFT, padx=5)
        self.page_spinbox = Spinbox(self.page_frame, from_=1, to=len(self.data), width=5, command=self.update_table)
        self.page_spinbox.pack(side=LEFT, padx=5)
        self.page_button = Button(self.page_frame, text="Lehekülg", command=self.update_table)
        self.page_button.pack(side=LEFT, padx=5)

    # Funktsioon andmete otsimiseks
    def search():
    # Kustuta eelmine tulemus
    tulemus.delete(*tulemus.get_children())
    # Otsi tekstikasti sisestatud andmeid andmebaasist ja kuvatakse tulemus puuvaates
    otsing = otsi_kast.get()
    for rida in cur.execute(f"SELECT * FROM mpettai WHERE LOWER(nimi) LIKE '%{otsing.lower()}%' OR LOWER(kategooria) LIKE '%{otsing.lower()}%'"):
        tulemus.insert("", "end", values=rida)

# Loo nupp andmete otsimiseks
otsi_nupp = Button(otsi_raam, text="Otsi", command=otsi_andmeid)
otsi_nupp.pack(side=RIGHT, padx=5, pady=5)