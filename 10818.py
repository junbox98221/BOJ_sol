n = int(input())
arr = list(map(int,input().split()))#split은 공백을 기준으로 자름
#map 함수는 iterator 각 원소에 함수를 적용한다!
c = str(min(arr))+' '+str(max(arr))
print(c)