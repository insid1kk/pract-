import os
from image_processor import ImageProcessor

class UserInterface:
    @staticmethod
    def get_user_input():
        """Получает данные от пользователя"""
        print("\n=== Конвертер изображений в черно-белое ===")
        input_path = input("Введите путь к изображению: ").strip()

        if input_path and os.path.isfile(input_path):
            # Получаем путь к рабочему столу
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            
            # Создаем путь к папке "1" на рабочем столе
            folder_1 = os.path.join(desktop_path, "1")
            
            # Создаем путь к папке "Результаты" внутри папки "1"
            results_folder = os.path.join(folder_1, "Результаты")

            # Проверяем и создаем папки если их нет
            if not os.path.exists(folder_1):
                os.makedirs(folder_1)
                print(f"■ Создана папка: {folder_1}")
            
            if not os.path.exists(results_folder):
                os.makedirs(results_folder)
                print(f"■ Создана папка: {results_folder}")

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
        if ImageProcessor.convert_to_grayscale(input_path, output_path):
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
            # Показываем путь к сохраненному файлу
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            results_path = os.path.join(desktop_path, "1", "Результаты")
            print(f"✅ Файл сохранен в: {results_path}")

def main():
    ui = UserInterface()
    ui.process_image()

if __name__ == "__main__":
    main()
