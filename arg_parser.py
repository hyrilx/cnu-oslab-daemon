import argparse
import sys
from pathlib import Path

import local
import remote


class OslabFrameworkClientArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'{self.prog}: error: {message}\n')
        self.print_help()
        sys.exit(2)

    def handle(self):
        args = self.parse_args()
        if hasattr(args, 'func'):
            args.func(args)
        else:
            self.error('Unknown arguments.')


def build_parser():
    parser = OslabFrameworkClientArgumentParser(
        description="CNU-OSLAB 守护进程"
    )

    subparsers = parser.add_subparsers(
        dest='mode',
        required=True,
        help='运行模式'
    )

    parser_local = subparsers.add_parser('local', help='本地模式')
    parser_local.add_argument(
        '--source','-s',
        type=str,
        required=False,
        help='内核源代码路径'
    )
    local_subparsers = parser_local.add_subparsers(
        dest='action',
        required=True,
        help='本地动作'
    )
    parser_local_build = local_subparsers.add_parser('build', help='构建本地内核')
    parser_local_build.set_defaults(func=local.local_build)
    parser_local_run = local_subparsers.add_parser('run', help='运行本地内核')
    parser_local_run.set_defaults(func=local.local_run)
    parser_local_clean = local_subparsers.add_parser('clean', help='清理本地内核')
    parser_local_clean.set_defaults(func=local.local_clean)
    parser_local_clean = local_subparsers.add_parser('detect', help='检测本地内核')
    parser_local_clean.set_defaults(func=local.local_detect)

    parser_remote = subparsers.add_parser('remote', help='远程模式')
    remote_subparsers = parser_remote.add_subparsers(
        dest='action',
        required=True,
        help='远程动作'
    )
    parser_remote_test = remote_subparsers.add_parser('submit', help='提交内核代码并进行测评')
    parser_remote_test.add_argument(
        '--eval_id', '-e',
        type=int,
        required=True,
        help='测评实验ID'
    )
    parser_remote_test.set_defaults(func=remote.remote_submit)

    return parser