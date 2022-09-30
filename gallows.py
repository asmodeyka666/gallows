import random as rd
import os

ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
word_list = []
flag = False # проверка буквы или слова на дурака
guessed_letters = []
guessed_words = []
path = os.path.join(os.getcwd(), 'words.txt')
with open(path, encoding='utf8') as file:
    for line in file:
        word_list.append(line.strip())

def get_word():
    return rd.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |    (°□°)
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |    (°□°)
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |    (°□°)
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |    (°□°)
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |    (°□°)
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |    (°□°)
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def examination(letter):
    global flag    # проверка буквы или слова на дурака
    global guessed_letters   # список уже названных букв
    global guessed_words   # список уже названных слов
    if len(letter) == len(word):
        if letter in guessed_words:
            print('Это слово Вы уже называли, попробуйте другое!')
        else:
            for i in letter:
                if i not in ru:
                    print('Вы допустили ошибку в написании слова '
                      '(в словах нет символов и они состоят только из русских букв)')
                    break
            else:
                flag = True
                guessed_words.append(letter)
    elif len(letter) == 1:
        if letter in ru:
            if letter in guessed_letters:
                print('Эту букву Вы уже называли, попробуйте другую!')
            else:
                flag = True
                guessed_letters.append(letter)
        else:
            print('Вы ввели не букву русского алфавита')
    else:
        print(f'Длинна слова не подходит! Слово состоит из {len(word)} букв!')


def play(word):
    global flag   # проверка буквы или слова на дурака
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    global guessed_letters  # список уже названных букв
    guessed_letters = []
    global guessed_words   # список уже названных слов
    guessed_words = []
    tries = 6  # количество попыток
    print(f'Компьютер загадал слово из {len(word)} букв, попробуй угадать его, прежде, чем тебя повесят!')
    while guessed == False and tries != 0:
        print(display_hangman(tries))
        print('Названные слова: ', *guessed_words, sep=' ')
        print('Названные буквы: ', *guessed_letters, sep = ' ')
        print('Загаданное слово: ', word_completion)

        # Ввод буквы или слова с проверкой на дурака
        while flag == False:
            letter = input('Введите одну букву или слово целиком (Е и Ё - это разные буквы!): ').upper()
            examination(letter)
        flag = False

        if letter == word:
            print('УРА!!! Вы угадали слово целиком! Поздравляю! \\(^O^)/')
            break
        elif letter in word:
            print('УРА!!! Есть такая буква!')
            work_word = list(word_completion)
            for i in range(len(word)):
                if letter == word[i]:
                    work_word[i] = letter
            word_completion = ''.join(work_word)
            if tries < 6:
                tries += 1
            if word == word_completion:
                print(f'Вы выиграли! Загаданное слово было {word} (^.^)')
                break
        else:
            print('Увы! Такой буквы нет в слове(')
            tries -= 1
    if tries == 0:
        print(display_hangman(tries))
        print(f'Вы проиграли( Загаданное слово было {word}')



print('Добро пожаловать в игру "Виселица"!')
while True:
    word = get_word()
    play(word)

    exit = input('Сыграем еще разок?) (Y/N) ')
    while exit not in 'YyNnНнТт':
        exit = input()
    if exit in 'YyНн':
        True
        print()
    else:
        print('До новых встреч!')
        break

