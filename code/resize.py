
from PIL import Image

def img_resize(file_path)
    image = Image.open(f'{file_path}')
    new_image = image.resize((380, 380))
    new_image.save(f'{file_path}')


if __name__ == '__main__':
    img_resize('../data/test/dummy.jpg')
