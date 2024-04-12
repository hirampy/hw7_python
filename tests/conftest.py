import os
import shutil
import zipfile
import pytest

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(os.path.dirname(CURRENT_FILE))
TMP_DIR = os.path.join(CURRENT_DIR, "temp")
RES_DIR = os.path.join(CURRENT_DIR, "resource")
archive = os.path.join(RES_DIR, "arch.zip")

@pytest.fixture(scope="session", autouse=True)
def arch_file():
    if not os.path.exists(RES_DIR):
        os.mkdir(RES_DIR)
    with zipfile.ZipFile(archive, 'w') as zf:
        for file in os.listdir(TMP_DIR):
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))

    yield
    shutil.rmtree(RES_DIR)