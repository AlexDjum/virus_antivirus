virus_code = 'Я вирус'

with open('script_scan.py', encoding='utf-8') as file:
    content = file.read()

    if virus_code in content:
        print('Вирус обнаружен')
    else:
        print('Вирус не обнаружен')