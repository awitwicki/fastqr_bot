# open text file and replace substring and save it
with open('amazing-qr/amzqr/amzqr.py', 'r+') as file:
    code = file.read()
    code = code.replace('qr.resize((qr.size[0]*3, qr.size[1]*3))', 'qr.resize((qr.size[0]*3, qr.size[1]*3), resample=Image.BOX)')
    file.seek(0)
    file.write(code)
