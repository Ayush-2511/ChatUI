import json
import os

MEMORY_FILE = "memory.json"


if not os.path.exists(MEMORY_FILE):
    
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump([], f)


with open(MEMORY_FILE, "r+", encoding="utf-8") as f:
    content = f.read().strip()


    if not content:
        memory = []
        f.seek(0)
        json.dump(memory, f)
        f.truncate()
    else:
        memory = json.loads(content)
def saveMemory(memory):
    with open("memory.json", "w") as f:
            memory = memory[-30:]
            json.dump(memory,f, indent = 2)