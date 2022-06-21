import urllib.request
import pymysql
import wget

if __name__ == "__main__":
    # 打开数据库连接
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='Jp15149622693',
                         database='english')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "SELECT * FROM english.a级"
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    # wu记录没有下载的MP3文件
    wu = 0
    you =0
    for i in range(len(results)):
        print(results[i][3])
        url = results[i][3]  # 目标路由，下载的资源是图片
        path = 'c:/mp3/danci/a级/' + url[-69:]  # 保存的路径
        print(path)
        # if url[45:52] == 'clfugc/':
        #     path = 'c:/mp3/danci/' + url[52:]
        # if url[45:52] == 'vwpqcw/':
        #     path = 'c:/mp3/danci/' + url[52:]
        # if url[45:52] == 'tkdghk/':
        #     path = 'c:/mp3/danci/' + url[52:]
        # if url[45:52] == 'verskb/':
        #     path = 'c:/mp3/danci/' + url[52:]
        # if url[45:52] == 'robdnp/':
        #     path = 'c:/mp3/danci/' + url[52:]
        if url[30:34] == '/us/':
            print("tmp文件")
            wu += 1
            continue
        else:
            if url == '没有MP3':
                print("没有MP3")
                wu += 1
                continue
            else:
                you += 1
                wget.download(url, path)  # 下载

    print('没有录入'+str(wu)+'个'+"下载"+str(you))
    # 关闭数据库连接
    db.close()
# https://media-audio1.baydn.com/us/2d64ef18127c52d86d02b24fa90116be.mp3
