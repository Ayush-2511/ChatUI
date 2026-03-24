import json
import os

def saveNote(json_data):
    try:
        dir = 'Notes'
        data = json.loads(json_data)
        filename = data.get('filename', 'notes')
        n = 1
        while os.path.exists(os.path.join(dir, filename if n == 1 else f"{filename.replace('.txt', '')}({n}).txt")):
            n += 1
        
        content = data.get('content')
        
        
        
        os.makedirs(dir, exist_ok=True)
        filename = ''.join(char if char not in r'<>:"/\|?*' else '_' for char in filename)
        filename = filename if filename.endswith('.txt') else f"{filename}.txt"
        filepath = os.path.join(dir, filename)
        with open(filepath, 'w') as file:
            file.write(content)
        print(f"Note saved successfully as {filepath}")

        return {"status": "success", "filepath": f"{filepath}"}

    except Exception as e:
        return {"status": "error", "error": str(e)}
    
if __name__ == "__main__":
    sample_json = json.dumps({
        "filename": "meeting_notes.txt",
        "content": "Meeting at 3 PM with the team to discuss project updates."
    })
    print(saveNote(sample_json))