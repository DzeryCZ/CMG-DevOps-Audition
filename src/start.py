import sys
import os.path
from src.service.ProcessLogs import ProcessLogs
from typing import List


def start():
    arguments = get_arguments()
    logs = load_log(arguments['path_to_log_file'])
    processed_logs = ProcessLogs(logs)
    test_result = processed_logs.get_product_classes()
    print(test_result)


def print_help():
    print('USAGE: run.py PATH_TO_LOG_FILE')


def get_arguments():
    if len(sys.argv) < 2:
        print_help()
        sys.exit()

    arguments = {'path_to_log_file': sys.argv[1]}

    return arguments


def load_log(path: str) -> List[str]:
    if not os.path.isfile(path):
        print_help()
        sys.exit()

    return open(path, 'r').read().splitlines()
