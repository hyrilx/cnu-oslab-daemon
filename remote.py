import os
import tarfile
from os import PathLike
from pathlib import Path

import requests
import tempfile

import config
import local


def create_archive(directory:PathLike):
    archive_fd, archive_path = tempfile.mkstemp(suffix='.tar')
    os.close(archive_fd)

    with tarfile.open(archive_path, "w") as tar:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            files = [f for f in files if not f.startswith('.')]
            for file in files:
                full_path = os.path.join(root, file)
                arc_name = os.path.relpath(full_path, directory)
                tar.add(full_path, arcname=arc_name)
    return archive_path



def upload_directory(eval_id:str) -> None:
    archive_path = create_archive(Path(config.OS_SOURCE_PATH))

    with open(archive_path, 'rb') as f:
        response = requests.post(f'{config.SERVER}/submit', files={'file': f},
                                 data={'user_id': config.STUDENT_ID, 'exp_id': eval_id}, stream=True)

    os.remove(archive_path)

    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                print(line.decode('utf-8'))
    else:
        print(f"Query failed: {response.text}")


def remote_submit(args):
    eval_id = args.eval_id

    print('[SUBMITTING...]')
    local.local_clean(args)
    upload_directory(eval_id)