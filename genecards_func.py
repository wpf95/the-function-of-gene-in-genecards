import re
import requests
from bs4 import BeautifulSoup
kv = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
genelist = input("输入查找的全部基因，空格分隔:")
genelist = genelist.strip().split()
for gene in genelist:
    url = "https://www.genecards.org/cgi-bin/carddisp.pl?gene="+ gene
    r = requests.get(url, headers=kv)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    sa = soup.find_all("a", {"data-ga-action": "GWA"})

    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for m in sa:
        list1.append(str(m))
    for n in list1:
        if 'title=' not in n:
            list2.append(str(n))
    for i in list2[1:]:
        re1 = r'data-ga-source-accession=(.*?)href'
        func = re.findall(re1, i)
        list3.append(func)
    for a in list3:
        b = str(a).replace('"', '').replace("'", "")
        list4.append(b)
    print([str(list4).replace("[", "").replace("]", "").replace("'", "")])
