# dlmove/watcher.py

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dlmove.mover import move_files
from pathlib import Path


class DownloadsHandler(FileSystemEventHandler):
    # this class tells watchdog what to do when something happens in the folder

    def __init__(self, config: dict) -> None:
        self.config = config

    def on_created(self, event) -> None:
        # ignore new folders, only handle files
        if event.is_directory:
            return
        
        print(f"\nNew file: {event.src_path}")
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