from django.utils import timezone
from .modles import DailyOperatingHours

def get_today_operating_hours():
    current_day=timezone.now().strftime('%A')

try:
    hours_entry=DailyOperatingHours.objects.get(day_name=current_day)

    return (hours_entry.open_time,hours_entry.close_time)
except DailyOperatingHours.DoesNotExist:
    return(None,None)