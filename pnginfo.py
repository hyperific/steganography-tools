def encode(path,message):
	from PIL import Image, PngImagePlugin
	info = PngImagePlugin.PngInfo()
	info.add_text("text", message)
	info.add_text("ZIP", "VALUE", zip=True)
	im = Image.open(path)
	im.save(path, "PNG", pnginfo=info)

def decode(path):
	from PIL import Image, PngImagePlugin
	im = Image.open(path)
	return im.text["text"]
