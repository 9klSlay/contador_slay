import tkinter as tk
from datetime import datetime

target_9k = datetime(2025, 12, 25, 6, 28)

def get_time_parts(target):
    now = datetime.now()
    remaining = target - now
    if remaining.total_seconds() <= 0:
        return (0, 0, 0, 0, 0)
    months = remaining.days // 30
    days = remaining.days % 30
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    return (months, days, hours, minutes, seconds)

def update_timer():
    parts = get_time_parts(target_9k)
    if all(v == 0 for v in parts):
        for lbl in labels_9k:
            lbl.config(text="00")
        msg_text.config(text="¡Ya volvió ")
        msg_name.config(text="9k_lSlay", fg="#b300ff")
        return
    for i, val in enumerate(parts):
        labels_9k[i].config(text=f"{val:02}")
    root.after(1000, update_timer)

def toggle_topmost():
    global topmost
    topmost = not topmost
    root.attributes("-topmost", topmost)
    if topmost:
        btn_topmost.config(text="Desactivar fijación", bg="#4d4d4d", fg="#00ff00")
    else:
        btn_topmost.config(text="Fijar ventana arriba", bg="black", fg="#00ff00")

root = tk.Tk()
root.title("Regreso de 9k_lSlay")
root.configure(bg="black")
root.geometry("700x500")
topmost = False

btn_topmost = tk.Button(
    root,
    text="Fijar ventana arriba",
    command=toggle_topmost,
    bg="black",
    fg="#00ff00",
    bd=0,
    activebackground="#222",
    activeforeground="#00ff00",
    font=("Consolas", 10, "bold")
)
btn_topmost.place(relx=1, x=-10, y=10, anchor="ne")

def crear_contador(padre, color):
    labels = []
    textos = ["Meses", "Días", "Horas", "Minutos", "Segundos"]
    frame = tk.Frame(padre, bg="black")
    frame.pack(pady=10)
    for i, texto in enumerate(textos):
        col = tk.Frame(frame, bg="black")
        col.grid(row=0, column=i, padx=10)
        num = tk.Label(col, text="00", font=("Consolas", 36, "bold"), fg=color, bg="black")
        num.pack()
        lab = tk.Label(col, text=texto, font=("Consolas", 14), fg=color, bg="black")
        lab.pack()
        labels.append(num)
    return labels

labels_9k = crear_contador(root, "#00ff00")

msg_frame = tk.Frame(root, bg="black")
msg_frame.pack(pady=10)

msg_text = tk.Label(
    msg_frame,
    text="Regreso de ",
    font=("Consolas", 18, "bold"),
    fg="#00ff00",
    bg="black"
)
msg_text.pack(side="left")

msg_name = tk.Label(
    msg_frame,
    text="9k_lSlay",
    font=("Consolas", 18, "bold"),
    fg="#b300ff", 
    bg="black"
)
msg_name.pack(side="left")

update_timer()

root.mainloop()

