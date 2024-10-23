from pathlib import Path
import sys

from arg_parser import build_parser
import config


def check_config() -> bool:
    os_source_path = Path(config.OS_SOURCE_PATH)
    toolchain_path = Path(config.TOOLCHAIN_PATH)
    return (
            (
                    hasattr(config, 'OS_SOURCE_PATH')
                    and hasattr(config, 'TOOLCHAIN_PATH')
                    and hasattr(config, 'STUDENT_ID')
                    and hasattr(config, 'SERVER')
            )
            and (
                    os_source_path.exists()
                    and (os_source_path / 'main.c').exists()
                    and (os_source_path / 'Makefile').exists()
                    and (os_source_path / 'Makefile.inc').exists()
                    and (os_source_path / 'kernel.ld').exists()
            )
            and (
                    toolchain_path.exists()
                    and (toolchain_path / 'bin').exists()
                    and (toolchain_path / 'aarch64-none-elf').exists()
                    and (toolchain_path / 'libexec').exists()
                    and (toolchain_path / 'bin' / 'aarch64-none-elf-gcc').exists()
            )
            and (
                config.STUDENT_ID.isdigit()
            )
    )


if __name__ == "__main__":
    if not check_config():
        print("配置文件无效，请检查是否包含必要内容且合法.", file=sys.stderr)
        exit(1)

    parser = build_parser()
    parser.handle()
