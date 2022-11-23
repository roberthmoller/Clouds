# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import json
import logging
from typing import List, Tuple


def main(keyvalue: str) -> List[Tuple[str, int]]:
    logging.log(logging.INFO, f"map -> {keyvalue}")
    linenumber, line = json.loads(keyvalue)
    return list(map(lambda word: (word, 1), line.split()))
