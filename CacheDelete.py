import os
import shutil
from tkinter import Tk, Button, Label, messagebox, filedialog

# Path to the file that stores the last selected root folder
CONFIG_FILE = "last_used_folder.txt"

# Function to load the last saved root folder path from a file
def load_last_folder():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            folder = file.readline().strip()
            if os.path.exists(folder):
                return folder
    return None

# Function to save the selected root folder path to a file
def save_folder_path(path):
    with open(CONFIG_FILE, "w") as file:
        file.write(path)

# Function to delete CacheClip folder
def delete_cacheclip():
    # Try to load the last used root folder
    root_folder = load_last_folder()

    # If no valid saved folder, ask the user to choose a root folder
    if not root_folder:
        root_folder = filedialog.askdirectory(title="Select Root Folder")
        if root_folder:
            save_folder_path(root_folder)  # Save the root folder path

    if root_folder:
        cacheclip_folder = os.path.join(root_folder, "CacheClip")
        
        # Check if the CacheClip folder exists and delete it
        if os.path.exists(cacheclip_folder):
            try:
                shutil.rmtree(cacheclip_folder)
                messagebox.showinfo("Success", "CacheClip folder deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "CacheClip folder not found.")
    else:
        messagebox.showwarning("Warning", "No folder selected.")

# Create the main window
root = Tk()
root.title("Delete CacheClip Folder")

# Add a label
label = Label(root, text="Click the button to delete the CacheClip folder (auto-detect in last used root folder).")
label.pack(pady=10)

# Add the button to delete the folder
delete_button = Button(root, text="Delete CacheClip", command=delete_cacheclip)
delete_button.pack(pady=20)

# Run the application
root.geometry("400x150")
root.mainloop()
