from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from django.utils import timezone
from .models import Coupon

class CouponValidationView(APIView):
    def post(self,request):
        code=request.data.get('code')
        today=timezone.now().data()

        try:
            coupon=Coupon.objects.get(
                code__iexact=code,
                is__active=True,
                valid_from__lte=today,
                valid_until__gte=today
            )

            return Response({
                "valid":True,
                "discount_percentage": coupon.discount_percentage,
                "code":coupon.code
            },status=status.HTTP_200_OK)
        except Coupon.DoesNotExist:
            return Response({
                "valid":False,
                "error":"Invalid or expired coupon code."
            },status=status.HTTP_400_BAD_REQUEST)