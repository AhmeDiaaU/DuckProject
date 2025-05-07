import tkinter as tk
from tkinter import ttk

from Ducks.MallardDuck import MallardDuck
from Ducks.RubberDuck import RubberDuck
from Ducks.RocketDuck import RocketDuck


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Duck Simulator")
        self.root.geometry("400x300")
        
        self.current_duck = None
        
        frame = ttk.Frame(root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Duck Type:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.cmb_duck_type = ttk.Combobox(frame, values=["Mallard", "Rubber", "Rocket"])
        self.cmb_duck_type.grid(row=0, column=1, sticky=tk.W, pady=5)
        self.cmb_duck_type.current(0)
        
        
        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Display", command=self.btn_display_click).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Fly", command=self.btn_fly_click).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Quack", command=self.btn_quack_click).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(frame, text="Output:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.txt_output = tk.Text(frame, height=10, width=40)
        self.txt_output.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(3, weight=1)
    
    def set_duck_type(self):
        duck_type = self.cmb_duck_type.get()
        if duck_type == "Mallard":
            self.current_duck = MallardDuck()
        elif duck_type == "Rubber":
            self.current_duck = RubberDuck()
        elif duck_type == "Rocket":
            self.current_duck = RocketDuck()
        else:
            self.current_duck = None
    
    def btn_display_click(self):
        self.set_duck_type()
        if self.current_duck:
            self.txt_output.delete(1.0, tk.END)
            self.txt_output.insert(tk.END, self.current_duck.display())
    
    def btn_fly_click(self):
        self.set_duck_type()
        if self.current_duck:
            self.txt_output.delete(1.0, tk.END)
            self.txt_output.insert(tk.END, self.current_duck.perform_fly())
    
    def btn_quack_click(self):
        self.set_duck_type()
        if self.current_duck:
            self.txt_output.delete(1.0, tk.END)
            self.txt_output.insert(tk.END, self.current_duck.perform_quack())


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()