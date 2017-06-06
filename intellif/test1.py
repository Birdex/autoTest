from intellif.IntellifAutotestClass import DbData
# 测试获取数据库特征值

# db = DbData("192.168.2.27", "root", "introcks1234", "intellif_face")
db = DbData()
for feature in db.query(count=2):
    print(feature)
    print()
