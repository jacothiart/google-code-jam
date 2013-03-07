import copy

SPACE = ' '
LINE_BREAK = '\n'

file = open('H-small-practice.in')
lines = list(file)

CASE_COUNT = int(lines.pop(0))

output_file = open('H-small-practice.out', 'w')


for z in range(0, CASE_COUNT):
	input = lines.pop(0).strip(LINE_BREAK)

	input_list = list(input)
	unique = set(input_list)
	unique_len = len(unique)
	count = int('9' * unique_len)

	i = 1
	val = -1

	m = {
		0: ')',
		1: '!',
		2: '@',
		3: '#',
		4: '$',
		5: '%',
		6: '^',
		7: '&',
		8: '*',
		9: '(',
	}
	print count
	main = True
	
	while i <= count and main:
		s = str(i)
		
		l = []
		
		for v in s:
			l.append(int(v))

		u = set(l)
		#print u
		if len(u) == unique_len:
			# do conversion
			c = input
			
			for k, v in enumerate(l):
				c = c.replace(input_list[k], m[v])
			
			for k, v in enumerate(m):
				c = c.replace(m[v], str(k))
			
			j = 2
			
			while j <= 36:
				# go through all the bases
				try:
					new = int(c, j)
					if new < val or val == -1:
						val = new
						main = False
				except:
					pass
				
				j += 1
			
		i += 1

	line_break = LINE_BREAK
	print z
	if (z + 1) == CASE_COUNT:
		line_break = ''
		
	output_file.write('Case #' + str(z + 1) + ': ' + str(val) + line_break)
	