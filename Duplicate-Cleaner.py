import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import font as tkfont

def update_results():
    input_text = text_input.get("1.0", tk.END).strip()
    nomor_list = [n.strip() for n in input_text.split('\n') if n.strip()]
    
    if not nomor_list:
        # Clear all outputs if input is empty
        text_output.delete("1.0", tk.END)
        text_duplikat.delete("1.0", tk.END)
        label_hasil.config(text="Hasil: 0 item")
        label_info.config(text="✔ Data sudah unik", fg="#388e3c")
        return
    
    # Process duplicates
    nomor_unik = []
    nomor_duplikat = []
    
    for nomor in nomor_list:
        if nomor not in nomor_unik:
            nomor_unik.append(nomor)
        else:
            nomor_duplikat.append(nomor)
    
    total_output = len(nomor_unik)
    
    # Update output
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", "\n".join(sorted(nomor_unik)))
    label_hasil.config(text=f"Hasil: {total_output} item (Tanpa duplikat)")
    
    text_duplikat.delete("1.0", tk.END)
    if nomor_duplikat:
        text_duplikat.insert("1.0", "\n".join(sorted(nomor_duplikat)))
        label_info.config(text=f"♻ {len(nomor_duplikat)} duplikat dihapus", fg="#d32f2f")
    else:
        text_duplikat.insert("1.0", "✔ Tidak ada duplikat")
        label_info.config(text="✔ Data sudah unik", fg="#388e3c")

def update_column1_counter(event=None):
    column1_text = text_input.get("1.0", tk.END).strip()
    column1_items = [n.strip() for n in column1_text.split('\n') if n.strip()]
    label_total_input.config(text=f"Total: {len(column1_items)} item")

def update_column2_counter(event=None):
    column2_text = text_column2.get("1.0", tk.END).strip()
    column2_items = [n.strip() for n in column2_text.split('\n') if n.strip()]
    label_total_column2.config(text=f"Total: {len(column2_items)} item")

def remove_from_column1():
    column1_text = text_input.get("1.0", tk.END).strip()
    column2_text = text_column2.get("1.0", tk.END).strip()
    
    column1_items = [n.strip() for n in column1_text.split('\n') if n.strip()]
    column2_items = [n.strip() for n in column2_text.split('\n') if n.strip()]
    
    if not column1_items:
        messagebox.showwarning("Peringatan", "Kolom 1 kosong!")
        return
    
    # Remove items from column1 that exist in column2
    result_items = [item for item in column1_items if item not in column2_items]
    removed_items = [item for item in column1_items if item in column2_items]
    
    # Update clean results
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", "\n".join(sorted(result_items)))
    label_hasil.config(text=f"Hasil: {len(result_items)} item (Setelah hapus dari Kolom 2)")
    
    # Update duplicates section
    text_duplikat.delete("1.0", tk.END)
    if removed_items:
        text_duplikat.insert("1.0", "\n".join(sorted(removed_items)))
        label_info.config(text=f"♻ {len(removed_items)} item dihapus karena ada di Kolom 2", fg="#d32f2f")
    else:
        text_duplikat.insert("1.0", "✔ Tidak ada item yang dihapus")
        label_info.config(text="✔ Tidak ada item yang dihapus", fg="#388e3c")

def clear_all():
    text_input.delete("1.0", tk.END)
    text_column2.delete("1.0", tk.END)
    text_output.delete("1.0", tk.END)
    text_duplikat.delete("1.0", tk.END)
    label_total_input.config(text="Total: 0 item")
    label_total_column2.config(text="Total: 0 item")
    label_hasil.config(text="Hasil: 0 item")
    label_info.config(text="✔ Tidak ada item yang dihapus", fg="#388e3c")

# GUI Setup
app = tk.Tk()
app.title("Duplikat Cleaner")
app.geometry("400x700")
app.resizable(False, False)

# Style Configuration
bg_color = "#f5f5f5"
accent_color = "#1976d2"
app.configure(bg=bg_color)

# Custom Font
default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=9)
text_font = ('Consolas', 9)

# Header
header = tk.Frame(app, bg=accent_color, height=40)
header.pack(fill=tk.X)
tk.Label(header, text="DUPLIKAT CLEANER", bg=accent_color, fg="white", 
         font=('Arial', 11, 'bold')).pack(pady=8)

# Main Container - Vertical Layout
main_frame = tk.Frame(app, bg=bg_color, padx=10, pady=10)
main_frame.pack(fill=tk.BOTH, expand=True)

