import tkinter as tk
from tkinter import ttk, filedialog
import ctypes
import sys
import win32gui
import win32con
import win32api
import win32process
import psutil
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter
import numpy as np
import cv2
import win32event

# ============= CONFIGURABLE BASE ADDRESSES =============
# Replace these addresses with your game's actual addresses
BASE_ADDRESSES = {
    # Player Stats
    "health": 0x00000000,      # Health address
    "armor": 0x00000000,       # Armor address
    "ammo": 0x00000000,        # Ammo address
    "money": 0x00000000,       # Money address
    "score": 0x00000000,       # Score address
    
    # Weapons
    "weapons": 0x00000000,     # Weapons list address
    "current_weapon": 0x00000000,  # Current weapon address
    
    # Movement
    "speed": 0x00000000,       # Movement speed address
    "jump": 0x00000000,        # Jump height address
    
    # Misc
    "god_mode": 0x00000000,    # God mode address
    "no_clip": 0x00000000,     # No clip address
    "invisibility": 0x00000000 # Invisibility address
}

# ============= WEAPON LIST =============
# Add or modify weapons as needed
WEAPONS = {
    "Pistol": 0x00000001,
    "Shotgun": 0x00000002,
    "SMG": 0x00000003,
    "Rifle": 0x00000004,
    "Sniper": 0x00000005,
    "RPG": 0x00000006,
    "Grenade": 0x00000007,
    "Knife": 0x00000008
}

# ============= FEATURE CATEGORIES =============
FEATURE_CATEGORIES = {
    "Player Stats": {
        "health": "Unlimited Health",
        "armor": "Unlimited Armor",
        "ammo": "Unlimited Ammo",
        "money": "Unlimited Money",
        "score": "Max Score"
    },
    "Weapons": {
        "weapons": "Unlock All Weapons",
        "current_weapon": "Current Weapon"
    },
    "Movement": {
        "speed": "Speed Hack",
        "jump": "Super Jump",
        "no_clip": "No Clip"
    },
    "Misc": {
        "god_mode": "God Mode",
        "invisibility": "Invisibility"
    }
}

