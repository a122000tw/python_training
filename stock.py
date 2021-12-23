# 匯入 Shioaji 套件
import shioaji as sj

# 建立 Shioaji api 物件
api = sj.Shioaji()

# 登入帳號
api.login(
    person_id="a122000tw@gmail.com",
    passwd="love2200023",
    contracts_cb=lambda security_type: print(f"{repr(security_type)} fetch done.")
)

# 匯入憑證
api.activate_ca(
    ca_path="",
    ca_passwd="",
    person_id="",
)
