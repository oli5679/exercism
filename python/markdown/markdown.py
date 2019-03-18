import re

def add_headers(line):
    if re.match('###### (.*)', line):
        return '<h6>' + line[7:] + '</h6>'
    elif re.match('## (.*)', line):
        return '<h2>' + line[3:] + '</h2>'
    elif re.match('# (.*)', line):
        return '<h1>' + line[2:] + '</h1>'
    else:
        return '<p>{}</p>'.format(line)


def add_bold(line):
    bold_match = re.match('(.*)__(.*)__(.*)', line)
    if bold_match:
        return bold_match.group(1) + '<strong>' + \
                        bold_match.group(2) + '</strong>' + bold_match.group(3)
    else:
        return line

def add_italic(line):
    italic_match = re.match('(.*)_(.*)_(.*)', line)
    if italic_match:
        return italic_match.group(1) + '<em>' + \
                        italic_match.group(2) + '</em>' + italic_match.group(3)
    else:
        return line


def parse_markdown(markdown):
    lines = markdown.split('\n')
    with_headers = [add_headers(l) for l in lines]
    with_bold = [add_bold(l) for l in with_headers]
    with_italic = [add_italic(l) for l in with_bold]
    return add_unordered_lists(with_italic)

def add_unordered_lists(markdown):
    list_flag = False
    with_list_elements = ''
    for row in markdown:
        list_match = re.match(r'\* (.*)', row)
        if list_match:
            if not list_flag:
                with_list_elements += '<ul>'          
                with_list_elements += ('<li>' + list_match.group(1) + '<\li>')
            list_flag = True

        else:
            if list_flag:
                with_list_elements += '</ul>' + row
                list_flag = False
            else:
                with_list_elements += row

    return with_list_elements
    



def parse_markdown_old(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    for line in lines:
        i = add_headers(line)
        m = re.match(r'\* (.*)', i)
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                    is_italic = True
                i = '<ul><li>' + curr + '</li>'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = m1.group(1) + '<strong>' + \
                        m1.group(2) + '</strong>' + m1.group(3)
                if is_italic:
                    curr = m1.group(1) + '<em>' + m1.group(2) + \
                        '</em>' + m1.group(3)
                i = '<li>' + curr + '</li>'
        else:
            if in_list:
                i = '</ul>'+i
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        res += i
    if in_list:
        res += '</ul>'
    return res
