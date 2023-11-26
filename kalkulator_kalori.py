import tkinter as tk

def hitung_kalori():
    total_kalori = 0
    total_kalori += int(entry_makanan1.get()) if entry_makanan1.get().isdigit() else 0
    total_kalori += int(entry_makanan2.get()) if entry_makanan2.get().isdigit() else 0
    total_kalori += int(entry_makanan3.get()) if entry_makanan3.get().isdigit() else 0

    label_hasil.config(text=f"Total Kalori: {total_kalori}")

root = tk.Tk()
root.title("Penghitung Kalori Makanan")
root.geometry("400x470")


label_judul = tk.Label(root, text="Aplikasi Penghitung Kalori", font=("Helvetica", 20))
label_judul.pack(pady=10)

label_makanan1 = tk.Label(root, text="Makanan 1:")
label_makanan1.pack()
entry_makanan1 = tk.Entry(root, font=("Helvetica", 16))
entry_makanan1.pack()

label_makanan2 = tk.Label(root, text="Makanan 2:")
label_makanan2.pack()
entry_makanan2 = tk.Entry(root, font=("Helvetica", 16))
entry_makanan2.pack()

label_makanan3 = tk.Label(root, text="Makanan 3:")
label_makanan3.pack()
entry_makanan3 = tk.Entry(root, font=("Helvetica", 16))
entry_makanan3.pack()

button_hitung = tk.Button(root, text="Hitung Kalori", command=hitung_kalori, font=("Helvetica", 16))
button_hitung.pack(pady=10)

label_hasil = tk.Label(root, text="Total Kalori: 0", font=("Helvetica", 18))
label_hasil.pack(pady=10)

root.mainloop()
