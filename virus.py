virus_code = 'print("Я вирус")'

with open('script_scan.py', 'a', encoding='utf-8') as file:
    file.write(f'\n{virus_code}\n')
