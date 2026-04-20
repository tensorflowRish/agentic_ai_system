import asyncio
import json
from llm import call_llm


async def plan_task(user_input: str):

    prompt = f"""
    You are a task planning agent.

    Break this task into steps:
    - step (number)
    - agent (retriever, analyzer, writer)
    - task (string)

    Return ONLY valid JSON array.

    Task: {user_input}
    """

    raw = await call_llm(prompt)

    try:
        plan = json.loads(raw)

    except Exception:
        plan = [
        {"step": 1, "agent": "retriever", "task": user_input},
        {"step": 2, "agent": "analyzer", "task": user_input},
        {"step": 3, "agent": "writer", "task": user_input},
        ]

    return plan