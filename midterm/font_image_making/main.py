from PIL import Image, ImageDraw, ImageFont
import textwrap
import cv2
def make_font_image(font_name) :
    im = Image.open("C:/Users/TOP/Desktop/opensource/whitewithgrid.jpg")

    if font_name.upper() == font_name.lower() :  #폰트이름이한글
        draw = ImageDraw.Draw(im)
        draw.text((340,50),font_name, font = ImageFont.truetype("C:/Windows/Fonts/"+font_name+".otf", 40), fill = 'black')
        draw.text((80,125)," a   b   c   d   e   f   g", font = ImageFont.truetype("C:/Windows/Fonts/"+font_name+".otf", 80), fill = (224,224,224))
        draw.text((80,235)," h   i   j    k   l   m   n", font = ImageFont.truetype("C:/Windows/Fonts/"+font_name+".otf", 80), fill = (224,224,224))
        draw.text((80,345)," o   p   q   r    s   t   u", font = ImageFont.truetype("C:/Windows/Fonts/"+font_name+".otf", 80), fill = (224,224,224))
        draw.text((195,455)," v   w   x   y   z  ", font = ImageFont.truetype("C:/Windows/Fonts/"+font_name+".otf", 80), fill = (224,224,224))
        im.save("fontimage"+font_name+".png")
    else :
        draw = ImageDraw.Draw(im)
        myfont0 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40)
        myfont1 = ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 80)
        row0 = font_name
        row1 = 'a  b  c  d  e  f  g'
        row2 = 'h  i  j  k  l  m  n'
        row3 = 'o  p  q  r  s  t  u'
        row4 = 'v  w  x  y  z'
        w0,h0 = draw.textsize(row0, font = myfont0)
        w1,h1 = draw.textsize(row1 , font = myfont1)
        w2, h2 = draw.textsize(row2, font=myfont1)
        w3, h3 = draw.textsize(row3, font=myfont1)
        w4, h4 = draw.textsize(row4, font=myfont1)
        draw.text(((860-w0)/2.0, 50), font_name, font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 40), fill='black')
        draw.text(((860-w1)/2.0, 125), row1 ,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 80), fill=(224,224,224))
        draw.text(((860-w2)/2.0, 245), row2 ,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 80), fill=(224,224,224))
        draw.text(((860-w3)/2.0, 365), row3,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 80), fill=(224,224,224))
        draw.text(((860-w4)/2.0, 485), row4,font=ImageFont.truetype("C:/Windows/Fonts/" + font_name + ".ttf", 80), fill=(224,224,224))
        im.save("fontimage_"+font_name+".png")

make_font_image("bahnschrift")
make_font_image("segoesc")


