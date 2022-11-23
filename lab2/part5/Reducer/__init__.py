# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from functools import reduce


def main(keyvalues: str) -> str:
    words = map(lambda wordandone: wordandone.split('|'), keyvalues.split(','))
    logging.log(logging.INFO, f"Words: {words}")
    return (words[0][0], reduce(lambda count, word: count+1, words, 0))
