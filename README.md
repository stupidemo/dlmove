# dlmove

A simple CLI tool for linux that automatically sorts files from your Downloads folder.

I built this as a learning project while studying Python.
It's also genuinely useful - my Downloads folder was a mess.

## What it does

Moves files from your Downloads folder into organized subfolders
based on file extension. The folder structure is fully configurable.

```
Downloads/sound.mp3  ->  ~/Sorted/Music/sound.mp3
Downloads/doc.pdf    ->  ~/Sorted/Docs/PDFs/doc.pdf
Downloads/mod.jar    ->  ~/Sorted/Mods/mod.jar
```

If a file with the same name already exists, it adds (1), (2), etc.
instead of overwriting it.

## Install

```bash
git clone https://github.com/stupidemo/dlmove
cd dlmove
pip install -e .
```

## Setup

Copy the example config to the default location:
```bash
mkdir -p ~/.config/dlmove
cp config.yaml ~/.config/dlmove/config.yaml
```

Then edit it to match your folder structure.

## Usage

```bash
dlmove -h / --help 
dlmove -dr / --dry-run   # preview without moving anything
dlmove -d / --daemon     # watch folder in background
dlmove -c / --config ~/path/to/config.yaml
dlmove -v / --version
```

## Auto-start on boot (Linux)

```bash
# copy the service file
mkdir -p ~/.config/systemd/user
cp dlmove.service ~/.config/systemd/user/

# enable it
systemctl --user daemon-reload
systemctl --user enable dlmove.service
systemctl --user start dlmove.service
```

## Built with

- [watchdog](https://github.com/gorakhargosh/watchdog) — filesystem monitoring
- [PyYAML](https://pyyaml.org/) — config parsing
- pathlib, shutil, argparse — standard library

## Note

Hope this will be useful and easy-to-use. Looking forward to add more functions to this project

## License

[MIT License](LICENSE)