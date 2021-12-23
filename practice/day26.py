from urllib.request import urlopen
import re

html = urlopen("https://mofanpy.com/static/scraping/basic-structure.html").read().decode('utf-8')
# print(html)

res = re.findall(r"<title>(.*?)</title>", html)
print("\nPage title is: ", res[0])

resP = re.findall(r"<p>(.*?)</p>", html, flags = re.DOTALL) # re.DOTALL 多行訊息
print("\nPage paragraph is :", resP[0])

res = re.findall(r'href="(.+?)"', html)
print("\nAll links :", res)