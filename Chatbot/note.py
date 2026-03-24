import json
import os

def saveNote(json_data):
    try:
        data = json.loads(json_data)
        n = 1
        while os.path.exists(os.path.join(dir, filename if n == 1 else f"{filename.replace('.txt', '')}({n}).txt")):
            n += 1
        filename = data.get('filename', 'notes')
        content = data.get('content')
        
        
        dir = 'Notes'
        os.makedirs(dir, exist_ok=True)
        filename = ''.join(char if char not in r'<>:"/\|?*' else '_' for char in filename)
        filename = filename if filename.endswith('.txt') else f"{filename}.txt"
        filepath = os.path.join(dir, filename)
        with open(filepath, 'w') as file:
            file.write(content)
        print(f"Note saved successfully as {filepath}")

        return {"status": "success", "filepath": f"{filepath}"}

    except Exception as e:
        print("Invalid JSON data")
        return {"status": "error", "error": str(e)}