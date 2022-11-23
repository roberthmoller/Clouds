# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
from functools import reduce

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    file_content = """
        Oh-oh-oh
        Let's go fly a kite
        Up to the highest height
        Let's go fly a kite
        And send it soaring
        Up through the atmosphere
        Up where the air is clear
        Oh, let's go fly a kite
    """

    mappers = [
        context.call_activity("Mapper", json.dumps((linenumber, line)))
        for linenumber, line in enumerate(file_content.split('\n'))
    ]
    mapresults = yield context.task_all(mappers)
    flatmapresults = list(reduce(lambda a, b: a+b, mapresults))

    logging.log(logging.INFO, f"Mapper <- {flatmapresults}")
    shuffleresults = yield context.call_activity("Shuffler", json.dumps(flatmapresults))
    logging.log(logging.INFO, f"Shuffler <- {shuffleresults}")

    reducers = [
        context.call_activity("Reducer", json.dumps(group))
        for group in shuffleresults.items()
    ]
    reduceresults = yield context.task_all(reducers)
    logging.log(logging.INFO, f"Reducer <- {reduceresults}")

    return reduceresults
    # return shuffleresults
    # return mapresults


main = df.Orchestrator.create(orchestrator_function)
