import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.memory import ConversationBufferMemory
from langchain_core.messages import SystemMessage, AIMessage
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool
from datetime import datetime
from tools import tools
from vectordb import store_memory,retrieve_memory
from memory import memory as saved_history, saveMemory

#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
load_dotenv()

llm = ChatOpenAI(
        model="stepfun/step-3.5-flash:free",  # any model available on openrouter
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
                )

agent = create_react_agent(
        model=llm,
        tools=tools
        )
#---------------------------------------------------------------------------#
#---------------------------------------------------------------------------#
memory = ConversationBufferMemory(return_messages=True)

for msg in saved_history:
    if msg["role"] == "user":
        memory.chat_memory.add_user_message(msg["content"])
    elif msg["role"] == "ai":
        memory.chat_memory.add_ai_message(msg["content"])
def chat(user_input):
    saved_history.append({"role": "user", "content": user_input})
    saveMemory(saved_history)

    memories= retrieve_memory(user_input)
    memtext = "\n".join(memories)
    memory.chat_memory.add_user_message(user_input)

    messages = [
        SystemMessage(content=f"""
        You are a helpful casual assistant that talks in english
        Always and only use the calculator tool for calculations                    
        relevant Memories:
        {memtext}
                    """),
        *memory.chat_memory.messages
    ]
    
    result = agent.invoke({"messages": messages})

    ai_msg = result["messages"][-1].content

    # print("AI:", ai_msg)
    saved_history.append({"role": "ai", "content": ai_msg})
    saveMemory(saved_history)

    memory.chat_memory.add_ai_message(ai_msg)

    return ai_msg
