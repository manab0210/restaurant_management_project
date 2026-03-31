from datetime import datetime

def is_restaurant_open():
    """
    Checks if the restaurant is currently open based on hardcoded operating hours.
    Returns:
        bool: True if open, False otherwise.
    """
    # 1. Get the current local day and time
    now = datetime.now()
    current_day = now.strftime('%A')  # e.g., 'Monday'
    current_time = now.time()

    # 2. Define example opening hours
    # Format: 'Day': (start_hour, start_minute, end_hour, end_minute)
    # Using 24-hour format for easier comparison
    schedule = {
        'Monday': (9, 0, 22, 0),    # 9:00 AM - 10:00 PM
        'Tuesday': (9, 0, 22, 0),
        'Wednesday': (9, 0, 22, 0),
        'Thursday': (9, 0, 22, 0),
        'Friday': (9, 0, 23, 0),   # 9:00 AM - 11:00 PM
        'Saturday': (10, 0, 23, 0), # 10:00 AM - 11:00 PM
        'Sunday': (10, 0, 21, 0),   # 10:00 AM - 9:00 PM
    }

    # 3. Get the hours for today
    start_h, start_m, end_h, end_m = schedule.get(current_day)

    # 4. Create time objects for the boundaries
    from datetime import time
    opening_time = time(start_h, start_m)
    closing_time = time(end_h, end_m)

    # 5. Check if current time is within the range
    if opening_time <= current_time <= closing_time:
        return True
    
    return False