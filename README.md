## Setting up Automatic Script Execution

Our project includes a macOS `launchd` configuration file to schedule automatic script execution. Follow these steps to set it up:

1. **Update Paths**: Edit `config/com.example.myproject.plist` to update the paths to your Python executable and script file.

2. **Install Launch Agent**:
   Copy the `.plist` file to `~/Library/LaunchAgents/`:
   ```sh
   cp config/com.example.myproject.plist ~/Library/LaunchAgents/

3. **Load the Launch Agent**:
    $ launchctl load ~/Library/LaunchAgents/com.example.myproject.plist
