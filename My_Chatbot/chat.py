import os
from agents import Agent,Runner,RunConfig,OpenAIChatCompletionsModel,OpenAIProvider
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
import chainlit as cl

# Load environment variables
load_dotenv(find_dotenv())

# API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# OpenAI-compatible client for Gemini
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)






# Define the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# Configuration
run_Config = RunConfig(
    model=model,
    model_provider= provider,
    tracing_disabled=True
)

# Define your agent
agent1 = Agent(
    name="Assistant",
    instructions="You are a helpful agent"
)

# Run the conversation
result = Runner.run_sync(
    agent1,
    input="tell me te history of pakistan",
    run_config=run_Config,
)

# Print the result
print(result.final_output)




@cl.on_chat_start
async def on_chat_start():
    
    cl.user_session.set("history",[])
    # Send a welcome message
    await cl.Message(content="well come to MR DEKVER WORLD").send()



@cl.on_message
async def handle_message(message: cl.Message):
    
    history = cl.user_session.get("history")

    history.append({
        "role": "user",
        "content": message.content
    })

    # Run sync Runner in a thread
    result = Runner.run_sync(
    agent1,
    input=history,
    run_config=run_Config
)
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    await cl.Message(content=result.final_output).send()

