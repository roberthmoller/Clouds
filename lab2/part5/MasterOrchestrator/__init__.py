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
    file_content = "hello world\nI'm stressed"
    
    mappers = [
        context.call_activity("Mapper", json.dumps((linenumber, line)))
        for linenumber, line in enumerate(file_content.split('\n'))
    ]
    mapresults = yield context.task_all(mappers)
    flatmapresults = reduce(lambda a, b: a+b, mapresults)

    logging.log(logging.INFO, f"Flat map results: {flatmapresults}")
    # shuffleresults = context.call_activity("Shuffle", map(mapresults))

    # reducers = [
    #     context.call_activity("Reducer", group)
    #     for group in shuffleresults
    # ]
    # reduceresults = yield context.task_all(reducers)

    # return reduceresults
    # return shuffleresults
    return mapresults


main = df.Orchestrator.create(orchestrator_function)
