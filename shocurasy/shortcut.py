def crypto_key(size, file=None):
    """size of key\n
    create a txt file with key."""
    import random
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_ch = '!@#$%&*'
    random_ch = ['letter', 'special', 'number']
    key = ''
    for create in range(size):
        character = random_ch[random.randint(0, 2)]
        if character == random_ch[0]:
            key += f'{letters[random.randint(0, len(letters)-1)]}'
        elif character == random_ch[1]:
            key += f'{special_ch[random.randint(0, len(special_ch)-1)]}'
        elif character == random_ch[2]:
            key += f'{random.randint(0, 9)}'

    if file is None:
        write_file([key], 'Key.txt', 0)

    return key


def sql_create_values(file, table_name, colunas, objects):
    """fil = ['nome', 'idade', 'peso']\n
    info = ['Maria', 19, 67.2]
    sql_create_values('test.db', people, fil, info)\n"""
    import sqlite3
    conexao = sqlite3.connect(file)
    cursor = conexao.cursor()

    f = f'cursor.execute("INSERT INTO {table_name} ('
    for times in colunas:
        if times == colunas[-1]:
            f += f'{times}) '
        else:
            f += f'{times}, '
    f += 'VALUES ('
    for times in colunas:
        if times == colunas[-1]:
            f += f':{times})", '
        else:
            f += f':{times}, '
    f += '{'
    for times in range(len(objects)):
        if objects[times] == objects[-1]:
            if check_file(objects[times]) == 1:
                f += f'"{colunas[times]}": {file_to_binary(objects[times])}'
            elif type(objects[times]) == str:
                f += f'"{colunas[times]}": "{objects[times]}"'
            else:
                f += f'"{colunas[times]}": {objects[times]}'
        else:
            if check_file(objects[times]) == 1:
                f += f'"{colunas[times]}": {file_to_binary(objects[times])}, '
            elif type(objects[times]) == str:
                f += f'"{colunas[times]}": "{objects[times]}", '
            else:
                f += f'"{colunas[times]}": {objects[times]}, '
    f += '})'

    exec(f)

    conexao.commit()
    cursor.close()
    conexao.close()


def sql_create_table(file, table_name, colunas, type_colunas):
    """Cria a tabela e coloca os objetos e seu tipos\n
    INTEGER = int |---| REAL = float\n
    TEXT = str |---| BLOB = file |---| NUMERIC = numeric\n
    .\n
    obj = ['idade', 'nome', 'peso', 'id]\n
    tipos = ['int', 'str', 'float', 'INTERGER PRIMARY KEY AUTOINCREMENT']\n
    create_table(bank.db, 'peoples', obj, tipos )"""
    import sqlite3
    modos = ['REAL', 'INTERGER', 'TEXT', 'BLOB', 'NUMERIC']

    conexao = sqlite3.connect(file)
    cursor = conexao.cursor()

    types = []
    for creating in type_colunas:
        if creating == 'int':
            types += [modos[1]]
        elif creating == 'float':
            types += [modos[0]]
        elif creating == 'str':
            types += [modos[2]]
        elif creating == 'file':
            types += [modos[3]]
        elif creating == 'numeric':
            types += [modos[4]]
        else:
            types += creating

    f = f'cursor.execute("CREATE TABLE IF NOT EXISTS {table_name} ('
    for obj in range(len(colunas)):
        if colunas[-1] == colunas[obj]:
            f += f'{colunas[obj]} {types[obj]}'
        else:
            f += f'{colunas[obj]} {types[obj]}, '
    f += ')")'
    exec(f)

    cursor.close()
    conexao.close()


def file_to_binary(filename):
    """Convert digital data to binary format"""
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def hex_to_rgb(value):
    """convert hex to rgb\n
    value = hex_to_rgb("FF65BA")"""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))


def rgb_to_hex(rgb):
    """convert rgb to hex\n
    value = rgb_to_hex((100,250,20))"""
    return '%02x%02x%02x' % rgb


def cal_math(calculo, show=0):
    """resolve a conta matematica\n
    show 1 = mostra resultado\n
    show 0 = nao mostra o resultado"""
    result = eval(calculo)
    if show == 1:
        print(f'{calculo} = {result}')
    return result


def token_generate():
    from uuid import uuid4
    rand_token = uuid4()
    return rand_token


