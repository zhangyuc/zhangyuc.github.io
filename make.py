import xml.etree.ElementTree

def span_wrap(text, font_size=18, color='black'):
    return '<span style="FONT-SIZE: ' + str(font_size) + '; COLOR: ' + color + '">'+text+'</span>'

def link_html(text, url):
    return '<a style="text-decoration: none; color: blue" href="' + url + '">' + text +'</a>'

def writeline(line):
    writer.write(line+'<br>\n')

def write_blank_line():
    writeline('&nbsp;')

writer = open('index.html','w')
writer.write('<html>\n')

# include header
reader = open('head.html','r')
writer.write(reader.read())
writer.write('\n')
writer.write('<body style="PADDING-LEFT: 10pt; PADDING-RIGHT: 10pt">\n')

# include introduction
reader = open('intro.html','r')
writer.write(reader.read())
writer.write('\n')

# include papers
root = xml.etree.ElementTree.parse('papers.xml').getroot()

for category in root.iter('category'):
    title = category.findall('name')[0].text
    write_blank_line()
    write_blank_line()
    writeline(span_wrap('<strong>%s</strong>' % title, font_size=25))

    for paper in category.iter('paper'):
        write_blank_line()
        title = paper.findall('title')[0].text
        links = ''
        for link in paper.iter('link'):
            text = link.findall('text')[0].text
            url = link.findall('url')[0].text
            links += ' ['+link_html(text, url)+'] '
        writeline(span_wrap(title, color='#8C1515') + span_wrap(links))

        for authors in paper.iter('authors'):
            authors = str.replace(authors.text, 'Y. Zhang', '<strong>Y. Zhang</strong>')
            writeline(span_wrap(authors, color='#7F7F7F'))

        for journal in paper.iter('journal'):
            text = journal.text
            if (len(paper.findall('award')) == 1):
                text += '&nbsp&nbsp&nbsp&nbsp' + span_wrap('<strong>%s</strong>' % paper.findall('award')[0].text)
            writeline(span_wrap(text, color='#7F7F7F'))

# end of file
write_blank_line()
write_blank_line()
writer.write('</body>\n')
writer.write('</html>\n')
writer.close()
