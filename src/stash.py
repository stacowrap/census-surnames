#!/usr/bin/env python3

from pathlib import Path
import requests
from shutil import unpack_archive
import yaml

STASHED_DIR = Path('data', 'stashed')
SRC_MANIFEST_PATH = STASHED_DIR / 'manifest.yaml'

def fetch():
    manifest = yaml.load(SRC_MANIFEST_PATH.open())
    for year, files in manifest.items():
        print(year)
        destdir = STASHED_DIR / str(year)
        destdir.mkdir(exist_ok=True, parents=True)

        for fname, finfo in files.items():
            destpath = destdir / fname
            if destpath.is_file():
                sb = destpath.stat().st_size
                print(F"{destpath} exists: {sb} bytes")
                continue

            url = finfo['url']
            print(F"Downloading {url}")
            resp = requests.get(url)
            if resp.status_code == 200:
                content = resp.content
                print(F"Saving {len(content)} bytes to {destpath}")
                destpath.write_bytes(content)


def unpack():
    for zn in STASHED_DIR.glob('**/*.zip'):
        destdir = zn.parent
        print(F"Unzipping {zn.name} into {destdir}")
        unpack_archive(zn, extract_dir=destdir)




if __name__ == '__main__':
    print("Fetching remote data...")
    fetch()

    print("Unpacking fetched zips...")
    unpack()





