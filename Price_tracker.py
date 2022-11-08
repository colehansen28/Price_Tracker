import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/NVIDIA-GeForce-Founders-Graphics-GDDR6X/dp/B0BJFRT43X/ref=sr_1_4?keywords=4090+graphics' \
      '+card&qid=1667909635&s=electronics&sprefix=4090%2Celectronics%2C93&sr=1-4&ufe=app_do%3Aamzn1.fos.4dd97f68-284f' \
      '-40f5-a6f1-1e5b3de13370 '
URL2 = 'https://www.amazon.com/ZOTAC-Graphics-IceStorm-Advanced-ZT-D40900B-10P/dp/B09D1VF7F8/ref=asc_df_B09D1VF7F8' \
       '?tag=bingshoppinga-20&linkCode=df0&hvadid=80745504656191&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy' \
       '=&hvtargid=pla-4584345031991748&psc=1 '
URL3 = 'https://www.amazon.com/ZOTAC-Graphics-IceStorm-Advanced-ZT-D40900D-10P/dp/B0BGJQBW6Z/ref=asc_df_B0BGJQBW6Z' \
       '?tag=bingshoppinga-20&linkCode=df0&hvadid=80195759881320&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy' \
       '=&hvtargid=pla-4583795280267600&psc=1 '
URL4 = 'https://www.amazon.com/GeForce-Graphics-IceStorm-ZT-D40900J-10P-Motherboard/dp/B0BJ7NKSGT/ref' \
       '=asc_df_B0BJ7NKSGT?tag=bingshoppinga-20&linkCode=df0&hvadid=80058320814013&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c' \
       '&hvlocint=&hvlocphy=&hvtargid=pla-4583657843651595&psc=1 '
HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 44.0.2403.157 '
                  'Safari / 537.36',
    'Accept-Language': 'en-US, en;q=0.5'})


# Defining page scrapping for each GPU
def GPU():
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    product_name = ''
    product_price = ''
    try:
        product_title = soup.find("span",
                                  attrs={"id": 'productTitle'})
        product_name = product_title.string.strip().replace(',', '')

    except AttributeError:
        product_name = "Not Available"

    try:
        product_price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
    except AttributeError:
        product_price = "Not Available"

    print("product Title = ", product_name)
    print("product Price = ", product_price)


def GPU2():
    webpage = requests.get(URL2, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    product_name = ''
    product_price = ''
    try:
        product_title = soup.find("span",
                                  attrs={"id": 'productTitle'})
        product_name = product_title.string.strip().replace(',', '')

    except AttributeError:
        product_name = "Not Available"

    try:
        product_price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
    except AttributeError:
        product_price = "Not Available"

    print("product Title = ", product_name)
    print("product Price = ", product_price)


def GPU3():
    webpage = requests.get(URL3, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    product_name = ''
    product_price = ''
    try:
        product_title = soup.find("span",
                                  attrs={"id": 'productTitle'})
        product_name = product_title.string.strip().replace(',', '')

    except AttributeError:
        product_name = "Not Available"

    try:
        product_price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
    except AttributeError:
        product_price = "Not Available"

    print("product Title = ", product_name)
    print("product Price = ", product_price)


def GPU4():
    webpage = requests.get(URL4, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    product_name = ''
    product_price = ''
    try:
        product_title = soup.find("span",
                                  attrs={"id": 'productTitle'})
        product_name = product_title.string.strip().replace(',', '')

    except AttributeError:
        product_name = "Not Available"

    try:
        product_price = soup.find("span", attrs={'class': 'a-offscreen'}).string.strip().replace(',', '')
    except AttributeError:
        product_price = "Not Available"

    print("product Title = ", product_name)
    print("product Price = ", product_price)


# running Program-
GPU()
print("------------------------------------------------------------------")
GPU2()
print("------------------------------------------------------------------")
GPU3()
print("------------------------------------------------------------------")
GPU4()
print("------------------------------------------------------------------")
