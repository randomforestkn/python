import qrcode
import qrcode.image.svg

# convert text to qr code image and read the image with qr_code reader
img = qrcode.make("write anything")
img.save("qrcode.png")


# convert link to qr code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)

link = "link.com"
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("test.png")


# make svg
factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hello World", image_factory=factory)
svg_img.save("myqr.svg")
