import os
from image_processor import ImageProcessor

class UserInterface:
    @staticmethod
    def get_user_input():
        """Получает данные от пользователя"""
        print("\n=== Конвертер изображений в черно-белое ===")
        input_path = input("Введите путь к изображению: ").strip()

        if input_path and os.path.isfile(input_path):
            # Получаем папку где находится код программы (текущая директория)
            current_directory = os.getcwd()

            # Создаем путь к папке "Результаты" в корневой папке с кодом
            results_folder = os.path.join(current_directory, "Результаты")

            # Проверяем существование папки "Результаты"
            if not os.path.exists(results_folder):
                os.makedirs(results_folder)
                print(f"Создана папка для результатов: {results_folder}")

            # Генерируем имя для выходного файла
            filename = os.path.basename(input_path)
            name, ext = os.path.splitext(filename)
            output_filename = f"{name}_bw{ext}"

            # Полный путь к выходному файлу в папке "Результаты"
            output_path = os.path.join(results_folder, output_filename)

            return input_path, output_path
        else:
            print("✗ Файл не найден!")
            return None, None

    def process_image(self):
        """Основной процесс обработки"""
        input_path, output_path = self.get_user_input()

        if not input_path:
            return

        # Конвертируем в черно-белое
        processor = ImageProcessor()
        if processor.convert_to_grayscale(input_path, output_path):
            # Предлагаем переместить файл
            self.ask_for_move(output_path)

    def ask_for_move(self, file_path):
        """Спрашивает пользователя о перемещении файла"""
        choice = input("\nХотите переместить файл (y/n): ").strip().lower()
        if choice == 'y':
            destination = input("Введите папку для перемещения: ").strip()
            if destination:
                ImageProcessor.move_image(file_path, destination)
            else:
                print("✗ Не указана папка для перемещения")
        else:
            print("☑ Файл сохранен в папке 'Результаты'")

def main():
    ui = UserInterface()
    ui.process_image()

if __name__ == "__main__":
    main()