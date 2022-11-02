import argparse


def add_argument_parser():
    parser = argparse.ArgumentParser(description='<----- Rename Files ----->')
    parser.add_argument(
        '--d', dest='tgt_dir',
        help='Absolute path to directory where you want to change files. Don\'t forget slash at the '
             'end of path. Example: /path_to_dir/target_dir/'
        )

    return parser.parse_args()
