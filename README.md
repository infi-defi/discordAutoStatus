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

The application reads configuration settings from the `options.txt` file. This file is automatically created if it doesn't exist. The `options.txt` file should contain the following format:

```
Client_ID = "YOUR_CLIENT_ID"
options = option1,option2,option3
```

### `Client_ID`
Replace `"YOUR_CLIENT_ID"` with your actual Discord client ID. You can obtain this by creating an application in the [Discord Developer Portal](https://discord.com/developers/applications) and copying the "Client ID" from your application.

### `options`
This is a comma-separated list of options that will be available in the dropdown menu for updating your Discord status. For example, `options = coding, gaming, listening to music`.

## Running the Application

To run the application, execute the following command in your terminal:

```bash
python3 discord_rich_presence_updater.py
```

Make sure that your `options.txt` file is properly set up, and the application will open a window with the dropdown menu and buttons.

## Troubleshooting

- If you're having trouble connecting to Discord, ensure that your `Client_ID` is correctly set in `options.txt`.
- If the dropdown options don't appear, check the `options.txt` file for any syntax errors or missing values. Follow the given example. If its too broken to be fixed delete it, run the app again and it should reset.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.