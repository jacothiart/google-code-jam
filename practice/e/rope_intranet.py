SPACE = ' '
LINE_BREAK = '\n'

file = open('E-small-practice.in')
lines = list(file)

CASE_COUNT = int(lines.pop(0))

output_file = open('E-small-practice.out', 'w')

count = 0

i = 0

#r = int(lines.pop(0))

for i in range(0, CASE_COUNT):
    r = int(lines.pop(0))

    l = []

    for j in range(0, r):
        l.append(lines.pop(0).strip(LINE_BREAK).split(SPACE))

    c = 0

    # bubble sort in python on n number of lists
    while len(l) > 1:
        ll = l.pop(0)

        for k, v in enumerate(l):
            if (int(ll[0]) > int(v[0]) and int(ll[1]) < int(v[1])) or (int(ll[0]) < int(v[0]) and int(ll[1]) > int(v[1])):
                c += 1

    line_break = LINE_BREAK

    if (i + 1) == CASE_COUNT:
        line_break = ''

    output_file.write('Case #' + str(i + 1) + ': ' + str(c) + line_break)