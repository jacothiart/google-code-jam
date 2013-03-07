import timeit
s = """
SPACE = ' '
LINE_BREAK = '\\n'

file = open('B-large-practice.in')
lines = list(file)

n = lines.pop(0)

output_file = open('B-large-practice.out', 'w')

for case, seperated_words in enumerate(lines):
    seperated_words = seperated_words.strip(LINE_BREAK)

    output = 'Case #' + str(case + 1) + ': '

    for word in reversed(seperated_words.split(SPACE)):
        output += word + SPACE

    output = output[:len(output) - 1]

    line_break = LINE_BREAK

    if case == len(lines) - 1:
        line_break = ''

    output_file.write(output + line_break)
"""
t = timeit.Timer(stmt=s,)
print "%.6f usec/pass" % (t.timeit(number=1))
