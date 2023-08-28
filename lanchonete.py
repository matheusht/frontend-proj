import time
guizao = 'stefanini'.upper()
whitelist = ['guizao veado', 'nao', 'guizao trans', 'podre', 'gayzin']
print('-='*20)
print(f'         LANCHONETE {guizao}')
print('-='*20)
resp = str(input('ricardo PORRA do menu? '))
if resp in whitelist:
    print('MENU: ')
    for c in range(0,1):
        print('1- Guiziburguer')
        time.sleep(0.5)
        print('2- Guizitos ')
        time.sleep(0.5)
        print('3- Guizao frito')
        time.sleep(0.5)
        print('4-Guizao Empanade')
        time.sleep(0.5)
        print('5-Guizona e Fritas')