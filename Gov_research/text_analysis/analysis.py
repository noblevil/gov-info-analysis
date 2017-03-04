#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

import jieba
from bs4 import BeautifulSoup
from collections import Counter

def extract_text(url):
    """Extract html content."""
    with open(url, 'r') as f:
       html_cont = f.read()
    soup = BeautifulSoup(html_cont)
    report_text = soup.find_all('td')

    text = ''

    for td in report_text:
        text += td.get_text()
        text += '\n'

    return text

def word_frequency(text,city):
    """count word frequency."""
    words = [word for word in jieba.cut(text, cut_all=True) if len(word) >= 2]
    c = Counter(words)

    datas = []

    for word_freq in c.most_common(30):
        word, freq = word_freq
        data = {}
        data["word"] = word
        data["freq"] = freq
        datas.append(data)


    with open('statistics_' + city + '.html', 'w') as fout:
        fout.write("<html>")
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write("<body>")
        fout.write("<table>")

        for d in datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % d['word'].encode('utf-8'))
            fout.write("<td>%s</td>" % str(d['freq']).encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")


url = '/Users/noblevil/desktop/jm.html'
city = url.lstrip("Users/noblevil/desktop/").rsplit(".html")[0]
text = extract_text(url)
word_frequency(text,city)