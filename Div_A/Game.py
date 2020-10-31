n =int(input())
board = sorted(list(map(int,input().split())))
print(board[(n-1)//2])