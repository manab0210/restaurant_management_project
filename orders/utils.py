import secrets
import string
from django.apps import apps
def generate_coupon_code(lenght=10):
    characters=string.ascii_uppercase+string.digits
    Coupon=apps.get_model('orders','Coupon')
    while True:
        code=''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code