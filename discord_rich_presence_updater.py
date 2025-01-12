import time
import os
from tkinter import Tk, StringVar, OptionMenu, Button, Label
from pypresence import Presence

def initialize_config():
    if not os.path.exists("options.txt"):
        with open("options.txt", "w") as f:
            f.write('Client_ID = "YOUR_CLIENT_ID"\n')
            f.write('options = option1,option2,option3\n')

def load_config():
    client_id = ""
    options = []
    with open("options.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("Client_ID"):
                client_id = line.split("=")[1].strip().strip('"')
            elif line.startswith("options"):
                options = line.split("=")[1].strip().split(",")
    return client_id, options

initialize_config()
CLIENT_ID, options = load_config()

RPC = Presence(CLIENT_ID)
RPC.connect()

def update_status(selected_option):
    """Update Discord Rich Presence with the selected option."""
    RPC.update(
        state=f"hot diggity dog I surely do love {selected_option}", #change prefix to the option here.
        large_image="coding_logo",  # Add assets in the dev portal
        start=time.time()
    )
    status_label.config(text=f"Updated to: {selected_option}")

def close_app():
    """Closes the application and stops Rich Presence."""
    RPC.clear()
    app.destroy()

#gui
app = Tk()
app.title("Discord Rich Presence Updater")
app.geometry("400x200")

#dropdown
selected_option = StringVar(app)
selected_option.set(options[0])  # Default value
dropdown = OptionMenu(app, selected_option, *options)
dropdown.pack(pady=20)

#update button
update_button = Button(app, text="Update Status", command=lambda: update_status(selected_option.get()))
update_button.pack(pady=10)

#close button
close_button = Button(app, text="Close", command=close_app)
close_button.pack(pady=10)

#status label
status_label = Label(app, text="Select an option and update your status.")
status_label.pack(pady=10)

#run the app and pray :praying_emoji"
app.mainloop()