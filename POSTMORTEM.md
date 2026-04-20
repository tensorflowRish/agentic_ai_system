Post-Mortem Document
1. Scaling Issue
    The system currently uses in-memory queue (asyncio.Queue) which limits scalability.
    . Cannot distribute tasks across multiple machines
    . No presistence in case of system failure
    Solution:
    . Replace with Redis or Kafka for distributed task handling.

2. Design Decision to Change
    Currently system uses a sequential execution of agents.
    Limitation:
    . No parallelism
    . Inefficient for independent tasks
    Improvement:
    Implement DAG-based execution to allow parallel agent processing.

3. Trade-offs
    . Used in-memory queue for simplicity and faster development instead of Redis.
    . Used lightweight LLM(Groq, Llama) for faster responses instead of heavier models.
    . Chose sequential execution for clarity and control over data flow.