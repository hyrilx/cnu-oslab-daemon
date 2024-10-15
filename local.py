import os
import subprocess
from argparse import Namespace
from pathlib import Path

import config

def get_os_source_path(args: Namespace ) -> Path:
    if hasattr(args,'source') and args.source:
        return Path(args.source)
    else:
        return Path(config.OS_SOURCE_PATH)


def local_build(args: Namespace) -> None:
    local_clean(args)

    env = os.environ.copy()
    env['PATH'] = f'{config.TOOLCHAIN_PATH}:{env["PATH"]}'

    subprocess.run(['make'], cwd=get_os_source_path(args), env=env)


def local_run(args: Namespace)-> None:
    cwd = get_os_source_path(args)
    if not local_detect(args):
        local_build(args)

    subprocess.run(['qemu-system-aarch64',
                    '-machine','virt','-cpu','cortex-a57','-machine','type=virt','-m','128','-nographic',
                    '-kernel','kernel.elf'], cwd=cwd)


def local_clean(args: Namespace)-> None:
    subprocess.run(['make','clean'], cwd=get_os_source_path(args))

def local_detect(args: Namespace)-> bool:
    cwd = get_os_source_path(args)
    if (cwd / 'kernel.elf').exists():
        print('Kernel detected')
        return True
    else:
        print('Kernel not detected')
        return False