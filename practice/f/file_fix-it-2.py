from distutils import dir_util
import copy
import traceback

SPACE = ' '
LINE_BREAK = '\n'
D_S = '/'

file = open('A-small-practice.in')
lines = list(file)

CASE_COUNT = int(lines.pop(0))

output_file = open('A-small-practice.out', 'w')

count = 0

i = 0

for i in range(0, CASE_COUNT):
    nm = lines.pop(0).strip(LINE_BREAK).split(SPACE)
	
    n, m = int(nm[0]), int(nm[1])
    exists = []
    index = 0
    c = 0
	
    for j in range(0, n):
        if i > 69 and i < 80:
            pass
			#dir_util.mkpath(str(i + 1) + D_S + lines[j].strip(LINE_BREAK).strip(D_S))
		#print str(i + 1) + D_S + lines[j].strip(LINE_BREAK).strip(D_S)
        l = lines[j].strip(LINE_BREAK).lstrip(D_S).split(D_S)
        if len(l) > c:
            c = len(l)
	
    for j in range(n, n + m):
        if i > 69 and i < 80:
            pass
			#dir_util.mkpath(str(i + 1) + D_S + lines[j].strip(LINE_BREAK).strip(D_S))
        l = lines[j].strip(LINE_BREAK).lstrip(D_S).split(D_S)
        if len(l) > c:
            c = len(l)
	
    for d in range(0, c):
        exists.append({})
	
	#populate
    for j in range(0, n):
        l = lines.pop(0).strip(LINE_BREAK).lstrip(D_S).split(D_S)
        parent = ''
		
        for k, v in enumerate(l):
            try:
                exists[k][v]
                if not parent == '':
                    exists[k][v].append(parent)
            except:
                if not parent == '':
                    exists[k][v] = [parent]
                else:
                    exists[k][v] = []
            parent = v
	
    c = 0
	
    for j in range(0, m):
        l = lines.pop(0).strip(LINE_BREAK).lstrip(D_S).split(D_S)
        new = False
        parent = ''
        for k, v in enumerate(l):
            if i == 3:
				#print 'exists: ' + str(exists)
                pass
            try:
                exists[k][v]
					
                if new:
                    c += 1
                else:
                    p = ''
	
                    for kk, vv in enumerate(l):
                        #exists[kk][vv]
#                        if i == 76 and k == 2:
#                            print 'p: ' + str(p)
#                            print 'kk: ' + str(kk)
#                            print 'vv: ' + str(v)
#                            print 'exists[kk][vv]: ' + str(exists[kk][vv])
                        
                        if not p == '' and kk <= k and not p in exists[kk][vv]:
                            c += 1
                            new = True
                            break
                        p = vv
				
                if not parent == '':
                    exists[k][v].append(parent)
                else:
                    exists[k][v] = []
					
				#exists[k][v] = parent
				
            except:
                if not parent == '':
                    exists[k][v] = [parent]
                else:
                    exists[k][v] = []
				#exists[k][v] = parent
                c += 1
                new = True
			
            parent = v
			
            if i == 76:
                pass
                print 'exists:' + str(exists)
                print 'c:' + str(c)
	#print exists
	
    line_break = LINE_BREAK
	
    if (i + 1) == CASE_COUNT:
        line_break = ''
		
    output_file.write('Case #' + str(i + 1) + ': ' + str(c) + line_break)