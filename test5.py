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

c = canvas.Canvas("test5.pdf", pagesize=psize, bottomup=True)
c.setFont('Gothic', 16)
c.drawString(75*mm, 275*mm, '就労継続支援提供実績記録票')

c.setFont('Gothic', 11)
c.drawString(17*mm, 275*mm, '平成30年4月分')


colw = (25.0*mm, 29.5*mm, 32.0*mm, 32.0*mm, 22.0*mm, 43.5*mm)
head =[
    ['受給者証番号','','支給決定障害者氏名','','事業所番号',''],
    ['契約支給量','','','','事業者及び\nその事業所','']
]
table = Table(head, colWidths=colw, rowHeights=10.0*mm)
table.setStyle([
    ('FONT',   ( 0, 0), (-1,-1), 'Gothic', 8),
    ('GRID',   ( 0, 0), (-1,-1), 0.5, colors.black),
    ('BOX',    ( 0, 0), (-1,-1), 1.8, colors.black),
    ('VALIGN', ( 0, 0), (-1,-1), 'MIDDLE'),
    ('ALIGN',  ( 0, 0), (-1,-1), 'CENTER'),
    ('SPAN',   ( 1, 1), ( 3, 1))
])
table.wrapOn(c, xmargin, 252.0*mm)
table.drawOn(c, xmargin, 252.0*mm)

colw = (8.6*mm,11.0*mm, 17.2*mm, 17.2*mm, 17.2*mm, 17.2*mm, 8.0*mm, 8.0*mm, 14.0*mm, 8.6*mm, 8.6*mm, 13.8*mm, 34.6*mm )
data = [
    ['日\n付','曜\n日','サービス提供実績','','','','','','','','','利用者\n確認印','備考'],
    ['','','サービス提供\nの状況','開始時間','終了時間','利用時間','送迎加算','','`訪問支援特別加算','食料提供\n加算','施設外\n就労','',''],
    ['','','','','','','往','復','時間数'],
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
    ('FONT',   ( 8, 1), ( 8, 1), 'Gothic', 5),
    ('FONT',   ( 9, 1), (10, 1), 'Gothic', 6),
    ('GRID',   ( 0, 0), (-1,-1), 0.5, colors.black),
    ('BOX',    ( 0, 0), (-1,-1), 1.8, colors.black),
    ('BOX',    ( 0, 0), (-1, 2), 1.8, colors.black),
    ('BOX',    ( 0, 0), ( 1,-1), 1.8, colors.black),
    ('BOX',    (11, 0), (11,-1), 1.8, colors.black),
    ('VALIGN', ( 0, 0), (-1,-1), 'MIDDLE'),
    ('ALIGN',  ( 0, 0), (-1, 2), 'CENTER'),
    ('SPAN',   ( 0, 0), ( 0, 2)),
    ('SPAN',   ( 1, 0), ( 1, 2)),
    ('SPAN',   ( 2, 0), (10, 0)),
    ('SPAN',   ( 2, 1), ( 2, 2)),
    ('SPAN',   ( 3, 1), ( 3, 2)),
    ('SPAN',   ( 4, 1), ( 4, 2)),
    ('SPAN',   ( 5, 1), ( 5, 2)),
    ('SPAN',   ( 6, 1), ( 7, 1)),
    ('SPAN',   ( 9, 1), ( 9, 2)),
    ('SPAN',   (10, 1), (10, 2)),
    ('SPAN',   (11, 0), (11, 2)),
    ('SPAN',   (12, 0), (12, 2))
])
table.wrapOn(c, xmargin, 32.0*mm)
table.drawOn(c, xmargin, 32.0*mm)

colw=(71.3*mm,17.1*mm,16.0*mm,14.0*mm,8.6*mm,13.6*mm,9.0*mm,34.5*mm)
foot=[
    ['合計','時間','回','回','回','施設外\n支援','当月','日      '],
    ['','','','','','','累計','日      ']
]
table = Table(foot, colWidths=colw, rowHeights=4.0*mm)
table.setStyle([
    ('FONT',   ( 0, 0), (-1,-1), 'Gothic', 8),
    ('FONT',   ( 1, 0), ( 4,-1), 'Gothic', 6),
    ('FONT',   ( 6, 0), ( 6,-1), 'Gothic', 6),
    ('GRID',   ( 0, 0), (-1,-1), 0.5, colors.black),
    ('BOX',    ( 0, 0), (-1,-1), 1.8, colors.black),
    ('VALIGN', ( 0, 0), (-1,-1), 'MIDDLE'),
    ('ALIGN',  ( 0, 0), ( 0,-1), 'CENTER'),
    ('ALIGN',  ( 1, 0), ( 4,-1), 'RIGHT'),
    ('ALIGN',  ( 5, 0), ( 6,-1), 'CENTER'),
    ('ALIGN',  ( 7, 0), ( 7,-1), 'RIGHT'),
    ('SPAN',   ( 0, 0), ( 0, 1)),
    ('SPAN',   ( 1, 0), ( 1, 1)),
    ('SPAN',   ( 2, 0), ( 2, 1)),
    ('SPAN',   ( 3, 0), ( 3, 1)),
    ('SPAN',   ( 4, 0), ( 4, 1)),
    ('SPAN',   ( 5, 0), ( 5, 1))
])
table.wrapOn(c, xmargin, 23.2*mm)
table.drawOn(c, xmargin, 23.2*mm)

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
table.wrapOn(c, xmargin, 15.0*mm)
table.drawOn(c, xmargin, 15.0*mm)

c.showPage()
c.save()
