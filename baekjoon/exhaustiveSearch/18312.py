n, k = map(int, input().split())

cnt = 0
for hour in range(n+1):
    if hour < 10:
        hour = '0' + str(hour)
    for min in range(60):
        if min < 10:
            min = '0' + str(min)
        for sec in range(60):
            if sec < 10:
                sec = '0' + str(sec)
            if str(k) in str(hour) or str(k) in str(min) or str(k) in str(sec):
                cnt += 1
print(cnt)

'''
bronze 2
주의: k가 0일때 앞에 0이 없으면 0이 포함된 시간을 제대로 카운트할 수 없다.
'''