# Discord Auto Status

This is a simple Python application that allows you to update your Discord Rich Presence status dynamically using a dropdown menu.

## Prerequisites
- Python 3.6 or higher
- The `tkinter` and `pypresence` libraries

## Installation

### Linux
1. Install Python if you haven't already:
   ```bash
   sudo apt install python3
   ```

2. Install the required dependencies:
   ```bash
   pip install pypresence
   ```

3. Ensure that `tkinter` is installed. On Ubuntu, you can do this by running:
   ```bash
   sudo apt-get install python3-tk
   ```

### macOS
1. Install Python if you haven't already (macOS typically comes with Python installed):
   ```bash
   brew install python
   ```

2. Install the required dependencies:
   ```bash
   pip3 install pypresence
   ```

3. Make sure `tkinter` is installed. If it's missing, you can install it via:
   ```bash
   brew install python-tk
   ```

### Windows
1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install the required dependencies:
   ```bash
   pip install pypresence
   ```

3. `tkinter` is usually included with Python on Windows, but if it's not, you can install it by following these instructions: [tkinter installation guide for Windows](https://tkdocs.com/tutorial/install.html).

## Configuration

The application reads configuration settings from `config.json`. If this file doesn't exist, it is automatically created with default values.

### Example `config.json`
```json
{
    "clients": [
        { "client_id": "Client_ID_1", "name": "Coding" },
        { "client_id": "Client_ID_2", "name": "Chilling" }
    ],
    "description": "hot diggity dog I surely do love rich presence"
}
```

### Explanation:
- **`clients`**: A list of Discord applications, each containing:
  - `client_id`: The Application ID from the [Discord Developer Portal](https://discord.com/developers/applications).
  - `name`: The name that appears in the dropdown menu.
- **`description`**: The status message that remains static for all selected applications.


## Running the Application

To start the application, run:

```bash
python3 discord_rich_presence_updater.py
```

The app will open a window where you can select an application from the dropdown menu and update your Rich Presence.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.