class BlurredBackground(tk.Canvas):
    def __init__(self, parent, blur_amount=5):
        super().__init__(parent)
        self.blur_amount = blur_amount
        self.bind('<Configure>', self._on_resize)
        
    def _on_resize(self, event):
        # Create a new image with the window size
        width = event.width
        height = event.height
        
        # Create a gradient background
        image = np.zeros((height, width, 3), dtype=np.uint8)
        for i in range(height):
            color = int(255 * (1 - i/height))  # Gradient from dark to darker
            image[i, :] = [color//3, color//3, color//3]  # Dark gray gradient
            
        # Apply blur
        blurred = cv2.GaussianBlur(image, (self.blur_amount*2+1, self.blur_amount*2+1), 0)
        
        # Convert to PhotoImage
        self.background = ImageTk.PhotoImage(image=Image.fromarray(blurred))
        
        # Update canvas
        self.delete("background")
        self.create_image(0, 0, image=self.background, anchor="nw", tags="background")
        self.tag_lower("background")

class EnhancedModMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ZSCY Mod Menu")
        self.root.geometry("900x700")
        
        # Initialize states and dictionaries
        self.selected_process = None
        self.feature_states = {feature: False for feature in BASE_ADDRESSES.keys()}
        self.feature_buttons = {}  # Initialize feature_buttons dictionary
        
        # Create blurred background
        self.background = BlurredBackground(self.root)
        self.background.pack(fill='both', expand=True)
        
        # Create main frame with transparency
        self.main_frame = tk.Frame(self.background, bg='#1a1a1a')
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Title with custom styling
        title_label = tk.Label(
            self.main_frame,
            text="ZSCY",
            font=("Arial", 24, "bold"),
            fg="#00ff00",
            bg='#1a1a1a'
        )
        title_label.pack(pady=20)
        
        # Process selection frame
        self.process_frame = tk.Frame(self.main_frame, bg='#1a1a1a')
        self.process_frame.pack(fill='x', pady=10)
        
        # Process selection button
        self.process_btn = self.create_button("Select Game Process", self.select_process)
        self.process_btn.pack(pady=5)
        
        # Selected process label
        self.process_label = tk.Label(
            self.process_frame,
            text="No process selected",
            fg="#ff0000",
            bg='#1a1a1a',
            font=("Arial", 10)
        )
        self.process_label.pack(pady=5)
        
        # Create category tabs
        self.create_category_tabs()
        
    def create_category_tabs(self):
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Style the notebook
        style = ttk.Style()
        style.configure("TNotebook", background='#1a1a1a')
        style.configure("TNotebook.Tab", background='#333333', foreground='white', padding=[10, 5])
        style.map("TNotebook.Tab", background=[("selected", "#00ff00")], foreground=[("selected", "black")])
        
        # Create tabs for each category
        for category_name, features in FEATURE_CATEGORIES.items():
            tab = tk.Frame(self.notebook, bg='#1a1a1a')
            self.notebook.add(tab, text=category_name)
            
            # Create feature buttons for this category
            for feature_id, feature_name in features.items():
                btn = self.create_button(feature_name, lambda f=feature_id: self.toggle_feature(f), tab)
                self.feature_buttons[feature_id] = btn
            
            # Add weapon buttons to Weapons tab
            if category_name == "Weapons":
                # Add separator
                separator = tk.Frame(tab, height=2, bg='#333333')
                separator.pack(fill='x', pady=10)
                
                # Add weapon label
                weapon_label = tk.Label(
                    tab,
                    text="Add Individual Weapons",
                    font=("Arial", 12, "bold"),
                    fg="#00ff00",
                    bg='#1a1a1a'
                )
                weapon_label.pack(pady=5)
                
                # Add weapon buttons
                for weapon_name in WEAPONS.keys():
                    self.create_button(f"Add {weapon_name}", lambda w=weapon_name: self.add_weapon(w), tab)
        
    def create_button(self, text, command, parent=None):
        if parent is None:
            parent = self.main_frame
            
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 10),
            bg='#333333',
            fg='white',
            activebackground='#00ff00',
            activeforeground='black',
            relief=tk.FLAT,
            width=15
        )
        btn.pack(pady=2)
        return btn
        
    def toggle_feature(self, feature):
        if not self.selected_process:
            messagebox.showerror("Error", "Please select a game process first!")
            return
            
        try:
            if not self.feature_states[feature]:
                # Write to memory to enable feature
                address = BASE_ADDRESSES[feature]
                # Add your memory writing code here
                self.feature_states[feature] = True
                self.feature_buttons[feature].configure(bg='#00ff00', fg='black')
                messagebox.showinfo("Success", f"{feature.replace('_', ' ').title()} enabled!")
            else:
                # Disable feature
                address = BASE_ADDRESSES[feature]
                # Add your memory writing code here
                self.feature_states[feature] = False
                self.feature_buttons[feature].configure(bg='#333333', fg='white')
                messagebox.showinfo("Success", f"{feature.replace('_', ' ').title()} disabled!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to toggle {feature}: {str(e)}")
            
    def add_weapon(self, weapon_name):
        if not self.selected_process:
            messagebox.showerror("Error", "Please select a game process first!")
            return
            
        try:
            weapon_id = WEAPONS[weapon_name]
            # Add your weapon adding code here
            messagebox.showinfo("Success", f"{weapon_name} added!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add {weapon_name}: {str(e)}")
            
    def select_process(self):
        try:
            # Get list of running processes
            processes = []
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    processes.append((proc.info['name'], proc.info['pid']))
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            # Create process selection window
            process_window = tk.Toplevel(self.root)
            process_window.title("Select Game Process")
            process_window.geometry("400x500")
            process_window.configure(bg='#1a1a1a')
            
            # Create search frame
            search_frame = tk.Frame(process_window, bg='#1a1a1a')
            search_frame.pack(fill='x', padx=10, pady=10)
            
            # Create search label
            search_label = tk.Label(
                search_frame,
                text="Search:",
                font=("Arial", 10),
                fg="white",
                bg='#1a1a1a'
            )
            search_label.pack(side='left', padx=5)
            
            # Create search entry
            search_var = tk.StringVar()
            search_entry = tk.Entry(
                search_frame,
                textvariable=search_var,
                font=("Arial", 10),
                bg='#333333',
                fg='white',
                insertbackground='white'
            )
            search_entry.pack(side='left', fill='x', expand=True, padx=5)
            
            # Create listbox with scrollbar
            frame = tk.Frame(process_window, bg='#1a1a1a')
            frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            scrollbar = tk.Scrollbar(frame)
            scrollbar.pack(side='right', fill='y')
            
            listbox = tk.Listbox(
                frame,
                bg='#333333',
                fg='white',
                selectmode='single',
                yscrollcommand=scrollbar.set
            )
            listbox.pack(side='left', fill='both', expand=True)
            
            scrollbar.config(command=listbox.yview)
            
            # Add processes to listbox
            for proc_name, proc_pid in processes:
                listbox.insert('end', f"{proc_name} (PID: {proc_pid})")
            
            # Store all processes for filtering
            all_processes = processes.copy()
            
            def filter_processes(*args):
                search_term = search_var.get().lower()
                listbox.delete(0, tk.END)
                
                for proc_name, proc_pid in all_processes:
                    if search_term in proc_name.lower():
                        listbox.insert('end', f"{proc_name} (PID: {proc_pid})")
            
            # Bind search entry to filter function
            search_var.trace('w', filter_processes)
            
            def on_select():
                if listbox.curselection():
                    index = listbox.curselection()[0]
                    filtered_processes = []
                    for proc_name, proc_pid in all_processes:
                        if search_var.get().lower() in proc_name.lower():
                            filtered_processes.append((proc_name, proc_pid))
                    
                    proc_name, proc_pid = filtered_processes[index]
                    self.selected_process = proc_pid
                    self.process_label.config(
                        text=f"Selected: {proc_name} (PID: {proc_pid})",
                        fg="#00ff00"
                    )
                    process_window.destroy()
            
            # Create button frame
            button_frame = tk.Frame(process_window, bg='#1a1a1a')
            button_frame.pack(fill='x', padx=10, pady=10)
            
            # Add select button
            select_btn = tk.Button(
                button_frame,
                text="Select",
                command=on_select,
                font=("Arial", 10),
                bg='#333333',
                fg='white',
                activebackground='#00ff00',
                activeforeground='black',
                relief=tk.FLAT,
                width=10
            )
            select_btn.pack(side='right', padx=5)
            
            # Add cancel button
            cancel_btn = tk.Button(
                button_frame,
                text="Cancel",
                command=process_window.destroy,
                font=("Arial", 10),
                bg='#333333',
                fg='white',
                activebackground='#ff0000',
                activeforeground='black',
                relief=tk.FLAT,
                width=10
            )
            cancel_btn.pack(side='right', padx=5)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get process list: {str(e)}")
    
    def inject_dll(self, process_id):
        try:
            # Get process handle
            process_handle = win32api.OpenProcess(
                win32con.PROCESS_ALL_ACCESS,
                False,
                process_id
            )
            
            # Allocate memory for DLL path
            dll_path = "path_to_your_dll.dll"  # Replace with actual DLL path
            path_bytes = (dll_path + '\0').encode('utf-8')
            path_size = len(path_bytes)
            
            # Allocate memory in target process
            remote_memory = win32process.VirtualAllocEx(
                process_handle,
                0,
                path_size,
                win32con.MEM_COMMIT | win32con.MEM_RESERVE,
                win32con.PAGE_READWRITE
            )
            
            # Write DLL path to allocated memory
            win32process.WriteProcessMemory(
                process_handle,
                remote_memory,
                path_bytes,
                path_size
            )
            
            # Get LoadLibraryA address
            kernel32 = win32api.GetModuleHandle('kernel32.dll')
            load_library = win32api.GetProcAddress(kernel32, 'LoadLibraryA')
            
            # Create remote thread to load DLL
            thread_handle = win32process.CreateRemoteThread(
                process_handle,
                None,
                0,
                load_library,
                remote_memory,
                0,
                None
            )
            
            # Wait for thread completion
            win32event.WaitForSingleObject(thread_handle, win32event.INFINITE)
            
            # Cleanup
            win32api.CloseHandle(thread_handle)
            win32process.VirtualFreeEx(process_handle, remote_memory, 0, win32con.MEM_RELEASE)
            win32api.CloseHandle(process_handle)
            
            return True
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to inject DLL: {str(e)}")
            return False
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Check if running with admin privileges
    # if not ctypes.windll.shell32.IsUserAnAdmin():
    #     messagebox.showerror("Error", "Please run this program as administrator!")
    #     sys.exit(1)
        
    menu = EnhancedModMenu()
    menu.run() 