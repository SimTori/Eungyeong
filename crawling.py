from bs4 import BeautifulSoup
import requests
import pprint
# 옷감 0 / 가죽 5 / 목재 10 / 철 주괴 15

def crwaling():
    preurl = requests.get('https://archeage.xlgames.com/play/worldinfo')
    soup = BeautifulSoup(preurl.text, 'html.parser')
    text = ['옷감', '가죽', '목재', '철 주괴']
    data = soup.select('tbody')
    arr1 = []
    test = []
    spl = []

    for i in range(0, 2):
        arr1.append(data[i].text)

    for data in arr1:
        test.append(data.split('\n'))

    for ta in test:
        spl.append(list(filter(None, ta)))


    for sp in spl:
        for i in range(0, 4):
            if sp.index(text[1]) != 5:
                sp.insert(sp.index(text[1]), '　　　　　　　　　')
            else:
                break
        for i in range(0, 4):
            if sp.index(text[2]) != 10:
                sp.insert(sp.index(text[2]), '　　　　　　　　　')
            else:
                break
        for i in range(0, 4):
            if sp.index(text[3]) != 15:
                sp.insert(sp.index(text[2]), '　　　　　　　　　')
            else:
                break
        for i in range(0, 4):
            if len(sp) != 20:
                sp.insert(len(sp), '-------------------------')
            else:
                break

    return spl


crwaling()
