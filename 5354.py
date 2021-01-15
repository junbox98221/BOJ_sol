import sys
data  = []
for i in range(int(sys.stdin.readline())):
    data.append(int(sys.stdin.readline()))
for J in data:
    if J != 1:
        print('#'*J)
        print('#{}#\n'.format('J'*(J-2))*(J-2),end = '')
        if J == data[-1]:
            print('#' * J)
        else:
            print('#' * J, end='\n\n')
    else:
        if J == data[-1]:
            print('#')
        else:
            print('#', end='\n\n')