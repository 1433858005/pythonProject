with open('py.txt', encoding='utf-8')as f:
    str1 = f.read(6)
    str2 = f.read()
    print(str1,str2,sep='\n')
