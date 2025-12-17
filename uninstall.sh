set -e

BIN_PATH="/usr/local/bin/dlmove"
CONFIG_DIR="$HOME/.config/dlmove"

echo "[*] Uninstalling dlmove..."

# Remove binary
if [ -f "$BIN_PATH" ]; then
    sudo rm "$BIN_PATH"
    echo "[OK] Removed $BIN_PATH"
else
    echo "[INFO] dlmove binary not found"
fi

# Remove config directory
if [ -d "$CONFIG_DIR" ]; then
    rm -rf "$CONFIG_DIR"
    echo "[OK] Removed config directory $CONFIG_DIR"
else
    echo "[INFO] Config directory not found"
fi

echo
echo "[DONE] dlmove has been uninstalled."
