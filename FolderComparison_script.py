import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def compare_folders(folder1, folder2):
    files1 = set([file.split('.')[0] for file in os.listdir(folder1) if os.path.isfile(os.path.join(folder1, file))])
    files2 = set([file.split('.')[0] for file in os.listdir(folder2) if os.path.isfile(os.path.join(folder2, file))])

    unique_files1 = files1 - files2
    unique_files2 = files2 - files1

    return unique_files1, unique_files2

def find_folder(button):
    folder_path = filedialog.askdirectory()
    if button == 1:
        entry_folder1.delete(0, tk.END)
        entry_folder1.insert(0, folder_path)
    else:
        entry_folder2.delete(0, tk.END)
        entry_folder2.insert(0, folder_path)

def update_output():
    folder1 = entry_folder1.get()
    folder2 = entry_folder2.get()

    if os.path.exists(folder1) and os.path.exists(folder2):
        unique_files1, unique_files2 = compare_folders(folder1, folder2)

        output1.config(state=tk.NORMAL)
        output1.delete(1.0, tk.END)
        output1.insert(tk.END, "Files unique to Folder 1:\n" + "\n".join(unique_files1))
        output1.config(state=tk.DISABLED)

        output2.config(state=tk.NORMAL)
        output2.delete(1.0, tk.END)
        output2.insert(tk.END, "Files unique to Folder 2:\n" + "\n".join(unique_files2))
        output2.config(state=tk.DISABLED)

    else:
        tk.messagebox.showerror("Error", "Invalid folder path")

# Create the main window
window = tk.Tk()
window.title("Folder Comparison Tool")

# Set the window icon
icon_path = "C:/Users/james/Desktop/Folder_Comparison_UI_Logo/logo.ico"
if os.path.exists(icon_path):
    window.iconbitmap(icon_path)

# Entry widgets for folder paths
entry_folder1 = tk.Entry(window, bg="ivory1", width=60)
entry_folder2 = tk.Entry(window, bg="ivory1", width=60)

# Buttons to find folder paths
button_folder1 = tk.Button(window, text="Folder 1", bg="ivory1", command=lambda: find_folder(1))
button_folder2 = tk.Button(window, text="Folder 2", bg="ivory1", command=lambda: find_folder(2))

# Output panels with scroll bars
output1 = tk.Text(window, height=10, width=50, state=tk.DISABLED)
output2 = tk.Text(window, height=10, width=50, state=tk.DISABLED)

scrollbar1 = tk.Scrollbar(window, command=output1.yview)
scrollbar2 = tk.Scrollbar(window, command=output2.yview)

output1.config(yscrollcommand=scrollbar1.set)
output2.config(yscrollcommand=scrollbar2.set)

# Button to trigger folder comparison
button_compare = tk.Button(window, text="Compare Folders", bg="ivory1", command=update_output)

# Arrange widgets in the window
entry_folder1.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
button_folder1.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
entry_folder2.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
button_folder2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
button_compare.grid(row=2, column=0, columnspan=2, pady=10)
output1.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
output2.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")
scrollbar1.grid(row=3, column=0, sticky="nse")
scrollbar2.grid(row=3, column=1, sticky="nse")

# Configure row and column weights to allow resizing
window.grid_rowconfigure(3, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Run the main loop
window.mainloop()
