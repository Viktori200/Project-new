def main():
    print('Выражение должно содержать один оператор: "+", "-", "*", "/"')
    print('Калькулятор принимает на вход числа от 1 до 10 включительно')
    s = input('Введите выражение: ')
    exist = '+' in s
    if exist == True:
        try:
            ss = s.split('+')
            if len(ss) > 2:
                print('Выражение должно содержать один оператор!')
            elif int(ss[0]) > 10:
                print('Неверный ввод. Числа должны быть от 1 до 10')
            elif int(ss[0]) < 1:
                print('Неверный ввод. Числа должны быть от 1 до 10')
            elif int(ss[1]) > 10:
                print('Неверный ввод. Числа должны быть от 1 до 10')
            elif int(ss[1]) < 1:
                print('Неверный ввод. Числа должны быть от 1 до 10')
            else:
                print('Ответ: ', int(ss[0]) + int(ss[1]))
        except:
            print('Проверьте правильность ввода выражения')
    else:
        exist = '-' in s
        if exist == True:
            try:
                ss = s.split('-')
                if len(ss) > 2:
                    print('Выражение должно содержать один оператор!')
                elif int(ss[0]) > 10:
                    print('Неверный ввод. Числа должны быть от 1 до 10')
                elif int(ss[0]) < 1:
                    print('Неверный ввод. Числа должны быть от 1 до 10')
                elif int(ss[1]) > 10:
                    print('Неверный ввод. Числа должны быть от 1 до 10')
                elif int(ss[1]) < 1:
                    print('Неверный ввод. Числа должны быть от 1 до 10')
                else:
                    print('Ответ: ', int(ss[0]) - int(ss[1]))
            except:
                print('Проверьте правильность ввода выражения')
        else:
            exist = '*' in s
            if exist == True:
                try:
                    ss = s.split('*')
                    if len(ss) > 2:
                        print('Выражение должно содержать один оператор!')
                    elif int(ss[0]) > 10:
                        print('Неверный ввод. Числа должны быть от 1 до 10')
                    elif int(ss[0]) < 1:
                        print('Неверный ввод. Числа должны быть от 1 до 10')
                    elif int(ss[1]) > 10:
                        print('Неверный ввод. Числа должны быть от 1 до 10')
                    elif int(ss[1]) < 1:
                        print('Неверный ввод. Числа должны быть от 1 до 10')
                    else:
                        print('Ответ: ', int(ss[0]) * int(ss[1]))
                except:
                    print('Проверьте правильность ввода выражения')
            else:
                exist = '/' in s
                if exist == True:
                    try:
                        ss = s.split('/')
                        if len(ss) > 2:
                            print('Выражение должно содержать один оператор!')
                        elif int(ss[0]) > 10:
                            print('Неверный ввод. Числа должны быть от 1 до 10')
                        elif int(ss[0]) < 1:
                            print('Неверный ввод. Числа должны быть от 1 до 10')
                        elif int(ss[1]) > 10:
                            print('Неверный ввод. Числа должны быть от 1 до 10')
                        elif int(ss[1]) < 1:
                            print('Неверный ввод. Числа должны быть от 1 до 10')
                        elif int(ss[1]) > int(ss[0]):
                            print('Ответом является дробное число')
                        else:
                            print('Ответ: ', int(int(ss[0]) / int(ss[1])))
                    except:
                        print('Проверьте правильность ввода выражения')
                else:
                    print('Неверное выражение!')

main()
while True:
    print('Продолжить? (да/нет)')
    decision = input()
    if decision == 'да':
        main()
    else:
        break