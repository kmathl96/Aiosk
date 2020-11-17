from math import sqrt
import heapq

customers = {
    '김영수': {
        '아메리카노': 2,
        '자몽허니블랙티': 3,
        '콜드브루': 3,
        '돌체라떼': 3,
    },
    '박희웅': {
        '아메리카노': 1,
        '카페라떼': 5,
        '콜드브루': 9,
        '카라멜마끼아또': 2,
        '돌체라떼': 5,
    },
    '이경민': {
        '아메리카노': 1,
        '자몽허니블랙티': 7,
        '카페라떼': 17,
        '콜드브루': 8,
        '돌체라떼': 9,
        '카라멜마끼아또': 10,
    },
    '이동옥': {
        '아메리카노': 8,
        '자몽허니블랙티': 8,
        '콜드브루': 3,
        '돌체라떼': 20,
        '녹차' : 2,
    },
    '최동녘': {
        '자몽허니블랙티': 6,
        '카페라떼': 10,
        '돌체라떼': 7,
        '콜드브루': 4,
        '카라멜마끼아또': 3,
    },
    '최수람': {
        '아메리카노': 3,
        '자몽허니블랙티': 4,
        '카페라떼': 2,
        '콜드브루': 3,
        '돌체라떼': 3,
        '카라멜마끼아또': 10,
    },
    '김혜선': {
        '아메리카노': 3,
        '자몽허니블랙티': 4,
        '돌체라떼': 3,
        '콜드브루': 5,
        '카라멜마끼아또': 3,
    },
    '권혁호': {
        '자몽허니블랙티': 10, 
        '카라멜마끼아또': 3,
        '콜드브루': 3
    },
}

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

def getRecommendation(data, person, sim_func=sim_person):
    result = top_match(customers, person)
    
    simSum = 0
    score = 0
    li = []
    score_dic = {}
    sim_dic = {}

    for sim, name in result:
        if sim > 0: continue
        for menu in data[name]:
            if menu not in data[person]:
                score -= sim*data[name][menu]
                score_dic.setdefault(menu, 0)
                score_dic[menu] += score

                sim_dic.setdefault(menu,0)
                sim_dic[menu] -= sim
                
            score = 0

    for key in score_dic:
        score_dic[key] /= sim_dic[key]
        li.append((score_dic[key], key))

    li = list(sorted(li,reverse=True))
    return li

print(getRecommendation(customers, '권혁호'))