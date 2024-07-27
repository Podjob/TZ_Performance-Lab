import sys

def readingFile(readableFile):
    # Чтение файла
    arrayInt = []
    with open(readableFile, 'r') as file:
        for line in file:
            line = line.strip()
            arrayInt.append(int(line))
    return arrayInt

def numberSelection(numdersArr):
    # Вычисление среднего значения массива и округление его до ближайшего целого числа
    sumArr = sum(numdersArr)
    requiredNumber = round(sumArr / len(numdersArr))
    return requiredNumber

def castingAnArrayToOneNumber(numdersArr, requiredNumber):
    # Сведение элементов массива к заданному числу и подсчет количества шагов
    steps = 0
    for numb in numdersArr:
        while numb != requiredNumber:
            if numb < requiredNumber:
                numb += 1
            if numb > requiredNumber:
                numb -= 1
            steps += 1
    return steps

# Получение пути к файлу из аргументов командной строки
numbersFilePath = sys.argv[1]
numbers = readingFile(numbersFilePath)
requiredNumber = numberSelection(numbers)
# Вывод количества шагов
print(castingAnArrayToOneNumber(numbers, requiredNumber))
