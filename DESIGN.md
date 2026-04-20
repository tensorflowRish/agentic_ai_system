System Design Document
1. Architecture Overview
    The system follows an agent-based architecture with asynchronous orchestration.

    Components:
    . API Layer (FastAPI)
    . Planner Agent
    . Orchestrator
    . Worker Agents (Retriever, Analyzer, Writer)
    . LLM Layer (Groq)

2. Agent Design
    Each agent has a clearly defined responsibiliy
    . Planner -> Task decomposition
    . Retriever -> Information gathering
    . Analyzer -> Insight extraction
    . Writer -> Final output generation

3. Orchestration
    . Implemented using async pipeline
    . Sequential execution with dependency passing
    . Each agent receives output from previous step

4. Communication
    . Simulated message queue using asyncio.Queue
    . Tasks are processed asynchronously
    . Results stored in in-memory store

5. Streaming
    . Implemented using FastAPI StreamingResponse
    . Sends step-wise updates to user

6. Failure Handling
    . Retry mechanism implemented at agent level
    . Fallback planning in case of LLM failure

7. Scalability Considerations
    Currently:
    . Single-process execution
    . In-memory queue
    In Future:
    . Replace queue with Redis/Kafka
    . Introduce distributed workers
    . Horizontal scaling
