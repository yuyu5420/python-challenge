import urllib.request
import re
url  = "http://www.pythonchallenge.com/pc/def/ocr.html"
with urllib.request.urlopen(url) as f:
    text = f.read()
    print(text)
    #s = re.search('\%\%\$\@.*', text)
    #print(s)