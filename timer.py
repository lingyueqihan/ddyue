import tkinter as tk
import time

class FocusClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Focus Clock")
        self.master.geometry("300x200")
        self.time_var = tk.StringVar()
        self.time_label = tk.Label(self.master, textvariable=self.time_var, font=("Arial", 80))
        self.time_label.pack(pady=20)
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_button.pack(pady=10)
        self.running = False
        self.seconds = 1500 # 25 minutes
        self.update_time()

    def update_time(self):
        minutes, seconds = divmod(self.seconds, 60)
        self.time_var.set("{:02d}:{:02d}".format(minutes, seconds))
        if self.seconds > 0 and self.running:
            self.seconds -= 1
            self.master.after(1000, self.update_time)
        elif self.seconds == 0:
            self.stop_timer()

    def start_timer(self):
        self.running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.update_time()

    def stop_timer(self):
        self.running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.seconds = 1500 # reset the timer

root = tk.Tk()
focus_clock = FocusClock(root)
root.mainloop()

