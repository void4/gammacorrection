from PIL import Image, ImageDraw

w = h = 256

img = Image.new("RGB", (w,h), (255,0,0))

img2 = Image.new("RGB", (w,h), (0,255,0))

def gamma(a):
	return tuple(p**2.2 for p in a)

def degamma(a):
	return tuple(int(p**(1/2.2)) for p in a)

def mix(a,b,p=0.5):
	return tuple(int(a[i]*p+b[i]*(1-p)) for i in range(len(a)))

for y in range(h):
	for x in range(w):
		a = img.getpixel((x,y))
		b = img2.getpixel((x,y))
		
		if x < w/2:
			c = mix(a,b, y/w)
		else:
			c = degamma(mix(gamma(a), gamma(b), y/w))
		
		img.putpixel((x,y), c)

img.save("comparison.png")
img.show()
