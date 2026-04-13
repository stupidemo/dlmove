# dlmove/mover.py

from pathlib import Path
import shutil


def resolve_conflict(destination: Path) -> Path:
    # if a file with the same name already exists, add (1), (2), etc.
    if not destination.exists():
        return destination
    
    stem = destination.stem       # coolsong
    suffix = destination.suffix   # .mp3
    parent = destination.parent   # ~/Sorted/Music

    counter = 1
    while True:
        new_name = f"{stem}({counter}){suffix}"
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        counter += 1

def build_destination(filename: str, folders: list, destination_dir: str) -> Path:
    # builds the full destination path by joining subfolders one by one
    # empty folders list means the file goes straight into destination_dir
    dest = Path(destination_dir).expanduser().resolve()

    for folder in folders:
        dest = dest / folder

    return dest / filename


def move_files(config: dict, dry_run: bool = False) -> None:
    downloads = Path(config["downloads_dir"]).expanduser().resolve()
    destination_dir = config["destination_dir"]
    extensions = config["extensions"]

    for item in downloads.iterdir():
        # skip folders, we only care about files
        if not item.is_file():
            continue

        # normalize extension so "MP3" and "mp3" both match
        ext = item.suffix.lstrip(".").lower()

        # if extension isn't in config, leave the file alone
        if ext not in extensions:
            #print(f" Key: {ext}(not in config)")
            continue

        folder = extensions[ext]
        dest_path = build_destination(item.name, folder, destination_dir)
        dest_path = resolve_conflict(dest_path)

        print(f" {item.name} ")
        print(f" from: {item}")
        print(f" to: {dest_path}\n")

        if not dry_run:
            # create all the subfolders if they don't exist yet
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(item), str(dest_path))