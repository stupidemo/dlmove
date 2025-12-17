
# dlmove

dlmove is a small CLI tool for Linux that sorts files from a source directory (usually Downloads) into a target directory structure based on file extensions.

Configuration is stored in a simple INI-style file under:
~/.config/dlmove/config.txt

## Features

- Sort files by extension
- Optional nested folders (folder/subfolder)
- Dry-run mode (preview changes)
- Automatic creation of missing target folders
- Safe naming: does not overwrite existing files (adds _copy)

## Installation

Clone the repository and run the installer:

```bash
git clone https://github.com/stupidemo/dlmove.git
cd dlmove
chmod +x dlmove install.sh uninstall.sh
./install.sh
```

## Configuration

Edit the config file:
```
nano ~/.config/dlmove/config.txt
```

Minimal example:
```
[DEFAULT]
downloads_dir = ~/Downloads
base_target_dir = ~/Sorted

[pdf]
folder = Documents
subfolder = PDF

[png]
folder = Pictures
```

Rules:

- Section name is the extension without a dot (e.g. `[pdf]` → `.pdf`)
- `folder` is required
- `subfolder` is optional


## Usage

Preview actions:
```
dlmove -dr
```

Apply changes:
```
dlmove -s
```

Show version:
```
dlmove -v
```

## Uninstall
```
./uninstall.sh
```
## License

MIT License