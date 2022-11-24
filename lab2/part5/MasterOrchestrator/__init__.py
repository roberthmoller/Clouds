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
    inputs = yield context.call_activity("getInputDataFn")
    logging.log(logging.INFO, f"getInputDataFn <- {inputs}")
    inputlines = reduce(
        lambda a, b: a+b, list(map(lambda file: file.split("\r\n"), inputs)))
    # I'm not sure what you want here. I'm assunimg you want to read all files and do the wordcount over all of them.

    mappers = [
        context.call_activity("Mapper", json.dumps((linenumber, line)))
        for linenumber, line in enumerate(inputlines)
    ]
    mapresults= yield context.task_all(mappers)
    flatmapresults= list(reduce(lambda a, b: a+b, mapresults))

    logging.log(logging.INFO, f"Mapper <- {flatmapresults}")
    shuffleresults=yield context.call_activity("Shuffler", json.dumps(flatmapresults))
    logging.log(logging.INFO, f"Shuffler <- {shuffleresults}")

    reducers=[
        context.call_activity("Reducer", json.dumps(group))
        for group in shuffleresults.items()
    ]
    reduceresults= yield context.task_all(reducers)
    logging.log(logging.INFO, f"Reducer <- {reduceresults}")

    return reduceresults
    # return shuffleresults
    # return mapresults


main= df.Orchestrator.create(orchestrator_function)
