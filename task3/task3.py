import json
import sys

def recordingValues(valuesFile, testsFile, reportFile):
    # Чтение values.json и tests.json
    with open(valuesFile, 'r', encoding='utf-8') as file:
        valuesData = json.load(file)
    with open(testsFile, 'r', encoding='utf-8') as file:
        testsData = json.load(file)

    # Создание словаря значений по id
    valuesDict = {item["id"]: item["value"] for item in valuesData.get("values", [])}

    # Заполнение значений в структуре tests через стек
    forBypass = [(testsData, None)]
    while forBypass:
        current, parent = forBypass.pop()
        if isinstance(current, dict):
            if "id" in current and current["id"] in valuesDict:
                current["value"] = valuesDict[current["id"]]
            for key, value in current.items():
                forBypass.append((value, current))
        elif isinstance(current, list):
            for index, item in enumerate(current):
                forBypass.append((item, current))

    # Запись результатов в report.json из testsData
    with open(reportFile, 'w', encoding='utf-8') as file:
        json.dump(testsData, file, ensure_ascii=False, indent=2)

# Получение путей к файлам из аргументов командной строки
valuesFilePath = sys.argv[1]
testsFilePath = sys.argv[2]
reportFilePath = sys.argv[3]
recordingValues(valuesFilePath, testsFilePath, reportFilePath)