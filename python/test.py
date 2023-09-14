import os

while True:
    userinput = input('>')
    if userinput == 'pwd':
        # print('/'.join(__file__.split('\\')[:-1]))
        print(os.getcwd())
    elif userinput == 'dir' or userinput == 'ls':
        print(os.listdir(os.getcwd()))
    elif userinput == 'exit':
        print('안녕히가세요.')
        break