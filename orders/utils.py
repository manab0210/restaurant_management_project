# from django.utils import timezone
# from .modles import DailyOperatingHours

# def get_today_operating_hours():
#     current_day=timezone.now().strftime('%A')

# try:
#     hours_entry=DailyOperatingHours.objects.get(day_name=current_day)

#     return (hours_entry.open_time,hours_entry.close_time)
# except DailyOperatingHours.DoesNotExist:
#     return(None,None)
    
from django.db.modles import Sum
from .modles import Order

def get_daily_sales_total(date):
    """Calculates total sales for a specific date.
    'date' should be a datetime.date object."""
    daily_orders=Order.objects.filter(created_at__date=date)
    result=daily_orders.aggregate(total_sum=Sum('total_price'))