# Input Section - Column 1
input_header = tk.Frame(main_frame, bg=bg_color)
input_header.pack(fill=tk.X)
tk.Label(input_header, text="Data Utama", bg=bg_color, fg=accent_color, 
         font=('Arial', 9, 'bold')).pack(side=tk.LEFT)
label_total_input = tk.Label(input_header, text="Total: 0 item", bg=bg_color, 
                            font=('Arial', 8), fg="#616161")
label_total_input.pack(side=tk.RIGHT)

text_input = scrolledtext.ScrolledText(main_frame, height=10, font=text_font, 
                                     bd=0, relief=tk.FLAT, padx=5, pady=5,
                                     highlightbackground="#e0e0e0", highlightthickness=1)
text_input.pack(fill=tk.BOTH, pady=(0, 10))

# Input Section - Column 2
column2_header = tk.Frame(main_frame, bg=bg_color)
column2_header.pack(fill=tk.X)
tk.Label(column2_header, text="Data Pembanding", bg=bg_color, fg="#d32f2f", 
         font=('Arial', 9, 'bold')).pack(side=tk.LEFT)
label_total_column2 = tk.Label(column2_header, text="Total: 0 item", bg=bg_color, 
                             font=('Arial', 8), fg="#616161")
label_total_column2.pack(side=tk.RIGHT)

text_column2 = scrolledtext.ScrolledText(main_frame, height=5, font=text_font, 
                                       bd=0, relief=tk.FLAT, padx=5, pady=5,
                                       highlightbackground="#e0e0e0", highlightthickness=1)
text_column2.pack(fill=tk.BOTH, pady=(0, 10))

# Button Frame
button_frame = tk.Frame(main_frame, bg=bg_color)
button_frame.pack(fill=tk.X, pady=5)

# Remove Duplicates Button
remove_dup_button = tk.Button(button_frame, text="Hapus Duplikat", 
                             command=update_results, bg="#1976d2", fg="white",
                             font=('Arial', 9, 'bold'), bd=0)
remove_dup_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

# Remove from Column 2 Button
remove_col2_button = tk.Button(button_frame, text="Hapus Item yang Ada di Kolom 2", 
                              command=remove_from_column1, bg="#d32f2f", fg="white",
                              font=('Arial', 9, 'bold'), bd=0)
remove_col2_button.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))

# Clear Button
clear_button = tk.Button(main_frame, text="Clear All", 
                        command=clear_all, bg="#616161", fg="white",
                        font=('Arial', 9, 'bold'), bd=0)
clear_button.pack(fill=tk.X, pady=5)

# Output Section
# Clean Results
clean_header = tk.Frame(main_frame, bg=bg_color)
clean_header.pack(fill=tk.X)
tk.Label(clean_header, text="Hasil Bersih", bg=bg_color, fg="#388e3c", 
         font=('Arial', 9, 'bold')).pack(side=tk.LEFT)
label_hasil = tk.Label(clean_header, text="Hasil: 0 item", bg=bg_color, 
                      font=('Arial', 8), fg="#616161")
label_hasil.pack(side=tk.RIGHT)

text_output = scrolledtext.ScrolledText(main_frame, height=8, font=text_font, 
                                      bg="#e8f5e9", bd=0, relief=tk.FLAT, padx=5, pady=5,
                                      highlightbackground="#e0e0e0", highlightthickness=1)
text_output.pack(fill=tk.BOTH, pady=(0, 10))

# Duplicates
dup_header = tk.Frame(main_frame, bg=bg_color)
dup_header.pack(fill=tk.X)
tk.Label(dup_header, text="Item yang Dihapus", bg=bg_color, fg="#d32f2f", 
         font=('Arial', 9, 'bold')).pack(side=tk.LEFT)
label_info = tk.Label(dup_header, text="✔ Tidak ada item yang dihapus", bg=bg_color, 
                     font=('Arial', 8), fg="#616161")
label_info.pack(side=tk.RIGHT)

text_duplikat = scrolledtext.ScrolledText(main_frame, height=5, font=text_font, 
                                         bg="#ffebee", bd=0, relief=tk.FLAT, padx=5, pady=5,
                                         highlightbackground="#e0e0e0", highlightthickness=1)
text_duplikat.pack(fill=tk.BOTH)

# Bind events for realtime counters
text_input.bind("<KeyRelease>", update_column1_counter)
text_input.bind("<ButtonRelease>", update_column1_counter)
text_column2.bind("<KeyRelease>", update_column2_counter)
text_column2.bind("<ButtonRelease>", update_column2_counter)

app.mainloop()