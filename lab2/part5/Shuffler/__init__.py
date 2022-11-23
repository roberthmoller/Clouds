# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

from itertools import groupby
from typing import Dict, List, Tuple
import json
import logging


def main(words: str) -> Dict[str, List[int]]:
    logging.log(logging.INFO, f"shuffle -> {words}")
    wordsandone = json.loads(words)
    shuffled = {}
    for word, one in wordsandone:
        if word not in shuffled:
            shuffled[word] = []
        shuffled[word].append(one)
    return shuffled
