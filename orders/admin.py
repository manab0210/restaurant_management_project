from django.contrib import admin
from .models import Order
@admin.action(description="Mark selected orders as Processed")
def mark_orders_processed(modeladmin,request,queryset):
    wpdated_count=queryset.update(status='Processed')
    modeladmin.message_user(request,f"Successfully marked {updated_count} orders as Processed.")
class OrderAdmin(admin.ModelsAdmin):
    list_display=['id','customer_name','status','created_at']
    actions=[mark_orders_processed]
admin.site.register(Order,OrderAdmin)