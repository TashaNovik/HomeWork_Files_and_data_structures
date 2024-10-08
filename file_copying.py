'''
Задание 1. Копирование содержимого одного файла в другой.
Создайте программу, которая копирует содержимое файла source.txt
в новый файл destination.txt.
'''

if __name__ == '__main__':
    try:
        with open('source.txt', 'r', encoding='utf-8') as source_file:
            content = source_file.read()

        with open('destination.txt', 'w', encoding='utf-8') as destination_file:
            destination_file.write(content)
    except FileNotFoundError:
        print("Файл source.txt не найден.")
    except OSError as e:
        print(f"Ошибка файловой системы: {e}")
    except UnicodeDecodeError:
        print("Ошибка декодирования файла. Проверьте кодировку.")
