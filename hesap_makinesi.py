import tkinter as tk

#Ekran Oluştur
ekran = tk.Tk()
ekran.title("PYTHON İLE HESAP MAKİNESİ")


#Giriş Oluştur
entry = tk.Entry(width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

#Komutları Oluştur
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Mevcut girişi temizle
    entry.insert(tk.END, current + value)  # Yeni değeri ekle

def button_clear():
    entry.delete(0, tk.END)  # Girişi temizle
label = tk.Label(text="Coder With : @ilahici_tg")
def button_equal():
    try:
        result = eval(entry.get())  # Hesaplama yapmak için eval fonksiyonu
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Hata")
label.place(x=250,y=550)
# Düğmeleri oluştur
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)
]

# Düğmeleri ekle
for (text, row, col, *span) in buttons:
    if text == 'C':
        button = tk.Button( text=text, width=10, height=3, font=("Arial", 18),bg="black",fg="white",activebackground="cyan", command=button_clear)
        button.grid(row=row, column=col, columnspan=2, padx=5, pady=5)
    elif text == '=':
        button = tk.Button( text=text, width=10, height=3, font=("Arial", 18),bg="black",fg="white",activebackground="cyan", command=button_equal)
        button.grid(row=row, column=col, padx=5, pady=5)
    else:
        button = tk.Button( text=text, width=5, height=3, font=("Arial", 18),bg="black",fg="white",activebackground="cyan", command=lambda val=text: button_click(val))
        button.grid(row=row, column=col, padx=5, pady=5)



ekran.mainloop()
