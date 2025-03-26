from datetime import datetime

def timeuntil(end_time):
    """Calculate remaining time until auction ends."""
    now = datetime.now()

    # Handle both ISO format and standard "%Y-%m-%d %H:%M:%S"
    try:
        end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        end_time = datetime.fromisoformat(end_time)  # This correctly handles '2025-03-04T11:02:06.366109'

    remaining = end_time - now
    
    if remaining.total_seconds() <= 0:
        return "Auction Ended"
    return f"{remaining.days} days, {remaining.seconds // 3600} hours remaining"