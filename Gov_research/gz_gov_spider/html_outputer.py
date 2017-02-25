#!/usr/bin/env python
# _*_ encoding:utf-8 _*_

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('fs.html', 'w')
        fout.write("<html>")
        fout.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['title'].encode("utf-8") )
            fout.write("<td>%s</td>" % data['source'].encode("utf-8") )
            fout.write("<td>%s</td>" % str(data['time']).encode("utf-8") )
            fout.write("<td>%s</td>" % data['content'].encode("utf-8") )
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
