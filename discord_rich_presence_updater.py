import time
import os
import json
from tkinter import Tk, StringVar, OptionMenu, Button, Label
from pypresence import Presence

CONFIG_FILE = "config.json"

# Generate config file.
def initialize_config():
    if not os.path.exists(CONFIG_FILE):
        default_config = {
            "clients": [
                {"client_id": "Client_ID_1", "name": "Coding"},
                {"client_id": "Client_ID_2", "name": "Chilling"}
            ],
            "description": "hot diggity dog I surely do love rich presence"
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f, indent=4)

# Loads config file
def load_config():
    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)
    return data["clients"], data["description"]

initialize_config()
clients, description = load_config()

if not clients:
    raise ValueError("No Client IDs found in config.json!")

current_client_index = 0
RPC = None

# Reconnect
def connect_rpc(client_index):
    global RPC, current_client_index
    current_client_index = client_index  
    if RPC:
        RPC.clear()
    RPC = Presence(clients[client_index]["client_id"])
    RPC.connect()

connect_rpc(current_client_index)  

# Update
def update_status(selected_name):
    client_index = next((i for i, c in enumerate(clients) if c["name"] == selected_name), 0)
    if client_index != current_client_index:
        connect_rpc(client_index)  

    RPC.update(
        state=description,
        large_image="coding_logo",  
        start=time.time()
    )
    status_label.config(text=f"Updated to: {selected_name} (App ID: {clients[client_index]['client_id']})")

def close_app():
    RPC.clear()
    app.destroy()

# GUI
app = Tk()
app.title("Discord Rich Presence Updater")
app.geometry("400x200")

selected_option = StringVar(app)
selected_option.set(clients[0]["name"])  

dropdown = OptionMenu(app, selected_option, *[c["name"] for c in clients])
dropdown.pack(pady=20)

update_button = Button(app, text="Update Status", command=lambda: update_status(selected_option.get()))
update_button.pack(pady=10)

close_button = Button(app, text="Close", command=close_app)
close_button.pack(pady=10)

status_label = Label(app, text="Select an application and update your status.")
status_label.pack(pady=10)

app.mainloop()