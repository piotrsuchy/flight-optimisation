import argparse
import logging
import pickle

def setup_logging(to_file):
    # Set up basic configuration for logging
    # The level and format will apply to all handlers unless overridden
    logging.basicConfig(filename='logs/log.txt', level=logging.INFO if to_file else logging.CRITICAL,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    if to_file:
        # Add the file handler
        file_handler = logging.FileHandler('logs/log.txt')
        # Set the level for the file handler
        file_handler.setLevel(logging.INFO)

        # Get the root logger and add the file handler to it
        logger = logging.getLogger()
        logger.addHandler(file_handler)

def get_args():
    parser = argparse.ArgumentParser(
        description='Run the evolutionary algorithm.'
    )
    parser.add_argument('--log', action='store_true', help='enable logging')
    parser.add_argument('--pickle', help='Pickle file name', type=str)
    return parser.parse_args()

def save_to_file(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)

def load_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)