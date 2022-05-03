import tkinter as tk
from tkinter import ttk
from tkinter import  filedialog

def add_task():
    if task.get() != "":
        task_treeview.insert(parent="", index="end", values=(task.get().replace(" ", "\ ")))
        task_entry.delete(0, tk.END)
    else:
        print("Bitte einen Task eingeben...")

def remove_task():
    selected_item = task_treeview.selection()
    if selected_item != ():
        task_treeview.delete(selected_item)
    else:
        print("Bitte einen Task markieren..")

def save_file():
    file_name = filedialog.asksaveasfilename(defaultextension=(".txt"), initialdir="C:\\Users\\Nutzer\\Desktop\\To-do-Listen-App", title="Datei speichern")
    if file_name:
        file = open(file_name, "w")
        for line in task_treeview.get_children():
            for value in task_treeview.item(line)["values"]:
                file.write(value + "\n")
        file.close()

def open_file():
   file_name = filedialog.askopenfilename(initialdir="C:\\Users\\Nutzer\\Desktop\\To-do-Listen-App", title="Datei öffnen")
   if file_name:
       file = open(file_name, "r")
       for line in file.readlines():
            task_treeview.insert(parent="", index="end", values=(line.replace(" ", "\ ")))
       file.close()

root = tk.Tk()
root.title("To-Do-Liste")
root.geometry("600x390")
root.configure(bg="#00ff00")
root.columnconfigure(0, weight=1)

task = tk.StringVar()

# Frames
user_input_frame = ttk.Frame(root)
user_input_frame.grid(row=0, column=0, pady=20)
task_frame = ttk.Frame(root)
task_frame.grid(row=1, column=0, pady=10)

# Widgets für user_input_frame
task_label = ttk.Label(user_input_frame, text="Task: ")
task_label.grid(row=0, column=0)
task_entry = ttk.Entry(user_input_frame, width=90, textvariable=task)
task_entry.grid(row=0, column=1)

add_task_button = ttk.Button(user_input_frame, text="Task hinzufügen", command=add_task)
add_task_button.grid(row=1, column=0, columnspan=2, sticky="EW", pady=2)

# Widgets für task_frame
task_treeview = ttk.Treeview(task_frame, selectmode="browse")    # "browse", damit nur ein Punkt gleichzeitig ausgewählt werden kann
task_treeview.grid(row=0, column=0, sticky="EW")

#Spalten definieren und konfigurieren
task_treeview.configure(columns=("task"))
task_treeview.column("#0", width=0, stretch=tk.NO)  # Trick, um die sonst immer vorhandene 1.Spalte verschwinden zu lassen
task_treeview.heading("task", text="Tasks")
task_treeview.column("task", width=575)

# Scrollbar für Treeview Widget erzeugen und an task_treeview binden
task_treeview_scroll = ttk.Scrollbar(task_frame, orient="vertical", command=task_treeview.yview)
task_treeview_scroll.grid(row=0, column=1, sticky="NS")
task_treeview.configure(yscrollcommand=task_treeview_scroll.set)

delete_task_button = ttk.Button(task_frame, text="Markierten Text entfernen", command=remove_task)
delete_task_button.grid(row=1, column=0, columnspan=2, stick="EW")

# Menü mit Speichermechanismus
application_menu = tk.Menu(root)
root.configure(menu=application_menu)

file_menu = tk.Menu(application_menu)
file_menu.add_command(label="Datei speichern", command=save_file)
file_menu.add_command(label="Datei öffnen", command=open_file)

application_menu.add_cascade(label="Datei", menu=file_menu)


root.mainloop()
