from urllib.request import urlopen
import re

html = urlopen("https://24h.pchome.com.tw/prod/DBCV00-A900BLYWF").read().decode("utf-8")
# print(html)

href = re.findall(r'href="(.*?)"', html)
print("\nAll links :", href)