def write_file(content, file, check_read=0,  path=None):
    """It places the desired content in the file and maintains the
     information that exists within the file.\n
     You can put the directory of the file if you want, it is not mandatory to have it.\n
     info = ['a', 2, 'start = 1', random]\n
     write(info, 123.py, 1,)\n
     Check read 1 = keep the data\n
     0 or nothing = remove the data\n"""
    if check_read == 1:
        if check_file(file) == 1:
            info = read_file(file, path)
            info += content
        else:
            info = content
            print("Not Founded!")
    else:
        info = content

    if path is None:
        reading = open(f'{file}', 'w')
    else:
        reading = open(f'{path}/{file}', 'w')

    for line in info:
        reading.write(f"{line}\r")


def read_file(file, path=None):
    """Make a list of a file\n
    You can put the directory of the file if you want, it is not mandatory to have it.\n
    file_list = read('info.txt')\n
    file_list = read('welcome.txt', 'C:/Python38')"""
    if path is None:
        reading = open(f'{file}', 'r')
    else:
        reading = open(f'{path}/{file}', 'r')
    content = []
    for line in reading:
        content += [f'{line[0:len(line)-1]}']
    return content


def check_date(format='%d/%m/%Y'):
    """Show the current date\n
    date = check_date("%Y/%m/%d")\n
    %Y: a year in 4 digits.\n
    %y: a year in 2 digits.\n
    %m: month in 2 digits.\n
    %B: full name of the month.\n
    %w: week number from 0 to 6.\n
    %A: full name of the weekday.\n
    %d: day of the month.\n
    %j: day of the year."""
    import datetime
    date = f"{datetime.datetime.now():{format}}"
    return date


def check_time():
    """Show the current time
    day_time = check_time"""
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def keyboard_piano(num_key=None):
    """its every key piano on keyboard\n
    0 to 61
    key = keyboard_piano(10)
    keys = keyboard_piano()"""
    keys = ['1', 'shift + 1', '2', 'shift + 2', '3', '4', 'shift + 4', '5', 'shift + 5', '6', 'shift + 6',
            '7', '8', 'shift + 8', '9', 'shift + 9', '0', 'q', 'shift + q', 'w', 'shift + w', 'e', 'shift + e',
            'r', 't', 'shift + t', 'y', 'shift + y', 'u', 'i', 'shift + i', 'o', 'shift + o', 'p', 'shift + p',
            'a', 's', 'shift + s', 'd', 'shift + d', 'f', 'g', 'shift + g', 'h', 'shift + h', 'j', 'shift + j',
            'k', 'l', 'shift + l', 'z', 'shift + z', 'x', 'c', 'shift + c', 'v', 'shift + v', 'b', 'shift + b',
            'n', 'm']
    if num_key is None:
        key = keys
    else:
        key = keys[num_key]
    return key


def check_file(file, path=None):
    """It will check if the file exists\n
    You can put the directory of the file if you want, it is not mandatory to have it.\n
    check_file(abc.txt)\n
    1 = exists 0 = don't exists"""
    import os
    if path is None:
        if os.path.isfile(f'{file}'):
            value = 1
        else:
            value = 0
    else:
        if os.path.isfile(f'{path}/{file}'):
            value = 1
        else:
            value = 0
    return value


def console(command='start notepad'):
    """type the terminal command\n
    output = console('start notepad.exe')"""
    import os

    comando = command
    if comando.lower() == "sair":
        exit()
    elif 'cd..' in comando:
        comando = os.getcwd()
        value = comando.count('\\')
        x = 0
        back = ''
        for characters in comando:
            if characters == '\\':
                x += 1
            if x == value:
                break
            else:
                back += characters
        os.chdir(back)
    elif 'cd' in comando:
        comando = comando.replace('cd ', '')
        os.chdir(comando)
    else:
        output = os.system(comando)
        if output == 0:  # if works
            pass
        else:
            print('\nFAIL:')
            print(f'ERROR: {output}')
    return output


def tempo(delay=10):
    """tempo(milliseconds)\n
    Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision."""
    import time
    start = time.time()
    while True:
        if type(delay) != int:
            print('What? Its Milliseconds.')
            print('tempo(100)')
        elif round(1000 * (time.time() - start)) >= delay:
            break


def detect_pixel(pos_x, pos_y):
    """Check color pixel. \n
    color = detect_pixel(100,100)
    """
    from PIL import ImageGrab
    img = ImageGrab.grab().load()  # 30 ms
    pixel = img[pos_x, pos_y]
    return pixel


def random_num(min_num=0, max_num=100, mode=1):
    """Random Value \n
    mode 1 = int \n
    mode 2 = float \n
    number = random_num(0, 10, 1)"""
    import random
    if mode == 1:
        value = random.randint(min_num, max_num)
    elif mode == 2:
        value = round(random.uniform(min_num, max_num), 3)
    else:
        print('What?')
        print('Mode 1 = int')
        print('Mode 2 = float')
    return value


