from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .serializers import *
from .models import *
from accounts.models import *
from decouple import config
import requests, json, random, string
import tensorflow.compat.v1 as tf, sys
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
import numpy as np
import time
import datetime
from PIL import Image
import os, cv2, glob, dlib
import base64
from django.core.files.base import ContentFile
from math import sqrt
import heapq


# Create your views here.
@api_view(['POST'])
def pay(request):
    if request.method == 'POST':
        # 주문 내역 저장
        print(request.data)
        menus = request.data['menu']
        total_price = request.data['total_price']
        user_age = request.data['age']
        coupons = request.data['used_coupon']
        
        m = datetime.datetime.today().month
        if 3 <= m < 6:
            season = Season.objects.get(name='spring')
        elif 6 <= m < 9:
            season = Season.objects.get(name='summer')
        elif 9 <= m < 12:
            season = Season.objects.get(name='autumn')
        else:
            season = Season.objects.get(name='winter')


        virtualUser = VirtualUser.objects.get(age=user_age)
        total_qty = sum([menus[k] for k in menus.keys()])
        # 카카오페이 결제
        if request.data['use_kakao']:
            url = "https://kapi.kakao.com"
            headers = {
                'Authorization': "KakaoAK " + config('KAKAO_ADMIN_KEY'),
                'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
            }
            params = {
                'cid': "TC0ONETIME",
                'partner_order_id': 'aiosk',
                'partner_user_id': str(virtualUser.pk),
                'item_name': "baverage",
                'quantity': total_qty,
                'total_amount': total_price,
                'tax_free_amount': 0,
                'approval_url': 'http:/localhost:3000/final',
                'fail_url': 'http://localhost:3000/pay',
                'cancel_url': 'http://localhost:3000/pay',
            }
            response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
            response = json.loads(response.text)
            if 'tid' in response: # 카카오페이 결제 성공
                phone_number = request.data.get('phone_number')
                if User.objects.filter(phoneNum=phone_number).exists():
                    user = User.objects.get(phoneNum=phone_number)
                    # 포인트 적립
                    user.point += (total_qty-len(coupons))
                    user.save()
                else: # 처음 적립하는 경우
                    user = User.objects.create(
                        phoneNum = phone_number,
                        point = total_qty
                    )
                # 쿠폰 발급 (10포인트 차감)
                if user.point >= 10:
                    coupon_cnt = user.point//10
                    user.point -= coupon_cnt*10
                    for i in range(coupon_cnt):
                        code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(settings.COUPON_CODE_LENGTH))
                        coupon = Coupon.objects.create(
                            user = user,
                            code = code 
                        )
                        # api.send_sms(body=f'{code}', from_phone='+821012345678', to=[f'+82{phone_number[1:]}'])
                        
                        # message = SmsMessage(body=f'{code}', from_phone='+8201012345678', to=['+82{}'.format(phone_number)])
                        # message.send()
                    user.save()
                for coupon_code in coupons:
                    coupon = Coupon.objects.get(user=user, code=coupon_code)
                    coupon.delete()
                order = Order.objects.create(
                    virtual_user = virtualUser,
                    price = total_price
                )
                for menu_name in menus.keys():
                    Detail.objects.create(
                        menu = Menu.objects.get(name=menu_name),
                        amount = menus[menu_name],
                        order = order
                    )
                    
                for menu_name in menus.keys():
                    menu = Menu.objects.get(name=menu_name)
                    if History.objects.filter(user=user, menu=menu).exists():
                        history = History.objects.get(user=user, menu=menu)
                        history.count += menus[menu_name]
                        history.save()
                    else:
                        History.objects.create(
                            user = user,
                            menu = menu,
                            count = menus[menu_name],
                            season = season
                        )
            return Response(response)
        else: # 카드 결제
            phone_number = request.data.get('phone_number')
            if User.objects.filter(phoneNum=phone_number).exists():
                user = User.objects.get(phoneNum=phone_number)
                # 포인트 적립
                user.point += (total_qty-len(coupons))
                user.save()
            else: # 처음 적립하는 경우
                user = User.objects.create(
                    phoneNum = phone_number,
                    point = total_qty
                )
            # 쿠폰 발급 (10포인트 차감)
            if user.point >= 10:
                coupon_cnt = user.point//10
                user.point -= coupon_cnt*10
                for i in range(coupon_cnt):
                    code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(settings.COUPON_CODE_LENGTH))
                    coupon = Coupon.objects.create(
                        user = user,
                        code = code 
                    )
                    # api.send_sms(body=f'{code}', from_phone='+821012345678', to=[f'+82{phone_number[1:]}'])
                    # message = SmsMessage(body=f'{code}', from_phone='+8201012345678', to=['+82{}'.format(phone_number)])
                    # message.send()
                user.save()
            for coupon_code in request.data.get('used_coupon'):
                coupon = Coupon.objects.get(user=user, code=coupon_code)
                coupon.delete()
            order = Order.objects.create(
                virtual_user = virtualUser,
                price = total_price
            )
            for menu_name in menus.keys():
                menu = Menu.objects.get(name=menu_name)
                Detail.objects.create(
                    menu = Menu.objects.get(name=menu_name),
                    amount = menus[menu_name],
                    order = order
                )
                if VirtualHistory.objects.filter(user=virtualUser, menu=menu, season=season).exists():
                    history = VirtualHistory.objects.get(user=virtualUser, menu=menu, season=season)
                    history.count += menus[menu_name]
                    history.save()
                else:
                    VirtualHistory.objects.create(
                        user = virtualUser,
                        menu = menu,
                        count = menus[menu_name],
                        season = season
                    )
                if History.objects.filter(user=user, menu=menu, season=season).exists():
                    history = History.objects.get(user=user, menu=menu, season=season)
                    history.count += menus[menu_name]
                    history.save()
                else:
                    History.objects.create(
                        user = user,
                        menu = menu,
                        count = menus[menu_name],
                        season = season
                    )
            return Response({'success': '카드 결제 성공'})
        order.delete()
        return Response({'error': '결제 실패'})
    return Response({'error': 'http method error'})

