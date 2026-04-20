from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import asyncio
import json

from planner import plan_task
from orchestrator import run_workflow

app = FastAPI()

class TaskRequest(BaseModel):
    user_input: str

@app.get("/")
def home():
    return {"message":"Agentic AI System Running"}

def format_event(update):

    event = update.get("event")

    if event == "STEP_STARTED":
        return f"\n Step {update['step']} ({update['agent']}) started...\n"

    elif event == "STEP_COMPLETED":

        output = update.get("output", "")

        short_output = output[:200] + "..." if len(output) > 200 else output

        return f" Step {update['step']} completed\n{short_output}\n"

    elif event == "STEP_FAILED":
        return f"\n Step {update['step']} failed: {update['error']}\n"

    elif event == "WORKFLOW_COMPLETED":
        return f"\n FINAL OUTPUT:\n{update['final_output']}\n"

    return ""

@app.post("/run-task")
async def run_task(request: TaskRequest):
    
    async def event_stream():
        #plan the task
        yield "Planning task...\n"
        plan = await plan_task(request.user_input)

        yield f"Plan created: {plan}\n"

        #Execute workflow
        async for update in run_workflow(plan):
            yield format_event(update)

        yield "Task Completed.\n"

    return StreamingResponse(event_stream(), media_type="text/plain")

