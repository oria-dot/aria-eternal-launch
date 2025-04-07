# dashboard_launcher.py – Launches Aria's Live Dashboard

def launch_dashboard(context):
    try:
        try:
        import tkinter
except ImportError:
    tkinter = None as tk
        root = tk.Tk()
        root.title("Aria Live Dashboard")
        label = tk.Label(root, text="System Status: " + (context.status[-1] if context.status else "Initializing..."))
        label.pack(padx=20, pady=20)
        root.after(5000, lambda: label.config(text="Updated Status: " + (context.status[-1] if context.status else "Running...")))
        root.mainloop()
    except Exception as e:
        print(f"[Dashboard] Failed to launch: {e}")
