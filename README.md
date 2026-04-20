Agentic AI System for Multi-Step Tasks

## Overview
This project implements an agentic AI system capable of decomposing complex user tasks into multiple steps and executing them using specialized agents with async orchestration and streaming responses.

## Architecture
Input -> Planner Agent -> Orchestrator -> Agents -> Streaming Output

## Features
.Agent-based architecture (Planner, Retriever, Analyzer, Writer)
.Async task orchestration
.Streaming responses (real-time updates)
.LLM-powered agents (Groq)
.Retry and failure handling
.Modular and extensible design

## Agents
.Planner Agent
    Breaks down user tasks into structured steps.
.Retriever Agent
    Fetches relevent information.
.Analyzer Agent
    Processes and extracts insights.
.Writer Agent
    Generates final output.

## Execution Flow
1. User submits task
2. Planner creates structured steps
3. Orchestrator executes steps sequentially
4. Each agent processes and passes output to next
5. Results streamed back to user

## Setup
pip install fastapi uvicorn python-dotenv groq asyncio
or
pip install -r requirements.txt

Create .env file with content:
    GROQ_API_KEY=your_groq_api_key

Run Server:
    uvicorn main:app --reload

Open API docs: 
    - http://127.0.0.1:8000/docs
    - POST /run-task

        {
        "user_input": "Explain impact of AI on jobs"
        }

## Limitatons
. Uses in-memory queue (not distributed)
. Sequential execution only
. No persistant state or memory

## Future Improvements
. Redis/Kafka integration
. Parallel execution
. Persistant memory layer 
. Real data retrieval APIs