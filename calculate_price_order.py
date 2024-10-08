'''
Задание 2. Подсчёт стоимости заказа из файла.
Напишите программу, которая считывает файл prices.txt,
содержащий информацию о товарах:
название, количество и цену, и подсчитывает общую стоимость заказа.
'''


def read_file_content(items):
    try:
        with open('prices.txt', 'r', encoding='utf-8') as source_file:
            for line in source_file:
                line = line.split('\t')
                list_items.append(line)
    except FileNotFoundError:
        print("Файл source.txt не найден.")
    except OSError as e:
        print(f"Ошибка файловой системы: {e}")
    except UnicodeDecodeError:
        print("Ошибка декодирования файла. Проверьте кодировку.")


def calculate_total_price_order():
    try:
        total_price = 0
        for item in list_items:
            total_price = total_price + (float(item[1]) * float(item[2]))
        print(total_price)
    except ValueError:
        print("Ошибка: некорректный ввод. Введите число, целое или с плавающей точкой.")


if __name__ == '__main__':
    list_items = []
    read_file_content(list_items)
    calculate_total_price_order()



