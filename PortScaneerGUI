import socket
from tkinter import Tk, Label, Entry, Button, Text, END, Scrollbar, RIGHT, Y

def scan_ports():
    # Clear the output area
    output_area.delete(1.0, END)

    target = target_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
    except ValueError:
        output_area.insert(END, "Please enter valid port numbers.\n")
        return

    if not target:
        output_area.insert(END, "Please enter a target IP or hostname.\n")
        return

    output_area.insert(END, f"Scanning ports {start_port} to {end_port} on {target}...\n\n")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout for each port
            result = s.connect_ex((target, port))
            if result == 0:
                output_area.insert(END, f"[+] Port {port} is open\n")
            else:
                output_area.insert(END, f"[-] Port {port} is closed\n")
    output_area.insert(END, "\nScan complete.\n")

# Create GUI
root = Tk()
root.title("Simple Port Scanner")

# Labels and Entries
Label(root, text="Target IP or Hostname:").grid(row=0, column=0, padx=5, pady=5)
target_entry = Entry(root, width=30)
target_entry.grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Start Port:").grid(row=1, column=0, padx=5, pady=5)
start_port_entry = Entry(root, width=10)
start_port_entry.grid(row=1, column=1, padx=5, pady=5, sticky="W")

Label(root, text="End Port:").grid(row=2, column=0, padx=5, pady=5)
end_port_entry = Entry(root, width=10)
end_port_entry.grid(row=2, column=1, padx=5, pady=5, sticky="W")

# Buttons
scan_button = Button(root, text="Scan", command=scan_ports)
scan_button.grid(row=3, column=1, pady=10, sticky="E")

# Output Area
output_area = Text(root, wrap="word", height=15, width=60)
output_area.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
scrollbar = Scrollbar(root, command=output_area.yview)
scrollbar.grid(row=4, column=2, sticky='nsew')
output_area['yscrollcommand'] = scrollbar.set

# Run the application
root.mainloop()
