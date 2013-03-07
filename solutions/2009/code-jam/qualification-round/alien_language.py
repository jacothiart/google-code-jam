import re

SPACE = ' '
LINE_BREAK = '\n'

file = open('A-large-practice.in')
lines = list(file)

l = lines.pop(0).strip(LINE_BREAK).split(SPACE)

L_COUNT, D_COUNT, N_COUNT = int(l[0]), int(l[1]), int(l[2])

D = ''

for i in range(0, D_COUNT):
    D += lines.pop(0).strip(LINE_BREAK) + SPACE

D = D[:len(D) - 1]

#m = re.search('((a|b)(b|c)(c|a))+', 'abcbcadacdbccba')
#m = re.findall(r"((a|b|c)(a|b|c)(a|b|c)+)", 'abc bca dac dbc cba')

output_file = open('A-large-practice.out', 'w')

for i in range(0, N_COUNT):
    n = lines.pop(0).strip(LINE_BREAK)
    nn = ''
	
    a = False
	
    for j in n:
        if j == '(':
            a = True
		
        if j == ')':
            a = False
            nn = nn[:len(nn) - 1]
			
        nn += j
		
        if a and not j == '(' and not j == ')':
            nn += '|'
		
    nn = '(' + nn + ')+'
	#print nn
	
    m = re.findall(nn, D)
	
    line_break = LINE_BREAK
	
    if (i + 1) == N_COUNT:
        line_break = ''
	
    output_file.write('Case #' + str(i + 1) + ': ' + str(len(m)) + line_break)