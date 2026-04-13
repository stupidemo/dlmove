# dlmove/watcher.py

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dlmove.mover import move_files
from pathlib import Path


def wait_for_file(path: str, timeout: int = 10) -> bool:
    # wait till file stops changing
    size_before = -1
    elapsed = 0

    while elapsed < timeout:
        try:
            size_now = os.path.getsize(path)
        except FileNotFoundError:
            return False
        
        if size_now == size_before:
            return True
        
        size_before = size_now
        time.sleep(1)
        elapsed += 1

    return False


class DownloadsHandler(FileSystemEventHandler):
    # this class tells watchdog what to do when something happens in the folder

    def __init__(self, config: dict) -> None:
        self.config = config


    def on_created(self, event) -> None:
        # ignore new folders, only handle files
        if event.is_directory:
            return

        # ignore temporary downloading files
        if event.src_path.endswith(".part") or event.src_path.endswith(".crdownload"):
            return

        print(f"\n  New file detected: {event.src_path}")
        
        # wait till file download completely
        if not wait_for_file(event.src_path):
            print(f"  Timeout: file never stabilized, skipping")
            return
        
        move_files(self.config)


def start_daemon(config: dict) -> None:
    handler = DownloadsHandler(config)

    # expanduser() here is important - watchdog doesn't understand ~
    watch_path = str(Path(config["downloads_dir"]).expanduser().resolve())

    observer = Observer()
    observer.schedule(
        handler,
        path=watch_path,
        recursive=False  # don't watch subfolders, just downloads
    )

    observer.start()
    print(f"Watching folder: {watch_path}")
    print("Press Ctrl+C to stop")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    # wait for the observer thread to fully finish before exiting
    observer.join()

