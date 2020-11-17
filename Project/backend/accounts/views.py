from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .serializers import *
from .models import *
import random, string, http.client

# @api_view(['GET','POST'])
# def coupon(request):
#     if request.method == 'GET': # 쿠폰 개수 확인
#         phone_number = request.GET.get('phone_number')
#         if User.objects.filter(phoneNum=phone_number).exists():
#             user = User.objects.get(phoneNum=phone_number)
#             return Response({
#                 'coupon': Coupon.objects.filter(user=user).count()
#             })
#         return Response({'error': '사용자가 존재하지 않음'})
#     elif request.method == 'POST':
#         phone_number = request.data.get('phone_number')
#         total_qty = request.data.get('total_qty')
#         if User.objects.filter(phoneNum=phone_number).exists():
#             user = User.objects.get(phoneNum=phone_number)
#             # 포인트 적립
#             user.point += total_qty
#             user.save()
#         else: # 처음 적립하는 경우
#             user = User.objects.create(
#                 phoneNum = phone_number,
#                 point = total_qty
#             )
#         # 쿠폰 발급 (10포인트 차감)
#         if user.point >= 10:
#             coupon_cnt = user.point//10
#             user.point -= coupon_cnt*10
#             for i in range(coupon_cnt):
#                 coupon = Coupon.objects.create(
#                     user = user,
#                     code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(settings.COUPON_CODE_LENGTH))
#                 )
#             user.save()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#     return Response({'error': 'http method error'})

@api_view(['POST'])
def coupon(request):
    if request.method == 'POST':
        phone_number = request.data['phone_number']
        # coupon_code = request.GET.get('code')
        user = User.objects.get(phoneNum=phone_number)
        coupon_list = [c.code for c in Coupon.objects.filter(user=user)]
        # serializer = CouponSerializer(data=coupon_list, many=True)
        # serializer.is_valid()
        # return Response(serializer.data)
        return Response({'coupon_list': coupon_list})
        # if Coupon.objects.filter(user=user, code=coupon_code).exists():
        #     return Response({'success': '유효한 쿠폰'})
        # else:
        #     return Response({'error': '유효하지 않은 쿠폰'})       
    # elif request.method == 'POST':
    #     phone_number = request.data.get('phone_number')
    #     user = User.objects.get(phoneNum=phone_number)
    #     coupon_code = request.data.get('code')
    #     if Coupon.objects.filter(user=user, code=coupon_code).exists():
    #         coupon = Coupon.objects.get(user=user, code=coupon_code)
    #         coupon.delete()
    #         serializer = UserSerializer(user)
    #         return Response({'success': '쿠폰 사용'})
    #     else:
    #         return Response({'error': '유효하지 않은 쿠폰'})
    return Response({'error': 'http method error'})

@api_view(['POST'])
def class5(request):
    user = User.objects.get(phoneNum=request.data["phone_num"])
    letter = Class5.objects.get(user=user).letter
    return Response({'letter': letter})