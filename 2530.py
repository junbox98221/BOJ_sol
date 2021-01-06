now = list(map(int,input().split()))
dur = int(input())

dur_s = dur % 60
dur_m = (dur // 60) % 60
dur_h = (dur // 60**2) % 24

now_h,now_m,now_s = now

if now_s+dur_s>=60:
    now_s = (now_s + dur_s) % 60
    now_m += 1
else:
    now_s += dur_s

if now_m + dur_m >= 60:
    now_m = (now_m + dur_m)%60
    now_h += 1
else:
    now_m += dur_m

if now_h + dur_h >= 24:
    now_h = (now_h + dur_h)%24
else:
    now_h += dur_h
print(str(now_h)+' '+str(now_m)+' '+ str(now_s))

