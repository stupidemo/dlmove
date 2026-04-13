# dlmove/cli.py

import argparse
from dlmove.config import load_config
from dlmove.mover import move_files
from dlmove.watcher import start_daemon


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="dlmove",
        description="Downloads files autosorter"
    )

    # path to config file, defaults to ~/.config/dlmove/config.yaml
    parser.add_argument(
        "-c", "--config",
        default="~/.config/dlmove/config.yaml",
        help="Path to config file"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version="dlmove 0.1.0"
    )

    # dry-run shows what would happen without actually moving anything
    # useful for testing before actually running
    parser.add_argument(
        "-dr", "--dry-run",
        action="store_true",
        help="Show what will be moved"
    )

    # daemon mode watches the folder and runs in the background
    parser.add_argument(
        "-d", "--daemon",
        action="store_true" 
    )

    args = parser.parse_args()
    config=load_config(args.config)

    if args.dry_run:
        print("dry-run mode - files are not moving\n")

    move_files(config, dry_run=args.dry_run)

    if args.daemon:
        start_daemon(config)
    else:
        move_files(config, dry_run=args.dry_run)