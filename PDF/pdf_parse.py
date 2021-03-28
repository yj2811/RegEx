import re

import pdfquery
from lxml import etree


PDF_FILE = 'insulin_pumps.pdf'

pdf = pdfquery.PDFQuery(PDF_FILE)
pdf.load()

product_info = []
page_count = len(pdf._pages)
for pg in range(page_count):
    data = pdf.extract([
        ('with_parent', 'LTPage[pageid="{}"]'.format(pg+1)),
        ('with_formatter', None),
        ('product_name', 'LTTextLineHorizontal:in_bbox("40, 48, 181, 633")'),
    ])

    for ix, pn in enumerate(sorted([d for d in data['product_name'] if d.text.strip()], key=lambda x: x.get('y0'), reverse=True)):
        if ix % 2 == 0:
            product_info.append({'Manufacturer': pn.text.strip(), 'page': pg, 'y_start': float(pn.get('y1')), 'y_end': float(pn.get('y1'))-150})
            if ix > 0:
                product_info[-2]['y_end'] = float(pn.get('y0'))+10.0
        else:
            product_info[-1]['Model'] = pn.text.strip()
            
pdf.file.close()


for p in product_info:
    s = p['Manufacturer']
    m = re.search(r"Tandem",s,re.I)
    if m:
        print('Manufacturer: {}[Model {}]\n'.format(p['Manufacturer'],p['Model']))