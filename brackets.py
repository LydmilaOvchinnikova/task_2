def brackets():
    st = input('напиши строку')
    sk = ''.join(input('дай скобку'))       #сразу введеные скобки разбиваю поэлементно
    o = ['(', '[', '{', '<']
    c = [')', ']', '}', '>']
    os = []
    cs = []
    l = 0
    p = 0
    for i in sk:                            #заполняю списки для скобок
        os.append(i)
        k = o.index(i)
        cs.append(c[k])
    m = []                                  #КАК НАЗНАЧИТЬ ЗА ОДИН РАЗ ТИП НЕСКОЛЬКИМ ПЕРЕМЕННЫМ???
    n = []
    a = []
    b = []
    for i in st:
        if i in os:
            m.append(os.index(i))            #заполняю массив с индексом типа скобки ('(' - 0, '[' - 1 и т.д.)
            a.append(st.index(i))           #ПРИ ПОДРЯД ИДУЩИХ СКОБКАХ ИНДЕКС ВЕЗДЕ ПЕРВОЙ СКОБКИ????
            l += 1
        if i in cs:
            if cs.index(i) == m[-1]:         #сравниваю закрывающую скобку с предыдущим элементом
                m.pop(-1)                   #если предыдущий элемент - такая же открывающая скобка, то удаляю эту открывающую скобку
                                            #m пустой, если вложения норм. например ([][{}])
            n = [cs.index(i)] + n            #список наоборот, чтоб было удобно сравнивать (массив аналогичен m)
            b = [st.index(i)] + b
            p += 1
    if not m:
        print('True')                       #АХАХХАХАХАХАХХА
    if l != p:
        print ('кол-во закрывающих и открывающих не совпадает')
    else:
        for index, (i, j) in enumerate(zip(m, n)):
            if i != j:
                print('False',(cs[n[index]], b[index]),(os[m[index]], a[index])) #АХАХАХХАХАХАХАХ - 2


brackets()