def openweb(key='0', link='youtube.com/watch?v=FF3Dr3_h0Hw', browser='chrome'):
    """Open website.\n
    reaload("f", "youtube.com", "chrome")"""
    import keyboard
    import os
    if keyboard.is_pressed(key):
        os.system(f'start {browser} {link}')
        on = 1
    else:
        on = 0
    return on


def pos_color(exit='q', show='p'):
    """set key to exit and to show.\n
    pos_color('f', 'p')"""
    import pyautogui
    import time
    import keyboard

    while not keyboard.is_pressed(exit):
        if keyboard.is_pressed(show):
            x, y = pyautogui.position()
            im = pyautogui.screenshot()
            r, g, b = im.getpixel((x, y))
            print(f' x,y = {x, y} RGB = {r, g, b}')
            time.sleep(0.5)
        time.sleep(0.1)


def sorteio(conteudo):
    """draw an object from the list\n
    items = [a,b,c,...]\n
    val = sorteio(items)"""
    import random
    itens = conteudo
    sorteado = itens[random.randint(0, len(itens))]
    return sorteado


def on_off(on, off):
    """One key for activate and other to desactivate\n
    val = on_off('del', 'insert')"""
    import keyboard
    if keyboard.is_pressed(on):
        value = 1
    elif keyboard.is_pressed(off):
        value = 0
    return value


def sorteio_porcentagem(min_num, max_num, times=1):
    """Generate random percentage\n
    x = sorteio_porcentagem(0, 100, 5)
    output = x = [30, 43, 60, 73, 90]
    """
    import random
    porcentagem = []
    minimo = min_num
    for gerar in range(times):
        value = random.randint(minimo, max_num)
        porcentagem += [value]
        minimo = value

    return porcentagem


def click(pos_x, pos_y):
    import pydirectinput as directinput
    directinput.PAUSE = 0.006
    directinput.click(pos_x, pos_y)


def screen():
    """Collects the cited coordinates of the corners. Useful to check the colors of pixels in a certain area"""
    import pyautogui
    import time
    import keyboard


    print('coloque o mouse no canto superior esquerdo da caixa de item recebido e aperte "P"')
    while True:
        if keyboard.is_pressed('p'):
            x1, y1 = pyautogui.position()
            print(f' x,y = {x1, y1}')
            break
        time.sleep(0.1)

    time.sleep(0.5)
    print('coloque o mouse no canto inferior direito da caixa de item recebido e aperte "P"')
    while True:
        if keyboard.is_pressed('p'):
            x2, y2 = pyautogui.position()
            print(f' x,y = {x2, y2}')
            break
        time.sleep(0.1)
    time.sleep(0.5)
    return x1, x2, y1, y2


def check_imports(pips, module=None):
    """Checks if pip(s) exists, if not, it does the installation if possible.\n
    pip = ['sqlite3', 'keyboard', 'mido']\n
    check_imports(pip)
    """
    x = 0
    if module == 'shortcut':
        pipes = pips
        for check_pip in pipes:
            try:
                exec(f'import {check_pip}')
            except:
                if check_pip == 'os':
                    v = 0
                else:
                    v = 1
                print(f'NOT FOUNDED PIP: {check_pip}')
                if v == 0:
                    print(f'Open cmd and type: pip install {check_pip}')
                else:
                    print('INSTALLING...')
                    console(f'pip install {check_pip}')
                    print('\n Info:')
                    console(f'pip show {check_pip}')
                    x = 2

        if x == 2:
            print('Installations done.\nYou are ready to use!')

    elif module != 'shortcut':
        pipes = pips
        for check_pip in pipes:
            try:
                if type(pipes) == str:
                    exec(f'import {pipes}')
                else:
                    exec(f'import {check_pip}')
            except:
                if check_pip == 'os':
                    v = 0
                else:
                    v = 1
                print(f'NOT FOUNDED PIP: {check_pip}')
                if v == 0:
                    print(f'Open cmd and type: pip install {check_pip}')
                else:
                    print('INSTALLING...')
                    console(f'pip install {check_pip}')
                    print('\n Info:')
                    console(f'pip show {check_pip}')
                    x = 2

        if x == 2:
            print('Installations done.\nYou are ready to use!')
        else:
            print('Everything is already installed.')


def check_def(file):
    file = open(f'{file}', 'r')
    x = 0
    lista = []
    for check in file:
        if check[0] == 'd':
            if 'def ' in check:
                x += 1
                lista += [check[0:-1]]
    file.close()
    return lista
