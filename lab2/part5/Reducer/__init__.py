# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import json
import logging
from functools import reduce


def main(keyvalues: str) -> str:
    logging.log(logging.INFO, f"reduce -> {keyvalues}")
    key, values = json.loads(keyvalues)
    return (key, reduce(lambda a, b: a+b, values))
