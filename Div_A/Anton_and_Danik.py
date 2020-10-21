n = int(input())
game = input()
a = game.count('A') ; d = game.count('D')
if a < d :
	print('Danik')
elif a > d:
	print('Anton')
else:
	print('Friendship')