LINE_BREAK = '\n'

file = open('H-small-practice.in')
lines = list(file)

CASE_COUNT = int(lines.pop(0))

output_file = open('H-small-practice.out', 'w')

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
    'a': '~',
    'b': '`',
    'c': '-',
    'd': '_',
    'e': '=',
    'f': '+',
    'g': '\'',
    'h': '|',
    'i': '[',
    'j': '{',
    'k': ']',
    'l': '}',
    'm': ';',
    'n': ':',
    'o': '\'',
    'p': '"',
    'q': ',',
    'r': '<',
    's': '.',
    't': '>',
    'u': '/',
    'v': '?',
}

n = {
    0: 1,
    1: 0,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 'a',
    11: 'b',
    12: 'c',
    13: 'd',
    14: 'e',
    15: 'f',
    16: 'g',
    17: 'h',
    18: 'i',
    19: 'j',
    20: 'k',
    21: 'l',
    22: 'm',
    23: 'n',
    24: 'o',
    25: 'p',
    26: 'q',
    27: 'r',
    28: 's',
    29: 't',
    30: 'u',
    31: 'v',
}

for z in range(0, CASE_COUNT):
    input = lines.pop(0).strip(LINE_BREAK)

    input_list = list(input)
    unique = set(input_list)
    unique_len = len(unique)
    unique_list = []

    i = 1
    val = -1
    l = []
    #print unique_len
    for x in range(0, unique_len):
        l.append(n[x])

    for k, v in enumerate(input_list):
        for kk, vv in enumerate(unique):
            if v == vv:
                unique_list.append(vv)
                unique.remove(vv)
                break
    # do conversion
    c = input
    #print l
    for k, v in enumerate(l):
        c = c.replace(unique_list[k], m[v])
    #print c
    for k, v in enumerate(m):
        print 'replace: ' + m[v] + ' with ' + str(v)
        c = c.replace(m[v], str(v))

    #print c

    j = 2

    while j <= 36:
        # go through all the bases
        try:
            new = int(c, j)
            if new < val or val == -1:
                val = new
        except:
            pass

        j += 1

    line_break = LINE_BREAK

    if (z + 1) == CASE_COUNT:
        line_break = ''

    output_file.write('Case #' + str(z + 1) + ': ' + str(val) + line_break)
