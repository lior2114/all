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
import win32event

# Replace these base addresses with your game's actual addresses
BASE_ADDRESSES = {
    "health": 0x00000000,  # Replace with actual health address
    "ammo": 0x00000000,    # Replace with actual ammo address
    "weapons": 0x00000000  # Replace with actual weapons address
}

class ModMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ZSCY Mod Menu")
        self.root.geometry("400x600")
        self.root.configure(bg='#1a1a1a')
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
        # Create main frame
        self.main_frame = tk.Frame(self.root, bg='#1a1a1a')
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title with custom styling
        title_label = tk.Label(
            self.main_frame,
            text="ZSYC",
            font=("Arial", 24, "bold"),
            fg="#00ff00",
            bg='#1a1a1a'
        )
        title_label.pack(pady=20)
        
        # Process selection frame
        self.process_frame = tk.Frame(self.main_frame, bg='#1a1a1a')
        self.process_frame.pack(fill='x', pady=10)
        
        # Process selection button
        self.process_btn = tk.Button(
            self.process_frame,
            text="Select Game Process",
            command=self.select_process,
            font=("Arial", 12),
            bg='#333333',
            fg='white',
            activebackground='#00ff00',
            activeforeground='black',
            relief=tk.FLAT,
            width=20,
            height=2
        )
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
        
        # Initialize states
        self.health_active = False
        self.ammo_active = False
        self.weapons_active = False
        self.selected_process = None
        
        # Create buttons with modern styling
        self.health_btn = self.create_button("Unlimited Health", self.toggle_health)
        self.ammo_btn = self.create_button("Unlimited Ammo", self.toggle_ammo)
        self.weapons_btn = self.create_button("Open All Weapons", self.toggle_weapons)
        
    def create_button(self, text, command):
        btn = tk.Button(
            self.main_frame,
            text=text,
            command=command,
            font=("Arial", 12),
            bg='#333333',
            fg='white',
            activebackground='#00ff00',
            activeforeground='black',
            relief=tk.FLAT,
            width=20,
            height=2
        )
        btn.pack(pady=10)
        return btn
        
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
            process_window.geometry("300x400")
            process_window.configure(bg='#1a1a1a')
            
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
            
            def on_select():
                if listbox.curselection():
                    index = listbox.curselection()[0]
                    proc_name, proc_pid = processes[index]
                    self.selected_process = proc_pid
                    self.process_label.config(
                        text=f"Selected: {proc_name} (PID: {proc_pid})",
                        fg="#00ff00"
                    )
                    process_window.destroy()
            
            # Add select button
            select_btn = tk.Button(
                process_window,
                text="Select",
                command=on_select,
                font=("Arial", 10),
                bg='#333333',
                fg='white',
                activebackground='#00ff00',
                activeforeground='black',
                relief=tk.FLAT
            )
            select_btn.pack(pady=10)
            
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
        
    def toggle_health(self):
        if not self.selected_process:
            messagebox.showerror("Error", "Please select a game process first!")
            return
            
        try:
            if not self.health_active:
                # Write to memory to enable unlimited health
                # Replace with actual memory writing code
                self.health_btn.configure(bg='#00ff00', fg='black')
            else:
                # Disable unlimited health
                self.health_btn.configure(bg='#333333', fg='white')
            self.health_active = not self.health_active
        except Exception as e:
            messagebox.showerror("Error", f"Failed to toggle health: {str(e)}")
            
    def toggle_ammo(self):
        if not self.selected_process:
            messagebox.showerror("Error", "Please select a game process first!")
            return
            
        try:
            if not self.ammo_active:
                # Write to memory to enable unlimited ammo
                # Replace with actual memory writing code
                self.ammo_btn.configure(bg='#00ff00', fg='black')
            else:
                # Disable unlimited ammo
                self.ammo_btn.configure(bg='#333333', fg='white')
            self.ammo_active = not self.ammo_active
        except Exception as e:
            messagebox.showerror("Error", f"Failed to toggle ammo: {str(e)}")
            
    def toggle_weapons(self):
        if not self.selected_process:
            messagebox.showerror("Error", "Please select a game process first!")
            return
            
        try:
            if not self.weapons_active:
                # Write to memory to unlock all weapons
                # Replace with actual memory writing code
                self.weapons_btn.configure(bg='#00ff00', fg='black')
            else:
                # Disable all weapons
                self.weapons_btn.configure(bg='#333333', fg='white')
            self.weapons_active = not self.weapons_active
        except Exception as e:
            messagebox.showerror("Error", f"Failed to toggle weapons: {str(e)}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Check if running with admin privileges
    # if not ctypes.windll.shell32.IsUserAnAdmin():
    #     messagebox.showerror("Error", "Please run this program as administrator!")
    #     sys.exit(1)
        
    menu = ModMenu()
    menu.run() 