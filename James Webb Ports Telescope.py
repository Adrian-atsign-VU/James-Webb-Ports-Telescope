# libraries needed
import tkinter as tk
from tkinter import ttk
import psutil
import webbrowser
import os

# Dictionary mapping port numbers to their Wikipedia page URLs
PORTS_WIKI_URLS = {
    20: "https://en.wikipedia.org/wiki/FTP_data_transfer",
    21: "https://en.wikipedia.org/wiki/FTP_control",
    22: "https://en.wikipedia.org/wiki/SSH_(Secure_Shell)",
    23: "https://en.wikipedia.org/wiki/Telnet",
    25: "https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol",
    53: "https://en.wikipedia.org/wiki/Domain_Name_System",
    67: "https://en.wikipedia.org/wiki/DHCP",
    68: "https://en.wikipedia.org/wiki/DHCP",
    69: "https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol",
    80: "https://en.wikipedia.org/wiki/HTTP",
    110: "https://en.wikipedia.org/wiki/Post_Office_Protocol",
    119: "https://en.wikipedia.org/wiki/Network_News_Transfer_Protocol",
    123: "https://en.wikipedia.org/wiki/Network_Time_Protocol",
    135: "https://en.wikipedia.org/wiki/RPC",
    137: "https://en.wikipedia.org/wiki/NetBIOS",
    138: "https://en.wikipedia.org/wiki/NetBIOS",
    139: "https://en.wikipedia.org/wiki/NetBIOS",
    143: "https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol",
    161: "https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol",
    162: "https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol",
    443: "https://en.wikipedia.org/wiki/HTTPS",
    445: "https://en.wikipedia.org/wiki/Server_Message_Block",
    546: "https://en.wikipedia.org/wiki/DHCPv6",
    547: "https://en.wikipedia.org/wiki/DHCPv6",
    995: "https://en.wikipedia.org/wiki/POP3S",
    1433: "https://en.wikipedia.org/wiki/Microsoft_SQL_Server",
    1521: "https://en.wikipedia.org/wiki/Oracle_Database",
    3306: "https://en.wikipedia.org/wiki/MySQL",
    3389: "https://en.wikipedia.org/wiki/Remote_Desktop_Protocol",
    9100: "https://en.wikipedia.org/wiki/Page_description_language",
    1984: "https://en.wikipedia.org/wiki/Nineteen_Eighty-Four",
    5426: "https://tcp-udp-ports.com/port-5426.htm",
    # Add more ports and their corresponding URLs as needed
}

def get_current_ports_in_use():
    connections = psutil.net_connections()
    ports_in_use = set()

    for conn in connections:
        if conn.status == psutil.CONN_ESTABLISHED and conn.laddr and conn.raddr:
            ports_in_use.add(conn.laddr.port)

    return sorted(list(ports_in_use))

def display_ports():
    ports_in_use = get_current_ports_in_use()
    ports_list.delete(0, tk.END)
    for port in ports_in_use:
        port_str = f"Port {port}"
        if port in PORTS_WIKI_URLS:
            port_str += f" - [Info](https://en.wikipedia.org/wiki/Port_{port})"
        ports_list.insert(tk.END, port_str)

def on_link_click(event):
    index = ports_list.nearest(event.y)
    text = ports_list.get(index)
    if "Info" in text:
        port_number = int(text.split()[1])
        if port_number in PORTS_WIKI_URLS:
            webbrowser.open(PORTS_WIKI_URLS[port_number])

# Create main window
root = tk.Tk()
root.title("James Webb Ports Telescope")
root.configure(bg="gray10")

# Set app icon
icon_path = "icon.ico"
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# Apply a modern dark theme
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", foreground="white", background="gray20")
style.configure("TLabel", foreground="white", background="gray10")

# Create label above listbox
label = ttk.Label(root, text="Ports in 'Use'", font=("Arial", 12, "bold"), anchor=tk.CENTER)
label.pack(fill=tk.X)

# Create listbox to display ports
ports_list = tk.Listbox(root, width=50, bg="gray20", fg="white", font=("Arial", 10), selectbackground="gray30", selectforeground="white")
ports_list.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
ports_list.bind("<Button-1>", on_link_click)

# Create button to refresh ports
refresh_button = ttk.Button(root, text="Refresh Ports", command=display_ports)
refresh_button.pack(pady=5)

# About
bottom_label = ttk.Label(root, text="Made By: Adrian - This is open-source and free. Not all ports will open to the wiki. Click on a port to learn more. Scroll to see more.", wraplength=400, justify=tk.CENTER)
bottom_label.pack(side=tk.BOTTOM, pady=(0, 10))

# Display ports initially
display_ports()

# Run the GUI
root.mainloop()
