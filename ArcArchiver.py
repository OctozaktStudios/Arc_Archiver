import tkinter as tk
from tkinter import filedialog
import tarfile
import os

def compress_files(input_files, output_file):
    with tarfile.open(output_file, 'w') as tar:
        for file in input_files:
            tar.add(file)
    status_label.config(text="Files archived successfully.")

def extract_files(input_file):
    with tarfile.open(input_file, 'r') as tar:
        tar.extractall()
    status_label.config(text="Files extracted successfully.")

def browse_archive():
    input_file = filedialog.askopenfilename(filetypes=[("Archive Files", "*.arc")])
    if input_file:
        with tarfile.open(input_file, 'r') as tar:
            file_list = tar.getnames()
            status_label.config(text="Files in the archive:")
            for file in file_list:
                file_label = tk.Label(root, text=file)
                file_label.pack()

def archive_files():
    input_files = filedialog.askopenfilenames()
    if input_files:
        output_file = filedialog.asksaveasfilename(defaultextension=".arc", filetypes=[("Archive Files", "*.arc")])
        if output_file:
            compress_files(input_files, output_file)

def extract_archive():
    input_file = filedialog.askopenfilename(filetypes=[("Archive Files", "*.arc")])
    if input_file:
        extract_files(input_file)

root = tk.Tk()
root.title("Archive Utility")

compress_button = tk.Button(root, text="Archive Files", command=archive_files)
compress_button.pack()

extract_button = tk.Button(root, text="Extract Files", command=extract_archive)
extract_button.pack()

browse_button = tk.Button(root, text="Browse Archive", command=browse_archive)
browse_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
