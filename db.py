import pymysql
import data
#连接Mysql数据库
db= pymysql.connect(host="localhost",user="root",password="123456",db="sjk",port=3306)
# 使用cursor()方法获取操作游标
cur = db.cursor()
#创建一个表用来存储 标题,题目解释,以及题目网页链接
def create_unifo_table():
    sql='''create table url_info(
    title varchar (2000),
    description varchar (2000),
    url varchar (2000))'''
    try:
        db.ping(reconnect=True)#重新连接数据库
        cur.execute(sql)
    except:
        print("该表已经存在")
    finally:
        db.commit()
#创建一个用来存储网页的连接
def create_url_table():
    sql = '''create table url_list(
      url varchar (2000))'''
    try:
        db.ping(reconnect=True)
        cur.execute(sql)
    except:
        print("该表已经存在")
    finally:
        db.commit()
# 插入每个题目的链接
def insert_url(url):
    sql_insert_url = "insert into url_list values ('%s')"% (pymysql.escape_string(url))
    try:
        db.ping(reconnect=True)
        cur.execute(sql_insert_url)
    except Exception as e:
        print("插入链接失败")
    finally:
        db.commit()
# 插入每个题目标题,题目解释,网页的链接
def insert_data(title, description, url):
    sql_insert_data = """insert into sjk.url_info values ('%s','%s','%s')""" % (pymysql.escape_string(title),pymysql.escape_string (description), pymysql.escape_string(url))
    try:
        db.ping(reconnect=True)
        cur.execute(sql_insert_data)  # 执行sql语句
    except Exception as e:
        print("插入数据失败")
        raise e
    finally:
        db.commit()
def delete_data(table):
    sql1 = "SET SQL_SAFE_UPDATES = 0"
    sql = "delete from %s"%table
    try:
        db.ping(reconnect=True) #重新连接数据库
        cur.execute(sql1)
        cur.execute(sql)  # 执行sql语句
    except Exception as e:
        print("插入数据失败")
        raise e
    finally:
        db.commit()
def main():
    data.main()
    create_unifo_table()
    content_list=data.content
    url_list=data.url_list
    for i in range(len(content_list)):
        insert_data(content_list[i][0],content_list[i][1],content_list[i][2])

    create_url_table()
    for i in range(len(url_list)):
          insert_url(url_list[i])
db.close()  # 关闭连接

if __name__ =="__main__":
     main()


