import os
import hashlib
import sys
from main import rename_files


def create_hashes_lst(path_to_files):

    hashes = []

    for file in sorted(os.listdir(path_to_files)):
        with open(rf'{path_to_files}{file}', 'rb') as f:
            hashes.append(hashlib.md5(f.read()).hexdigest())

    return hashes


def test_rename():
    tgt_dir = './test_data/'
    validate_dir = './test_data_validation/'

    try:
        rename_files(tgt_dir)
    except FileNotFoundError as e:
        sys.tracebacklimit = 0
        print(f'Probably wrong path!')

    test_hash = create_hashes_lst(tgt_dir)
    validation_hash = create_hashes_lst(validate_dir)

    assert test_hash == validation_hash


test_rename()
