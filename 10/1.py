#не знаю что делать он просто отказывается читать всё, говорит нет такого файла, хотя через консоль работает
with open('kabanovigorandreevich_u232_vvod.txt', 'r') as file:
    file_content = file.read()
    print(file_content)
    with open('kabanovigorandreevich_u232_vivod.txt', 'w') as output_file:
        output_file.write(file_content)
