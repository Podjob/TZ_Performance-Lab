import sys

def circularArrayPath(n, m):

    if n <= 0 or m <= 0:
        sys.exit("Ошибка: значение n или m меньше или равно 0!")

    nCount = 1
    mCount = 1
    lastNumber = 0
    path = [1]

    # Определение пути
    while lastNumber != 1:

        # Обновление текущего числа nCount
        if nCount < n:
            nCount += 1
        else:
            nCount = 1

        # Обновление счетчика интервала mCount
        if mCount < m:
            mCount += 1
        else:
            # Сброс счетчика и заполнение пути
            mCount = 1
            nCount -= 1
            if nCount == 0:
                nCount = n
            lastNumber = nCount
            path.append(lastNumber)
    # Формирование пути из массива в строку
    pathStr = ''.join(map(str, path[:-1]))
    return pathStr

# Задание аргументов
n = int(sys.argv[1])
m = int(sys.argv[2])

# Вывод результата
print(circularArrayPath(n, m))