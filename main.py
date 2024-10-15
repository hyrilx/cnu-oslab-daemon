from arg_parser import build_parser
import config


def check_config() -> bool:
    return (hasattr(config,'OS_SOURCE_PATH')
            and hasattr(config,'TOOLCHAIN_PATH')
            and hasattr(config,'STUDENT_ID')
            and hasattr(config,'SERVER'))

if __name__ == "__main__":
    if not check_config():
        raise RuntimeError()

    parser = build_parser()
    parser.handle()
