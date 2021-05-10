import pymysql
def query():
    conn = pymysql.Connect(host="rm-2zetm7o3xf179o6sw33150.mysql.rds.aliyuncs.com", port=3306, database="uclass_rd",
                           user="uclass_rd_rw", password="mBQXOLxJBmNcpim0tahWlqlSYDkM8c3y",
                           charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT phoneno,pwd FROM users WHERE phoneno = '11401240099'"
    cursor.execute(sql)
    cds = cursor.fetchone()
    return cds
    cursor.close()
    conn.close()

