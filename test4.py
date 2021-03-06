from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table

pdfmetrics.registerFont(TTFont('Gothic','/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'))
psize = portrait(A4)
pwidth, pheight = psize

xmargin = 15.0 * mm
ymargin = 30.0 * mm

c = canvas.Canvas("test4.pdf", pagesize=psize, bottomup=True)
c.setFont('Gothic', 11)
colw = (8.6*mm,11.0*mm, 17.2*mm, 17.2*mm, 17.2*mm, 8.0*mm, 8.0*mm, 14.0*mm, 8.6*mm, 8.6*mm, 13.8*mm, 51.8*mm )
data = [
    ['日\n付','曜\n日','サービス提供実績','','','','','','','','利用者\n確認印','備考'],
    ['','','サービス提供\nの状況','開始時間','終了時間','送迎加算','','`訪問支援特別加算','食料提供\n加算','施設外\n支援','',''],
    ['','','','','','往','復','時間数'],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
table = Table(data, colWidths=colw, rowHeights=7.0*mm)
table.setStyle([
    ('FONT',   ( 0, 0), (-1,-1), 'Gothic', 9),
    ('FONT',   ( 2, 1), ( 2, 1), 'Gothic', 8),
    ('FONT',   ( 7, 1), ( 7, 1), 'Gothic', 5),
    ('FONT',   ( 8, 1), ( 9, 1), 'Gothic', 6),
    ('GRID',   ( 0, 0), (-1,-1), 0.5, colors.black),
    ('BOX',    ( 0, 0), (-1,-1), 1.8, colors.black),
    ('BOX',    ( 0, 0), (-1, 2), 1.8, colors.black),
    ('BOX',    ( 0, 0), ( 1,-1), 1.8, colors.black),
    ('BOX',    (10, 0), (10,-1), 1.8, colors.black),
    ('VALIGN', ( 0, 0), (-1,-1), 'MIDDLE'),
    ('ALIGN',  ( 0, 0), (-1, 2), 'CENTER'),
    ('SPAN',   ( 0, 0), ( 0, 2)),
    ('SPAN',   ( 1, 0), ( 1, 2)),
    ('SPAN',   ( 2, 0), ( 9, 0)),
    ('SPAN',   (10, 0), (10, 2)),
    ('SPAN',   (11, 0), (11, 2)),
    ('SPAN',   ( 2, 1), ( 2, 2)),
    ('SPAN',   ( 3, 1), ( 3, 2)),
    ('SPAN',   ( 4, 1), ( 4, 2)),
    ('SPAN',   ( 5, 1), ( 6, 1)),
    ('SPAN',   ( 8, 1), ( 8, 2)),
    ('SPAN',   ( 9, 1), ( 9, 2))
])
'''
    ('ALIGN', (0,1), (0,32), 'RIGHT'),
    ('ALIGN', (1,0), (3,32), 'CENTER'),
    ('ALIGN', (4,0), (4,32), 'RIGHT'),
    ('ALIGN', (2,33),(4,-1), 'RIGHT'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('SPAN', (0,0),(2,0)),
    ('SPAN', (0,33),(1,-1)),
    ('SPAN', (5,33),(5,-1)),
'''
table.wrapOn(c, xmargin, 42.0*mm)
table.drawOn(c, xmargin, 42.0*mm)

colw=(71.0*mm,16.0*mm,14.0*mm,9.0*mm,11.5*mm,9.0*mm,17.0*mm,36.5*mm)
foot=[
    ['合計','回','回','回','施設外\n支援','当月','日      ',''],
    ['','','','','','累計','日/180日']
]
table = Table(foot, colWidths=colw, rowHeights=4.0*mm)
table.setStyle([
    ('FONT',   ( 0, 0), (-1,-1), 'Gothic', 8),
    ('FONT',   ( 1, 0), ( 3,-1), 'Gothic', 6),
    ('FONT',   ( 6, 0), ( 6,-1), 'Gothic', 6),
    ('GRID',   ( 0, 0), (-1,-1), 0.5, colors.black),
    ('BOX',    ( 0, 0), (-1,-1), 1.8, colors.black),
    ('VALIGN', ( 0, 0), (-1,-1), 'MIDDLE'),
    ('ALIGN',  ( 0, 0), ( 0,-1), 'CENTER'),
    ('ALIGN',  ( 1, 0), ( 3,-1), 'RIGHT'),
    ('ALIGN',  ( 4, 0), ( 5,-1), 'CENTER'),
    ('ALIGN',  ( 6, 0), ( 6,-1), 'RIGHT'),
    ('SPAN',   ( 0, 0), ( 0, 1)),
    ('SPAN',   ( 1, 0), ( 1, 1)),
    ('SPAN',   ( 2, 0), ( 2, 1)),
    ('SPAN',   ( 3, 0), ( 3, 1)),
    ('SPAN',   ( 4, 0), ( 4, 1)),
    ('SPAN',   ( 7, 0), ( 7, 1))
])
table.wrapOn(c, xmargin, 33.2*mm)
table.drawOn(c, xmargin, 33.2*mm)

colw=(28.0*mm,21.5*mm,30.5*mm,21.5*mm,30.5*mm,21.5*mm,30.5*mm)
foot=[
    ['初期加算','利用開始日','','30日目','','当月算定日数','']
]
table = Table(foot, colWidths=colw, rowHeights=6.5*mm)
table.setStyle([
    ('FONT',   ( 0, 0), (-1,-1), 'Gothic', 9),
    ('GRID',   ( 0, 0), (-1,-1), 0.5, colors.black),
    ('BOX',    ( 0, 0), (-1,-1), 1.8, colors.black),
    ('VALIGN', ( 0, 0), (-1,-1), 'MIDDLE'),
    ('ALIGN',  ( 0, 0), (-1,-1), 'CENTER')
])
table.wrapOn(c, xmargin, 25.0*mm)
table.drawOn(c, xmargin, 25.0*mm)

#c.drawString(xmargin, pheight-ymargin, 'Hello World!')
c.showPage()
c.save()
