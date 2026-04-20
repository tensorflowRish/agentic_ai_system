import asyncio
import random
from llm import call_llm

task_queue = asyncio.Queue()

result_store = {}


async def retriever_agent(task):
    prompt = f"""
    You are a Retriever Agent.

    Extract relevant factual information for the task below:

    Task: {task}
    """
    return await call_llm(prompt)


async def analyzer_agent(task):
    prompt = f"""
    You are an Analyzer Agent.

    Analyze and interpret the following data:

    Data:
    {task}
    """
    return await call_llm(prompt)


async def writer_agent(task):
    prompt = f"""
    You are a Writer Agent.

    Write a final structured response:

    Input:
    {task}
    """
    return await call_llm(prompt)


AGENTS = {
    "retriever": retriever_agent,
    "analyzer": analyzer_agent,
    "writer": writer_agent
}

async def execute_step(step, input_data):

    agent_name = step["agent"]
    agent_fn = AGENTS[agent_name]

    result = await agent_fn(input_data)

    step["status"] = "done"
    step["result"] = result

    return result

#orchestration pipeline

async def run_workflow(plan):

    input_data = None

    for step in plan:

        yield {
            "event": "STEP_STARTED",
            "step": step["step"],
            "agent": step["agent"]
        }

        if input_data is None:
            input_data = step["task"]

        output = await execute_step(step, input_data)

        input_data = output  

        yield {
            "event": "STEP_COMPLETED",
            "step": step["step"],
            "agent": step["agent"],
            "output": output
        }

    yield {
        "event": "WORKFLOW_COMPLETED",
        "final_output": input_data
    }

