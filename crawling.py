import requests
from bs4 import BeautifulSoup

# 옷감 0 / 가죽 5 / 목재 10 / 철 주괴 15
SERVER = {
    "다후타": "DAHUTA",
    "누이": "NUI",
    "하제": "HAJE",
    "모르페우스": "MORPHEUS",
    "랑그레이": "RANGORA",
    "환락": "SEASON",
}


def crwaling(server: str):
    preurl = requests.get('https://archeage.xlgames.com/play/worldinfo/{}'.format(SERVER[server]))
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