SPACE = ' '
LINE_BREAK = '\n'

file = open('A-large-practice.in')
lines = list(file)

CASE_COUNT = int(lines.pop(0))
CASE_LINE_COUNT = 3
CASE_LINE_TOTAL_COUNT = CASE_COUNT * CASE_LINE_COUNT

for i, line in enumerate(lines):
	lines[i] = line.strip(LINE_BREAK)
		
output_file = open('A-large-practice.out', 'w')

count = 0
i = 0

while count < CASE_LINE_TOTAL_COUNT:
    output = 'Case #' + str(i + 1) + ': '
    case_set = range(count, count + CASE_LINE_COUNT)
    c = lines[case_set[0]]
    p = lines[case_set[2]]
    l = list(p.split(SPACE))
    d = {}
    for k, v in enumerate(l):
        d[v] = k
    dd = {}
    for k, v in enumerate(reversed(l)):
        dd[v] = len(l) - k - 1

    e = enumerate(l)

    for k, v in e:
        m = str(int(c) - int(v))
        try:
            line_break = LINE_BREAK

            kk = k + 1
            s = int(d[m]) + 1

            if kk == s:
                # check if the current dict match the reverse, if so raise because it is the same number used twice
                if d[m] == dd[m]:
                    raise
                else:
                    s = int(dd[m]) + 1

            output += str(kk) + SPACE + str(s)

            if (i + 1) == CASE_COUNT:
                line_break = ''

            output_file.write(output + line_break)

            break
        except:
            pass

    count = count + CASE_LINE_COUNT
    i += 1