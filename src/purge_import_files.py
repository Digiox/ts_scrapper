
import os
def purge_import_files(filename: str) -> None:
    """Remove existing CSV file if it exists."""
    if os.path.exists(filename):
        print(f'{filename} already exists, deleting it')
        os.remove(filename)