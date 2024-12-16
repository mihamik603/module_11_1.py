from PIL import Image, ImageFilter

# Открытие изображения
image = Image.open('example.jpg')

# 1. Изменение размера изображения
resized_image = image.resize((200, 200))
resized_image.save('resized_image.jpg')

# 2. Применение фильтра размытия
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('blurred_image.jpg')

# 3. Конвертация изображения в другой формат (например, PNG)
image.save('converted_image.png', 'PNG')

# 4. Поворот изображения
rotated_image = image.rotate(90)
rotated_image.save('rotated_image.jpg')

# 5. Получение информации об изображении
print(f'Формат: {image.format}, Размер: {image.size}, Режим: {image.mode}')

