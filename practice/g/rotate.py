import copy

SPACE = ' '
LINE_BREAK = '\n'
D_S = '/'
B = 'B'
R = 'R'
DOT = '.'

file = open('G-large-practice.in')
lines = list(file)

CASE_COUNT = int(lines.pop(0))

output_file = open('G-large-practice.out', 'w')

count = 0

i = 0

for i in range(0, CASE_COUNT):
    nk = lines.pop(0).strip(LINE_BREAK).split(SPACE)
    N, K = int(nk[0]), int(nk[1])
	
    xy = []
	
    # gravity first to the right
    for j in range(0, N):
        s = lines.pop(0).strip(LINE_BREAK).replace(DOT, '')
        l = []
		
        for jj in s:
            l.append(jj)
		
        xy.append(l)
	
    for k, v in enumerate(xy):
        while len(xy[k]) < N:
            xy[k].insert(0, DOT)
		
    m = len(xy) - 1
	
    if i == 2:
        print xy
    kk = 0
    xy_temp = copy.deepcopy(xy)
		
	# rotate
    for j in xy:
        for k, v in enumerate(j):
            xy[k][m] = xy_temp[kk][k]
        kk += 1
        m -= 1
	
    m = len(xy) - 1
	
	# check for winners
    y = 0
	
    main = True
    bc = False
    rc = False
	
    while main:
        y = 0
        for j in xy:
            x = 0
            for k, v in enumerate(j):
                if j[k] == B:
                    c = 1
					
					# check upwards
                    yy = y
                    xx = x
                    t = True
					
                    while t:
                        yy -= 1
                        try:
                            if yy < 0:
                                raise
                            if xy[yy][x] == B:
                                c += 1
								
                                if c == K:
                                    bc = True
                            else:
                                raise
                        except:
                            t = False
					
                    c = 1
                    yy = y
                    xx = x
                    t = True
					
                    # check downwards
                    while t:
                        yy += 1
                        try:
                            if xy[yy][x] == B:
                                c += 1
								
                                if c == K:
                                    bc = True
                            else:
                                raise
                        except:
                            t = False
					
                    c = 1
                    yy = y
                    xx = x
                    t = True
                    print 'test'
					# check right
                    while t:
                        xx += 1
                        try:
                            if xy[y][xx] == B:
                                c += 1
                                if c == K:
                                    bc = True
                            else:
                                raise
                        except:
                            t = False
					
                    c = 1
                    yy = y
                    xx = x
                    t = True
					
					# check left
                    while t:
                        xx -= 1
                        try:
                            if xx < 0:
                                raise
                            if xy[y][xx] == B:
                                c += 1
								
                                if c == K:
                                    bc = True
                            else:
                                raise
                        except:
                            t = False
					
                    c = 1
                    yy = y
                    xx = x
                    t = True
					
					# check up left
                    while t:
                        yy -= 1
                        xx -= 1
                        try:
                            if yy < 0 or xx < 0:
                                raise
                            if xy[yy][xx] == B:
                                c += 1
								
                                if c == K:
                                    bc = True
                            else:
                                raise
                        except:
                            t = False
					
                    c = 1
                    yy = y
                    xx = x
                    t = True
					
					# check up right
                    while t:
                        yy -= 1
                        xx += 1
                        try:
                            if yy < 0:
                                raise
                            if xy[yy][xx] == B:
                                c += 1
								
                                if c == K:
                                    bc = True
                            else:
                                raise
                        except:
                            t = False
					
                    c = 1
                    yy = y
                    xx = x
                    t = True
					
					# check down left
                    while t:
                        yy += 1
                        xx -= 1
                        try:
                            if xx < 0:
                                raise
                            if xy[yy][xx] == B:
                                c += 1
								
                                if c == K:
                                    bc = True
                            else:
                                raise
                        except:
                            t = False
					
                    c = 1
                    yy = y
                    xx = x
                    t = True
					
					# check down right
                    while t:
                        yy += 1
                        xx += 1
                        try:
                            if xy[yy][xx] == B:
                                c += 1
								
                                if c == K:
                                    bc = True
                            else:
                                raise
                        except:
                            t = False

                if j[k] == R:
                    c = 1

					# check upwards
                    yy = y
                    xx = x
                    t = True

                    while t:
                        yy -= 1
                        try:
                            if yy < 0:
                                raise
                            if xy[yy][x] == R:
                                c += 1

                                if c == K:
                                    rc = True
                            else:
                                raise
                        except:
                            t = False

                    c = 1
                    yy = y
                    xx = x
                    t = True

                    # check downwards
                    while t:
                        yy += 1
                        try:
                            if xy[yy][x] == R:
                                c += 1

                                if c == K:
                                    rc = True
                            else:
                                raise
                        except:
                            t = False

                    c = 1
                    yy = y
                    xx = x
                    t = True

					# check right
                    while t:
                        xx += 1
                        try:
                            if xy[y][xx] == R:
                                c += 1
                                if c == K:
                                    rc = True
                            else:
                                raise
                        except:
                            t = False

                    c = 1
                    yy = y
                    xx = x
                    t = True

					# check left
                    while t:
                        xx -= 1
                        try:
                            if xx < 0:
                                raise
                            if xy[y][xx] == R:
                                c += 1

                                if c == K:
                                    rc = True
                            else:
                                raise
                        except:
                            t = False

                    c = 1
                    yy = y
                    xx = x
                    t = True

					# check up left
                    while t:
                        yy -= 1
                        xx -= 1
                        try:
                            if yy < 0 or xx < 0:
                                raise
                            if xy[yy][xx] == R:
                                c += 1

                                if c == K:
                                    rc = True
                            else:
                                raise
                        except:
                            t = False

                    c = 1
                    yy = y
                    xx = x
                    t = True

					# check up right
                    while t:
                        yy -= 1
                        xx += 1
                        try:
                            if yy < 0:
                                raise
                            if xy[yy][xx] == R:
                                c += 1

                                if c == K:
                                    rc = True
                            else:
                                raise
                        except:
                            t = False

                    c = 1
                    yy = y
                    xx = x
                    t = True

					# check down left
                    while t:
                        yy += 1
                        xx -= 1
                        try:
                            if xx < 0:
                                raise
                            if xy[yy][xx] == R:
                                c += 1

                                if c == K:
                                    rc = True
                            else:
                                raise
                        except:
                            t = False

                    c = 1
                    yy = y
                    xx = x
                    t = True

					# check down right
                    while t:
                        yy += 1
                        xx += 1
                        try:
                            if xy[yy][xx] == R:
                                c += 1

                                if c == K:
                                    rc = True
                            else:
                                raise
                        except:
                            t = False
                            
                x += 1
            y += 1
			
        main = False
	
    line_break = LINE_BREAK
	
    if (i + 1) == CASE_COUNT:
        line_break = ''
	
    oo = 'Neither'
    if bc:
        oo = 'Blue'
    if rc:
        oo = 'Red'
    if bc and rc:
        oo = 'Both'
		
    output_file.write('Case #' + str(i + 1) + ': ' + str(oo) + line_break)