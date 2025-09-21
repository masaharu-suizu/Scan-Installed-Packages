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
        "apt.yml"
    )
)

def load_config_file(path: str) -> list[str]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data.get("packages", [])
    except FileNotFoundError:
        print(f"Config file not found: {path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error loading config file: {e}", file=sys.stderr)
        sys.exit(1)

def get_all_installed_packages() -> list[str]:
    try:
        cmd = ["dpkg", "-l"]
        result = subprocess.check_output(cmd)
        return result.decode("utf-8").splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Command execution error: {e}", file=sys.stderr)
        sys.exit(1)

def main() -> None:
    target_packages = load_config_file(CONFIG_PATH)
    flipped_target_packages = {package: True for package in target_packages}

    all_installed_packages = get_all_installed_packages()

    results = []
    for line in all_installed_packages:
        if line.startswith("ii "):
            parts = line.split()
            if len(parts) >= 3:
                package_name    = parts[1]
                package_version = parts[2]
                # 対象のパッケージのみ結果用の配列に追加する
                if package_name in flipped_target_packages:
                    results.append([package_name, package_version])

    print(json.dumps(results))

if __name__ == "__main__":
    main()
