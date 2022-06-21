with open('py.txt', 'w+') as f:
    print(f.tell()) #文件指针处于文件头
    f.write('www.gnnu/cn')
    print(f.tell()) #文件指针处于文件尾
    f.seek(8,0) #文件指针处于位置8
    print(f.tell())
    f.write('.')
    print(f.tell())
    
    
    
