import os, sys
from console import add_argument_parser


def rename_files(tgt_dir: str):
    for file in os.listdir(tgt_dir):
        new_name = f'Приложение {file[2:]}'
        os.rename(os.path.join(tgt_dir, file), os.path.join(tgt_dir, new_name))


def main():
    args = add_argument_parser()
    tgt_dir = args.tgt_dir

    try:
        rename_files(tgt_dir)
    except FileNotFoundError as e:
        sys.tracebacklimit = 0
        print(f'Probably wrong path! {e}')


if __name__ == '__main__':
    main()
