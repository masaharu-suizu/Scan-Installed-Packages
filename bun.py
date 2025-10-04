#!/usr/bin/env python3

import json
import os
import subprocess
import sys
import yaml

CONFIG_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "configs",
        "bun.yml"
    )
)

def load_config_file(path: str) -> list[str]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data.get("project_path_list", [])
    except FileNotFoundError:
        print(f"Config file not found: {path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading config file: {e}", file=sys.stderr)
        sys.exit(1)

def get_installed_packages(path: str) -> str:
    try:
        cmd = ["bun", "pm", "ls", "--cwd", path]
        result = subprocess.check_output(cmd)
        return result.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        print(f"Command execution error: {e}", file=sys.stderr)
        sys.exit(1)

def main() -> None:
    path_list = load_config_file(CONFIG_PATH)
    if not path_list:
        print("No project paths found in config.", file=sys.stderr)
        sys.exit(1)

    for path in path_list:
        packages = get_installed_packages(path)
        print(packages)

if __name__ == "__main__":
    main()
