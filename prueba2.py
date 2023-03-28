import os
import subprocess
import tkinter as tk

class FileExplorer:
    def __init__(self, master):
        self.current_directory = "/"
        self.master = master
        self.location_label = tk.Label(master, text=self.current_directory)
        self.location_label.pack()
        
        self.listbox = tk.Listbox(master, width=50, height=20)
        self.listbox.pack()
        self.listbox.bind("<Double-Button-1>", self.on_folder_selected)
        
        self.refresh_listbox()

    def refresh_listbox(self):
        # Clear the listbox
        self.listbox.delete(0, tk.END)

        # Update the location label
        self.location_label.config(text=self.current_directory)
        
        # Add ".." folder to navigate back to parent folder
        self.listbox.insert(tk.END, "..")
        self.listbox.itemconfig(tk.END, {'fg': 'blue'})
        
        # Add the folders to the listbox with a different color
        cmd = ["adb", "shell", "ls", "-1", "-p", self.current_directory]
        output = subprocess.check_output(cmd).decode('utf-8').splitlines()
        for item in output:
            if item.endswith("/"):
                self.listbox.insert(tk.END, item)
                self.listbox.itemconfig(tk.END, {'fg': 'blue'})
            if not item.endswith("/"):
                self.listbox.insert(tk.END, item)

    def on_folder_selected(self, event):
        # Get the selected item from the listbox
        selection = self.listbox.get(self.listbox.curselection()[0])
        print(selection)
        if selection:
            # Check if the selected item is a folder and navigate to it
            if selection == "..":
                cmd = ["adb", "shell", "echo ", "$(cd " + self.current_directory + "/../ && pwd)"]
                self.current_directory = subprocess.check_output(cmd).decode('utf-8').splitlines()[0]
                self.refresh_listbox()
            else:
                full_path = self.current_directory + "/"+ selection
                if full_path.startswith("/"):
                    self.current_directory = full_path
                    self.location_label.config(text=full_path)
                    self.refresh_listbox()
                else:
                    self.current_directory = self.current_directory + "/"+ selection
                    self.location_label.config(text=self.current_directory)
                    self.refresh_listbox()
            
if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorer(root)
    app.refresh_listbox()
    root.mainloop()
