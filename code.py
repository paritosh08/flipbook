import sys
from fpdf import FPDF
from PIL import Image

f = open(sys.argv[1], "r")
form = f.readline().strip()
dimPg = [int(i) for i in f.readline().strip().split(" ")]
pgs = []
fName = []
dimImg = []
src = []
dest = []
for x in f:
	tmp = x.strip().split(" ")
	pgs.append((int(tmp[0]),int(tmp[1])))
	fName.append(tmp[2])
	dimImg.append((int(tmp[3]),int(tmp[4])))
	src.append((int(tmp[5]),int(tmp[6])))
	dest.append((int(tmp[7]),int(tmp[8])))
f.close()

mxPg = 0
for pg in pgs:
	if pg[1]>mxPg:
		mxPg = pg[1]
xS = [[-1]*mxPg for i in range(len(fName))]
yS = [[-1]*mxPg for i in range(len(fName))]
for i in range(len(fName)):
	startX = src[i][0]
	startY = src[i][1]
	endX = dest[i][0]
	endY = dest[i][1]
	x = startX
	y = startY
	pgSt = pgs[i][0]
	pgEn = pgs[i][1]
	stepX = (endX-startX)/(pgEn-pgSt)
	stepY = (endY-startY)/(pgEn-pgSt)
	for j in range(pgSt-1,pgEn):
		xS[i][j] = int(x)
		yS[i][j] = int(y)
		x = x + stepX
		y = y + stepY
# for i in range(mxPg):
# 	for j in range(len(fName)):
# 		print("(" + str(xS[j][i]) + "," + str(yS[j][i]) + ")", end=" ")
# 	print("")

if form=='pdf':
	# For PDF
	pdf = FPDF('P', 'mm', (dimPg[0], dimPg[1]))
	for i in range(mxPg):
		pdf.add_page()
		for j in range(len(fName)):
			if xS[j][i] != -1:
				pdf.image(fName[j],xS[j][i],yS[j][i],dimImg[j][0],dimImg[j][1])
	pdf.output(sys.argv[2], "F")
elif form=='gif':
	# For GIF
	images = []
	for i in range(mxPg):
		new_im = Image.new('RGB', (dimPg[0], dimPg[1]))
		for j in range(len(fName)):
			if xS[j][i] != -1:
				x = xS[j][i]
				y = yS[j][i]
				im = Image.open(fName[j])
				im.thumbnail((dimImg[j][0],dimImg[j][1]))
				new_im.paste(im, (x,y), im)
		images.append(new_im)
	images[0].save(sys.argv[2], save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)