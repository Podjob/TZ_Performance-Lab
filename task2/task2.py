import sys

def readingFile(readableFile):
    # Читаем файл и преобразуем строки в массивы float
    arrayFloat = []
    with open(readableFile, 'r') as file:
        for line in file:
            array = line.strip().split(' ')
            array = [float(item) for item in array]
            arrayFloat.append(array)
    return arrayFloat

def validatingDataFromFiles(circleParams, dots):
    # Проверка на количество точек и валидность параметров
    if len(dots) > 100:
        sys.exit("Число точек привышает 100")
    elif len(dots) < 1:
        sys.exit("Нет точек")
    for dot in dots:
        if len(dot) != 2:
            sys.exit("Точки заданы некорректно")

    # Проверка на валидность параметров окружности
    if len(circleParams) != 2:
        sys.exit("Неверные параметры окружности")
    elif len(circleParams[0]) != 2 or len(circleParams[1]) != 1:
        sys.exit("Неверные параметры окружности")
    if int(circleParams[1][0]) <= 0:
        sys.exit("Радиус окружности <= 0")

def classifyPoints(circleParams, dots):
    # Классифицируем точки по их положению относительно окружности
    center, radius = circleParams[0], circleParams[1][0]
    positionsArrey = []
    for point in dots:
        # Расчет расстояния до центра окружности
        distance = ((point[0] - center[0]) ** 2 + (point[1] - center[1]) ** 2) ** 0.5
        if distance < radius:
            positionsArrey.append(1)  # Внутри окружности
        elif distance == radius:
            positionsArrey.append(0)  # На окружности
        else:
            positionsArrey.append(2)  # Снаружи окружности
    positionsArreyString = '\n'.join(map(str, positionsArrey[:]))
    return positionsArreyString

# Получение имен файлов
circleFilePath = sys.argv[1]
dotsFilePath = sys.argv[2]

# Чтение параметров окружности и точек из файлов
circle = readingFile(circleFilePath)
dots = readingFile(dotsFilePath)

# Проверка параметров окружности и точек
validatingDataFromFiles(circle, dots)

# Вывод результатов классификации точек
print(classifyPoints(circle, dots))