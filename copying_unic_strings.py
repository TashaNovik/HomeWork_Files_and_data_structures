"""
Задание 4. Копирование уникального содержимого одного файла в другой.
Создайте программу, которая считывает строки из файла input.txt,
сохраняет только уникальные строки и записывает их в новый файл unique_output.txt.
"""

if __name__ == '__main__':
    def copy_unique_lines(input_filename, output_filename):
        """Копирует уникальные строки из input_filename в output_filename."""
        try:
            seen_lines = set()  # Множество для отслеживания уникальных строк
            with open(input_filename, 'r', encoding='utf-8') as infile, \
                    open(output_filename, 'w', encoding='utf-8') as outfile:

                for line in infile:
                    line = line.strip()  # Удаляем пробелы и переносы строк
                    if line not in seen_lines:
                        seen_lines.add(line)
                        outfile.write(line + '\n')  # Добавляем перенос строки обратно

        except FileNotFoundError:
            print(f"Файл {input_filename} не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


    # Пример использования
    copy_unique_lines("input.txt", "unique_output.txt")