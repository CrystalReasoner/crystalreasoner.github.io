from pdf2image import convert_from_path
images = convert_from_path('your-file.pdf', dpi=150)
for i, image in enumerate(images):
    image.save(f'page_{i+1}.png', 'PNG')