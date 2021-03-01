import os


PATH = os.path.join(os.getcwd(), 'files')
files = os.listdir(PATH)
print(PATH)
print(files)
for filename in os.listdir(PATH):
    with open(os.path.join(PATH, filename), 'r', encoding='cp866') as file:
        with open(os.path.join(os.getcwd(), 'results', filename), 'w', encoding='utf-8') as result_file:
            result_file.write(file.read())

