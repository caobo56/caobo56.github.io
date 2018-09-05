#!/usr/bin/python


def brainfuck_sum(l):
    res = ''
    if l['key'] == '+-':
        if l['value'] > 0:
            res = '*p += ' + str(l['value']) + ';\n'
        elif l['value'] < 0:
            res = '*p -= ' + str(-l['value']) + ';\n'
    elif l['key'] == '<>':
        if l['value'] < 0:
            res = 'p -= ' + str(-l['value']) + ';\n'
        elif l['value'] > 0:
            res = 'p += ' + str(l['value']) + ';\n'
    else:
        pass
    return res


def brainfuck_add(i):
    r = ''
    if i == ',':
        r = "*p = getchar();\n"
    elif i == '.':
        r = "putchar(*p);\n"
    elif i == '[':
        r = "if (*p) do {\n"
    elif i == ']':
        r = "} while (*p);\n"
    else:
        pass
    return r


def brainfuck_retract(i, p):
    r = ''
    p_count_l = p[0:i].count('[')
    p_count_r = p[0:i+1].count(']')
    p_count = p_count_l - p_count_r
    for t in range(p_count):
        r += '  '
    return r


def brainfuck_replace(p):
    while '+-' in p or '-+' in p or '<>' in p or '><' in p or '[]' in p:
        p = p.replace('+-', '').replace('-+', '').replace('<>', '').replace('><', '').replace('[]', '')
    return p


def brainfuck_to_c(source_code):
    p = source_code
    print(p)
    for i in p:
        if i not in ['+', '-', '<', '>', '.', ',', '[', ']']:
            p = p.replace(i, '')
    p = brainfuck_replace(p)
    if '[' in p or ']' in p:
        if p.count('[') != p.count(']') or p.index('[') > p.index(']'):
            return 'Error!'
    if p == '':
        return ''
    r = ''
    l = {'key': '', 'value': 0}
    for i in range(len(p)):
        if p[i] in '+-':
            if l['key'] != '+-':
                r += brainfuck_sum(l)
                l['key'] = '+-'
                l['value'] = 0
            l['value'] += (1 if (p[i] == '+') else -1)
        elif p[i] in '<>':
            if l['key'] != '<>':
                r += brainfuck_sum(l)
                l['key'] = '<>'
                l['value'] = 0
            l['value'] += (-1 if (p[i] == '<') else 1)
        elif p[i] in ['.', ',', '[', ']']:
            r += brainfuck_retract(i, p)
            r += brainfuck_add(p[i])
    if l['value'] != 0:
        r += brainfuck_sum(l)
    return r


print(brainfuck_to_c('[<<++-->>]'))
