from datetime import datetime
def is_restaurant_open():
    now=datetime.now()
    current_day=now.strftime('%A')
    current_time=now.time()
    schedule={
        'Monday':(9,0,22,0),
        'Tuesday':(9,0,22,0),
        'Wednesday':(9,0,22,0),
        'Thursday':(9,0,22,0),
        'Friday':(9,0,23,0),
        'Saturday':(10,0,23,0),
        'Sunday':(10,0,21,0),
    }
    start_h,start_m,end_h,end_m=schedule.get(current_day)
    from datetime import time
    opening_time=time(start_h,start_m)
    closing_time=time(end_h,end_m)
    if opening_time<=current_time<=closing_time:
        return True
    return False