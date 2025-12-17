set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BIN_PATH="/usr/local/bin/dlmove"
CONFIG_DIR="$HOME/.config/dlmove"
CONFIG_FILE="$CONFIG_DIR/config.txt"
CONFIG_EXAMPLE="$SCRIPT_DIR/config.example.txt"

echo "[*] Installing dlmove..."

# Install binary
echo "[*] Installing binary to $BIN_PATH (sudo required)"
sudo cp "$SCRIPT_DIR/dlmove" "$BIN_PATH"
sudo chmod +x "$BIN_PATH"

# Create config directory
echo "[*] Ensuring config directory exists: $CONFIG_DIR"
mkdir -p "$CONFIG_DIR"

# Install config if it does not exist
if [ -f "$CONFIG_FILE" ]; then
    echo "[INFO] Config already exists, not overwriting:"
    echo "       $CONFIG_FILE"
else
    echo "[*] Installing default config"
    cp "$CONFIG_EXAMPLE" "$CONFIG_FILE"
fi

echo
echo "[DONE] dlmove installed successfully."
echo
echo "Next steps:"
echo "  1. Edit config: nano ~/.config/dlmove/config.txt"
echo "  2. Preview changes: dlmove -dr"
echo "  3. Apply changes: dlmove -s"
