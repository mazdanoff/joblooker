import os
from urllib.parse import urlparse

from conf.path_conf import REPORT_DIR
from utils import today

today = today()

HTML_REPORT_PATH = os.path.join(REPORT_DIR, f'{today}.html')

html_string_start = '''
    <html>
      <head><title>Oferty {0}</title><meta charset="UTF-8"></head>
      <body>
      <h1>Oferty pracy z {0}</h1>
    '''.format(today)

html_string_end = '''
      </body>
    </html>
    '''


def save_as_html(data):

    with open(HTML_REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(html_string_start)
        f.write(f"<h2>Ofert znalezionych: {len(data)}</h2>")
        f.write('<table>')
        for header in ("Nazwa oferty", "Lokalizacja", "Link"):
            f.write('<th>' + str(header) + '</th>')
        for row in data:
            f.write('<tr>')
            f.write('<td>' + str(row[0]) + '</td>')
            f.write('<td>' + str(row[1]) + '</td>')
            f.write(f'<td><a target="_blank" rel="noopener noreferrer" href="{str(row[2])}">' + urlparse(row[2]).netloc + '</a></td>')
            f.write('</tr>')
        f.write('</table>')
        f.write(html_string_end)
