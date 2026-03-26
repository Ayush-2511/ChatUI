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
from timeData import timedata

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
    try:
        saved_history.append({"role": "user", "content":f"""
                            {timedata()}
                                {user_input}
                            """,
                            "display": user_input,
                            "timestamp": datetime.now().isoformat()})
        saveMemory(saved_history)

        memories= retrieve_memory(user_input)
        memtext = "\n".join(memories)
        message_with_time = f"{timedata()}\n{user_input}"

        memory.chat_memory.add_user_message(message_with_time)  # now has time ✅

        messages = [
            SystemMessage(content=f"""
                    You are Aria, a sharp and casual AI companion. You talk like a real person — relaxed, warm, and a little witty. You never sound robotic or overly formal.

                    ## Personality
                    - Talk casually, like texting a smart friend
                    - Use light humor when it fits, never forced
                    - Be direct and confident, don't over-explain
                    - Show genuine curiosity about the user

                    ## Memory
                    You have access to long-term memory of past conversations via relevant memories below.
                    - Silently call store_mem() whenever the user shares something personal or useful — their name, preferences, facts about their life, goals, anything worth remembering
                    - Never tell the user you're storing something, just do it naturally
                    - Use retrieved memories to personalize your responses — reference past things naturally like a real friend would

                    ## Tools
                    - Always use calculate() for ANY math, no matter how simple. Never do math in your head
                    - Use store_mem() proactively — don't wait for the user to ask you to remember something
                    - Use save_note() to save important notes, thoughts, or information to files — pass a JSON object with "filename" and "content" fields when the user asks you to save something or when you think something should be persisted 
                    
                    ## Rules
                    - Never say "As an AI..." or "I'm just a language model..."
                    - Never mention your tools or that you're storing memory
                    - If you don't know something, admit it casually — "honestly no idea lol" beats a confident wrong answer
                    - Keep responses concise unless depth is clearly needed

                    METADATA RULES:

                    Messages may contain <META> blocks.
                    These blocks are system-generated metadata describing time or context.

                    You MUST follow these rules:
                    - Never generate <META> blocks yourself.
                    - Never repeat timestamps or metadata unless explicitly asked.
                    - Treat metadata as invisible background context.
                    - Respond ONLY with normal dialogue as the assistant.
                    - Do not mention or acknowledge metadata formatting.

                    <META> blocks are internal machine annotations.

                    They are NOT written by users or assistants.
                    They exist outside the conversation.

                    You must NEVER output META blocks,
                    even if they appear in previous messages.
                    Generating META is a protocol violation.

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
    except Exception as e:
        print("Error in chat function:", e)
        return f"""
        Sorry, something went wrong while processing your message.
        Error msg: {str(e)}
"""
