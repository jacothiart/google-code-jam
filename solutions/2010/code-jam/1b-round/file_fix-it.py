import re
import copy

SPACE = ' '
LINE_BREAK = '\n'
D_S = '/'

file = open('A-large-practice.in')
lines = list(file)

CASE_COUNT = int(lines.pop(0))

output_file = open('A-large-practice.out', 'w')

count = 0

i = 0

l = 'z6nou z6nou z6nou aqka1'

m = re.findall('((?<! )z6nou|(?<=z6nou) z6nou|(?<=z6nou z6nou )aqka1)', l)

print m

for i in range(0, CASE_COUNT):
    nm = lines.pop(0).strip(LINE_BREAK).split(SPACE)
	
    n, m = int(nm[0]), int(nm[1])
    exists = []
	
    for	j in range(0, n):
        exists.append(lines.pop(0).strip(LINE_BREAK).lstrip(D_S).replace(D_S, SPACE))
	
    count = 0
	
    for	j in range(n, n + m):
        l = lines.pop(0).strip(LINE_BREAK).lstrip(D_S)
        ll = l.replace(D_S, SPACE)
        l2 = ll.split(SPACE)
        l4 = copy.deepcopy(l2)
		
        c = '((?<! )'
		
        p = l2.pop(0)
		
        c += p
		
        p += SPACE
		
        for k, v in enumerate(l2):
            c += '|(?<=' + p + ')' + l2[k]
            p += l2[k] + SPACE
		
        c += ')'
		
        index = -1
		
        cc = 0
		
        for k, v in enumerate(exists):
            l3 = re.findall(c, exists[k])

            while len(l3) > len(l4):
                l3.pop(len(l3) - 1)

            lll = len(l3)
			
            e = exists[k].split(SPACE)
			
            d = 0
			
            for kk, vv in enumerate(l3):
                if l4[kk] == e[kk]:
                    d += 1
                else:
                    break
					
            if d > cc:
                f = True
				
                if f:
                    cc = d
                    index = k
					
        aa = ll.split(SPACE)
		
        if not index == -1:
            count += len(aa) - cc
        else:
            count += len(aa)

        exists.append(ll)
		
    line_break = LINE_BREAK
	
    if (i + 1) == CASE_COUNT:
        line_break = ''
		
    output_file.write('Case #' + str(i + 1) + ': ' + str(count) + line_break)