import pickle                              #导入pickle模块
data1={'小寻':[18,'女',100],'小君':[19,'男',98],'小薇':[18,'男',60]}
data2=['高等教育','Python','程序设计']
with open('../../../Documents/WeChat Files/wxid_iewwm99i3kbc21/FileStorage/File/2022-06/实践内容8/test.dat', 'wb') as f1:
    pickle.dump(data1,f1)                  #将字典序列化
    pickle.dump(data2,f1,1)                #将列表序列化
with open('../../../Documents/WeChat Files/wxid_iewwm99i3kbc21/FileStorage/File/2022-06/实践内容8/test.dat', 'rb') as f2:
    data3=pickle.load(f2)                  #重构字典
    data4=pickle.load(f2)                  #重构列表
print(data3,data4)

    

    
    



