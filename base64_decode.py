import base64

img_data = b"<base64 here>"

with open("imageToSave.jpg", "wb") as fh:
    fh.write(base64.decodebytes(img_data))
