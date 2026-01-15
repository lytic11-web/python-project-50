import json


def read_file(file_path):
    """
    Читаем и парсим JSON фаил. Предполагаем, что
    он "чёткий и првильный"
    """
    with open(file_path, 'r') as file:
        return json.load(file)



def generate_diff(file1_path, file2_path, format='stylish'):
    """
    Основная функция сравнения файлов.
    """
    # Читаем файлы
    data1 = read_file(file1_path)
    data2 = read_file(file2_path)
    
    # Пока просто выводим содержимое файлов
    return f"File 1: {data1}\nFile 2: {data2}" 
