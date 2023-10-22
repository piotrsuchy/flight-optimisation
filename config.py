import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description='Run the evolutionary algorithm.'
    )
    parser.add_argument('--log', action='store_true', help='enable logging')
    return parser.parse_args()
