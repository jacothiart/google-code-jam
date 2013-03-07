SPACE = ' '
LINE_BREAK = '\n'

file = open('C-large-practice.in')
lines = list(file)

CASE_COUNT = int(lines.pop(0))
CASE_LINE_COUNT = 3
CASE_LINE_TOTAL_COUNT = CASE_COUNT * CASE_LINE_COUNT

for i, line in enumerate(lines):
	lines[i] = line.strip(LINE_BREAK)
		
output_file = open('C-large-practice.out', 'w')

count = 0

i = 0

# keep it integers because sorting strings and reversing strings is not the same

while count < CASE_LINE_TOTAL_COUNT:
	output = 'Case #' + str(i + 1) + ': '
	case_set = range(count, count + CASE_LINE_COUNT)
	
	l1 = [int(v) for v in lines[case_set[1]].split(SPACE)]
	l2 = [int(v) for v in lines[case_set[2]].split(SPACE)]
	
	v1 = sorted(l1)
	v2 = reversed(sorted(l2))
	v3 = [v for k, v in enumerate(v2)]
	
	y = 0
	
	for k, v in enumerate(v1):
		y += v * v3[k]
	
	output += str(y)
	
	line_break = LINE_BREAK
	
	if (i + 1) == CASE_COUNT:
		line_break = ''
	
	output_file.write(output + line_break)
			
	count = count + CASE_LINE_COUNT
	i += 1