# Libraries needed
import tkinter as tk
from tkinter import ttk
import psutil
import webbrowser
import os

# Dictionary mapping port numbers to their Wikipedia page URLs (Feel free to list more)
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
    53: "https://en.wikipedia.org/wiki/Domain_Name_System",
    80: "https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol",
    443: "https://en.wikipedia.org/wiki/HTTPS",
    21: "https://en.wikipedia.org/wiki/File_Transfer_Protocol",
    25: "https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol",
    22: "https://en.wikipedia.org/wiki/Secure_Shell",
    23: "https://en.wikipedia.org/wiki/Telnet",
    3389: "https://en.wikipedia.org/wiki/Remote_Desktop_Protocol",
    110: "https://en.wikipedia.org/wiki/Post_Office_Protocol",
    143: "https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol",
    69: "https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol",
    3306: "https://en.wikipedia.org/wiki/MySQL",
    1723: "https://en.wikipedia.org/wiki/Point-to-Point_Tunneling_Protocol",
    119: "https://en.wikipedia.org/wiki/Network_News_Transfer_Protocol",
    137: "https://en.wikipedia.org/wiki/NetBIOS",
    139: "https://en.wikipedia.org/wiki/NetBIOS",
    445: "https://en.wikipedia.org/wiki/Server_Message_Block",
    1433: "https://en.wikipedia.org/wiki/Microsoft_SQL_Server",
    161: "https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol",
    8080: "https://en.wikipedia.org/wiki/HTTP",
    427: "https://en.wikipedia.org/wiki/Service_Location_Protocol",
    548: "https://en.wikipedia.org/wiki/Apple_Filing_Protocol",
    554: "https://en.wikipedia.org/wiki/Real_Time_Streaming_Protocol",
    587: "https://en.wikipedia.org/wiki/Email_submission",
    636: "https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol",
    873: "https://en.wikipedia.org/wiki/RSYNC",
    990: "https://en.wikipedia.org/wiki/FTPS",
    993: "https://en.wikipedia.org/wiki/IMAPS",
    995: "https://en.wikipedia.org/wiki/POP3S",
    1434: "https://en.wikipedia.org/wiki/Microsoft_SQL_Server_Browser",
    2049: "https://en.wikipedia.org/wiki/Network_File_System_(protocol)",
    3307: "https://en.wikipedia.org/wiki/MySQL",
    5432: "https://en.wikipedia.org/wiki/PostgreSQL",
    5900: "https://en.wikipedia.org/wiki/Remote_Framebuffer",
    8080: "https://en.wikipedia.org/wiki/HTTP",
    9090: "https://en.wikipedia.org/wiki/Alternate_HTTP",
    1720: "https://en.wikipedia.org/wiki/H.323",
    2000: "https://en.wikipedia.org/wiki/Remote_Administration_Tool",
    32768: "https://en.wikipedia.org/wiki/Films_and_TV_Port",
    3689: "https://en.wikipedia.org/wiki/DAAP",
    54321: "https://en.wikipedia.org/wiki/BitTorrent_(protocol)",
    27015: "https://en.wikipedia.org/wiki/Steam_(service)",
    27016: "https://en.wikipedia.org/wiki/Steam_(service)",
    5190: "https://en.wikipedia.org/wiki/AOL_Instant_Messenger",
    1863: "https://en.wikipedia.org/wiki/Microsoft_Notification_Protocol",
    5050: "https://en.wikipedia.org/wiki/Yahoo!_Messenger",
    5060: "https://en.wikipedia.org/wiki/Session_Initiation_Protocol",
    5061: "https://en.wikipedia.org/wiki/Session_Initiation_Protocol",
    7070: "https://en.wikipedia.org/wiki/RealPlayer",
    7777: "https://en.wikipedia.org/wiki/Unreal_Tournament",
    2001: "https://en.wikipedia.org/wiki/User_Datagram_Protocol",
    2048: "https://en.wikipedia.org/wiki/Network_File_System_(protocol)",
    3306: "https://en.wikipedia.org/wiki/MySQL",
    953: "https://en.wikipedia.org/wiki/RNDC",
    111: "https://en.wikipedia.org/wiki/ONC_RPC",
    989: "https://en.wikipedia.org/wiki/FTPS",
    987: "https://en.wikipedia.org/wiki/Spam_Assassin",
    666: "https://en.wikipedia.org/wiki/IRC",
    999: "https://en.wikipedia.org/wiki/Apache_Apache_Coyote",
    19638: "https://en.wikipedia.org/wiki/Ensim_Webppliance",
    17500: "https://en.wikipedia.org/wiki/Dropbox_(service)",
    5051: "https://en.wikipedia.org/wiki/ITA_agent",
    5052: "https://en.wikipedia.org/wiki/ITA_manager",
}
# get_current_ports_in_use duh
def get_current_ports_in_use():
    connections = psutil.net_connections()
    ports_in_use = set()

    for conn in connections:
        if conn.status == psutil.CONN_ESTABLISHED and conn.laddr and conn.raddr:
            ports_in_use.add(conn.laddr.port)

    return sorted(list(ports_in_use))

# display_ports make click to open wiki and stuff
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

def refresh_ports():
    display_ports()

def exit_app():
    root.destroy()

def toggle_sort_order():
    global sort_order_asc
    sort_order_asc = not sort_order_asc
    filter_ports()

def filter_ports():
    # Sort ports based on sort_order_asc
    ports_list.delete(0, tk.END)
    ports_in_use = get_current_ports_in_use()
    sorted_ports = sorted(ports_in_use, reverse=not sort_order_asc)
    for port in sorted_ports:
        port_str = f"Port {port}"
        if port in PORTS_WIKI_URLS:
            port_str += f" - [Info](https://en.wikipedia.org/wiki/Port_{port})"
        ports_list.insert(tk.END, port_str)

# Create main window
root = tk.Tk()
root.title("James Webb Ports Telescope v2.0")
root.configure(bg="gray10")

# Set app icon with fail safe
icon_path = "icon-pro.ico"
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
refresh_button = ttk.Button(root, text="Refresh Ports", command=refresh_ports)
refresh_button.pack(pady=5, side=tk.LEFT)

# Create button to exit app
exit_button = ttk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5, side=tk.LEFT)

# Create button to toggle sort order
sort_order_asc = True
sort_order_button = ttk.Button(root, text="Toggle Sort Order", command=toggle_sort_order)
sort_order_button.pack(pady=5, side=tk.LEFT)

# About
bottom_label = ttk.Label(root, text="Developed by Adrian, this app is open-source and free. Note that not all ports have associated Wikipedia pages. Click on a port for details. Scroll for more information.", wraplength=450, justify=tk.CENTER)
bottom_label.pack(side=tk.BOTTOM, pady=(0, 10))

# Display ports initially
display_ports()

# Run the GUI
root.mainloop()
