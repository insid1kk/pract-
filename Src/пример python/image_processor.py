from PIL import Image
import os
import shutil

class ImageProcessor:
    @staticmethod
    def convert_to_grayscale(input_path: str, output_path: str) -> bool:
        """ 
        Конвертирует изображение в черно-белое
        Возвращает True при успехе, False при ошибке
        """ 
        try:
            # Создаем папку для результатов, если ее нет
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
                print(f"■ Создана папка: {output_dir}")

            with Image.open(input_path) as img:
                grayscale_img = img.convert('L')
                grayscale_img.save(output_path)
                print(f"■ Изображение конвертировано: {output_path}")
                return True
        except Exception as e:
            print(f"✗ Ошибка конвертации: {e}")
            return False

    @staticmethod
    def move_image(source_path: str, destination_folder: str) -> bool:
        """ 
        Перемещает файл в указанную папку
        """ 
        try:
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                print(f"■ Создана папка: {destination_folder}")

            filename = os.path.basename(source_path)
            destination_path = os.path.join(destination_folder, filename)

            shutil.move(source_path, destination_path)
            print(f"■ Файл перемещен: {destination_path}")
            return True
        except Exception as e:
            print(f"✗ Ошибка перемещения: {e}")
            return False