@api_view(['GET'])
def menu_list(request):
    menu_list = Menu.objects.all()
    serializer = MenuSerializer(data=menu_list, many=True)
    serializer.is_valid()
    return Response(serializer.data)


''' AI --------------------------------------------------------------------------------------------------------------- '''

def change_grayscale(path, x1, y1, x2, y2):
    temp = Image.open(path)
    temp_numpy = np.array(temp, 'uint8')
    temp_numpy = temp_numpy[y1:y2, x1:x2]
    try:
        gray = cv2.cvtColor(temp_numpy, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(path, gray)
    except:
        return temp

def face_detector(path):
    img = cv2.imread(path)
    detector = dlib.get_frontal_face_detector()
    faces = detector(img)
    x1, y1 = 0, 0
    y2, x2 = img.shape[:2]
    for face in faces:
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
    return x1, y1, x2, y2

def create_graph():
    """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
    # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
    with tf.gfile.FastGFile('/ai/tmp/output_graph.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

def run_inference_on_image(imagePath):
    answer = None
    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    create_graph()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-5:][::-1]  # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.
        f = open('/ai/tmp/output_labels.txt', 'rb') 
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            #print('%s (score = %.5f)' % (human_string, score))

        answer = labels[top_k[0]]
        #print(answer)
        return answer    

@api_view(['POST'])
def detect_age(request):
    print(request.data)
    config = ConfigProto()
    config.gpu_options.allow_growth = True
    session = InteractiveSession(config=config)
    image_string = request.data['files']
    val, imgstr = image_string.split(';base64,')
    imageData = base64.b64decode(imgstr)
    detect = Detection()
    image_name = datetime.datetime.now().isoformat()[-6:] + ".jpeg"
    detect.images = ContentFile(imageData, image_name)
    detect.save()
    print('hello')
    x1,y1,x2,y2 = face_detector("/backend/media/images/" + image_name)
    print('hi')
    image = change_grayscale("/backend/media/images/" + image_name, x1, y1, x2, y2)
    print('bye')
    # change_grayscale(imagePath)
    answer = run_inference_on_image("/backend/media/images/" + image_name)
    detect.delete()
    return Response({'answer': answer[2:-3]})
 

# recommend

def sim_person(data, name1, name2):
    sumX = 0    # X의 합
    sumY = 0    # Y의 합 
    sumPowX = 0 # X 제곱의 합
    sumPowY = 0 # Y 제곱의 합
    sumXY = 0   # X*Y의 합
    count = 0   # 메뉴 개수

    for i in data[name1]:
        if i in data[name2]:
            sumX += data[name1][i]
            sumY += data[name2][i]
            sumPowX += pow(data[name1][i], 2)
            sumPowY += pow(data[name2][i], 2)
            sumXY += data[name1][i] * data[name2][i]
            count += 1

    try:
        return (sumXY - ((sumX * sumY) / count) ) / sqrt((sumPowX - (pow(sumX,2) / count)) * (sumPowY - (pow(sumY,2) / count)))
    except ZeroDivisionError: # 중복 되는 아이템의 모든 횟수가 동일하다면 유사도 검출을 적용할 수 없다..
        return 0

def top_match(data, name, sim_func=sim_person):
    match = []
    for i in data:
        if name != i:
            heapq.heappush(match, (-sim_func(data, name, i), i))
    return list(match)

@api_view(['POST'])
def get_recommendation(request):
    print(request.data)
    customers = {}
    N = 6   # AI 기반 메뉴 추천 개수

    m = datetime.datetime.today().month
    if 3 <= m < 6:
        season = Season.objects.get(name='spring')
    elif 6 <= m < 9:
        season = Season.objects.get(name='summer')
    elif 9 <= m < 12:
        season = Season.objects.get(name='autumn')
    else:
        season = Season.objects.get(name='winter')
    
    ### Virtual User 기반 추천 ###
    # phone_number를 입력하지 않거나
    # 모든 메뉴를 먹어보거나
    # 3가지 미만의 메뉴를 먹어본 고객 대상
    menu_count = Menu.objects.all().count() - 1
    if User.objects.filter(phoneNum=request.data['phone_number']).exists():
        me = User.objects.get(phoneNum=request.data['phone_number'])
        is_user = True
    else: is_user = False
    ### 개인 추천 ###
    if is_user and 3 < History.objects.filter(user=User.objects.get(phoneNum=request.data['phone_number']), season=season).count() < menu_count:
        me = User.objects.get(phoneNum=request.data['phone_number'])
        if History.objects.filter(user=me,season=season).count() > 2:
            recommend1 = History.objects.filter(user=me,season=season).order_by('-count').values()[0]
        else: recommend1 = History.objects.filter(user=me).order_by('-count').values()[0]
        recommend2 = History.objects.filter(user=me).order_by('-updated_at').values()[0]
        recommend = [Menu.objects.get(id=recommend1['menu_id']), Menu.objects.get(id=recommend2['menu_id'])]
        for user in User.objects.all():
            histories = History.objects.filter(user=user)
            customers[user.phoneNum] = {}
            for history in histories:
                if history.menu.name not in customers[user.phoneNum].keys():
                    customers[user.phoneNum][history.menu.name] = history.count
                else: 
                    customers[user.phoneNum][history.menu.name] += history.count
        result = top_match(customers, me.phoneNum)
        simSum = 0
        score = 0
        li = []
        score_dic = {}
        sim_dic = {}

        for sim, name in result:
            if sim > 0: continue
            for menu in customers[name]:
                if menu not in customers[me.phoneNum]:
                    score -= sim*customers[name][menu]
                    score_dic.setdefault(menu, 0)
                    score_dic[menu] += score

                    sim_dic.setdefault(menu,0)
                    sim_dic[menu] -= sim
                    
                score = 0

        for key in score_dic:
            score_dic[key] /= sim_dic[key]
            li.append((score_dic[key], key))

        li = list(sorted(li,reverse=True))
        for i in range(min(4,len(li))):
            recommend.append(Menu.objects.get(name=li[i][1]))
        recommend_serializer = MenuSerializer(data=recommend, many=True)
        recommend_serializer.is_valid()

        return Response(recommend_serializer.data)
    else:
        me = VirtualUser.objects.get(age=request.data['age'])
        histories = VirtualHistory.objects.filter(user=me,season=season).order_by('-count')
        result = histories.values()[:N]
        recommend_list = [Menu.objects.get(id=menu['menu_id']) for menu in result]
        serializer = MenuSerializer(data=recommend_list, many=True)
        serializer.is_valid()
        return Response(serializer.data)

### crontab ###
def recommendation():

    for r in Recommend.objects.all():
        r.delete()
    
    N = 6   # AI 기반 메뉴 추천 개수
    menu_count = Menu.objects.all().count() - 1

    # 현재 시즌
    m = datetime.datetime.today().month
    if 3 <= m < 6:
        season = Season.objects.get(name='spring')
    elif 6 <= m < 9:
        season = Season.objects.get(name='summer')
    elif 9 <= m < 12:
        season = Season.objects.get(name='autumn')
    else:
        season = Season.objects.get(name='winter')
    
    for me in User.objects.all():
        # 3가지 이상 먹어봤으면서 전체 메뉴는 먹어보지 못한 고객 대상
        if 2 < History.objects.filter(user=me).count() < menu_count:

            ### best & latest ###
            # 해당 시즌에 2가지 이상 먹어봤다면 그 시즌에 맞게 추천
            if History.objects.filter(user=me,season=season).count() > 1:
                histories = History.objects.filter(user=me,season=season)
            else: histories = History.objects.filter(user=me)
            best = histories.order_by('-count').values()[0]
            tmp = histories.order_by('-updated_at').values()
            if tmp[0] == best: latest = tmp[1]
            else: latest = tmp[0]
            recommend = [Menu.objects.get(id=best['menu_id']), Menu.objects.get(id=latest['menu_id'])]

            ### RECOMMENDATION ###
            customers = {}
            for user in User.objects.all():
                histories = History.objects.filter(user=user)
                customers[user.phoneNum] = {}
                for history in histories:
                    if history.menu.name not in customers[user.phoneNum].keys():
                        customers[user.phoneNum][history.menu.name] = history.count
                    else: 
                        customers[user.phoneNum][history.menu.name] += history.count
            result = top_match(customers, me.phoneNum)
            simSum = 0
            score = 0
            li = []
            score_dic = {}
            sim_dic = {}

            for sim, name in result:
                if sim > 0: continue
                for menu in customers[name]:
                    if menu not in customers[me.phoneNum]:
                        score -= sim*customers[name][menu]
                        score_dic.setdefault(menu, 0)
                        score_dic[menu] += score

                        sim_dic.setdefault(menu,0)
                        sim_dic[menu] -= sim
                        
                    score = 0

            for key in score_dic:
                score_dic[key] /= sim_dic[key]
                li.append((score_dic[key], key))

            li = list(sorted(li,reverse=True))
            # 1
            for i in range(min(N-2,len(li))):
                recommend.append(Menu.objects.get(name=li[i][1]))
            for r in recommend:
                Recommend.objects.create(
                    user = me,
                    menu = r
                )
            # 2
            # for i in range()
            #     recommend.append(Menu.objects.get(name=li[i][1]))
            # for r in recommend:
            #     Recommend.objects.create(
            #         user = me,
            #         menu = r
            #     )
        
    for r in Recommend.objects.all():
        print(r)