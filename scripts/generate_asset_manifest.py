#!/usr/bin/env python3
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
assets=root/"assets"
extensions={".png",".jpg",".jpeg",".webp",".gif",".avif"}
files=sorted(p.name for p in assets.iterdir() if p.is_file() and p.suffix.lower() in extensions and p.name!="manifest.json")
(assets/"manifest.json").write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding="utf-8")
print(f"Generated manifest for {len(files)} asset(s)")
