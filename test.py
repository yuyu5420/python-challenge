import pickle
import urllib.request


url  = "http://www.pythonchallenge.com/pc/def/banner.p" #將此頁面的HTML GET下來
with urllib.request.urlopen(url) as f:
    #print(f.read())
    result = pickle.load(f)
    for i in result:
        for j in i:
            for x in range(j[1]):
                print(j[0],end="")
        print()