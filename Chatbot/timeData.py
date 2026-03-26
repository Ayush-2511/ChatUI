from datetime import datetime
from memory import memory
def timedata():
    now = datetime.now()
    human_time = now.strftime("%A, %B %d, %Y %I:%M %p")
    

    if len(memory) >= 2:
        last_timestamp = memory[-2].get("timestamp")
    else:
        last_timestamp = None

    if last_timestamp:
        previous = datetime.fromisoformat(last_timestamp)
        delta = now-previous

        seconds = int(delta.total_seconds())
        minutes = seconds//60
        hours = minutes//60

        time_gap = f"{hours} hours {minutes%60} minutes {seconds%60} seconds"

    else:
        time_gap = "first message"

    
    metadata = f"""
        <META>
        timestamp: {human_time}
        timegap: {time_gap}
        </META>
        """
    return metadata