```shell
$ git clone https://github.com/masaharu-suizu/Scan-Installed-Packages.git
Cloning into 'Scan-Installed-Packages'...
remote: Enumerating objects: 18, done.
remote: Counting objects: 100% (18/18), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 18 (delta 1), reused 14 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (18/18), 8.91 KiB | 8.91 MiB/s, done.
Resolving deltas: 100% (1/1), done.

$ cd Scan-Installed-Packages/

$ uv sync
Using CPython 3.13.7
Creating virtual environment at: .venv
Resolved 3 packages in 0.63ms
Installed 2 packages in 1ms
 + pyyaml==6.0.3
 + ruff==0.13.3

$ uv run apt.py 
[["perl", "5.38.2-3.2ubuntu0.2"], ["python3", "3.12.3-0ubuntu2"]]

$ uv run bun.py 
/home/ibukichi/GitHub/sandbox-bun node_modules (10)
├── @types/bun@1.2.21
├── @types/figlet@1.7.0
├── figlet@1.9.1
└── typescript@5.9.2
```