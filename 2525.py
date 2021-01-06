timedata = list(map(int,input().split()))
dur = int(input())

hour,minute = timedata
dur_h = dur//60
dur_m = dur%60

if minute+dur_m>=60:
    hour += 1
    minute = minute + dur_m - 60
else:
    minute = minute + dur_m

if hour+dur_h >= 24:
    hour = (hour + dur_h)%24
else:
    hour = hour + dur_h

print(str(hour)+' '+str(minute))