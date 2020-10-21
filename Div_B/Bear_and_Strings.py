def bear(s):
	b =0
	for i in range(len(s)):
		c = s.find('bear' , i)
		if c >=0:
			b+=len(s)-c-3
	return b
if __name__ == '__main__':
	s = input()
	print(bear(s))