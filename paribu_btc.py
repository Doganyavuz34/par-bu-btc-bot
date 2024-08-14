import requests

cookies = {
    '__cf_bm': 'PV_OHF0P9qNAyo_5ATe4U6JbanraMxLoueF3L4RH5qM-1714480350-1.0.1.1-enyI_h9zo05kHpwEMls9gGlnnOfAz9_Q.ZipRUon8F8vQ65f.__TrrQAClcwo42T3FoPUgGj3wMYF.6VYO4rJg',
    '_cfuvid': 'hWRn_sNEuzrbHB8Vic5wAqOM9stQrUbFly_nUwIVgb4-1714480350495-0.0.1.1-604800000',
    'cf_clearance': '2FrfcOTvC6wFGk1tyx5.TRl.noB2OgwEbwNsvAkBEh0-1714480352-1.0.1.1-Eem0yi7dhUZT3oMzDM8yshS9opPKT.uaWGS_uz2dNMNrAJF0vPsA1wtYNe3xM_RhWcTPHKrmEaNDTw9.2oXhCw',
    '_ga': 'GA1.1.644856096.1714480353',
    '_fbp': 'fb.1.1714480372680.168565665',
    '_tt_enable_cookie': '1',
    '_ttp': 'UpsrLWqYkJ_hP236_Fw6_EOovcd',
    '_ga_98JF77GNP2': 'GS1.1.1714480353.1.1.1714480557.58.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'tr-TR,tr;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '__cf_bm=PV_OHF0P9qNAyo_5ATe4U6JbanraMxLoueF3L4RH5qM-1714480350-1.0.1.1-enyI_h9zo05kHpwEMls9gGlnnOfAz9_Q.ZipRUon8F8vQ65f.__TrrQAClcwo42T3FoPUgGj3wMYF.6VYO4rJg; _cfuvid=hWRn_sNEuzrbHB8Vic5wAqOM9stQrUbFly_nUwIVgb4-1714480350495-0.0.1.1-604800000; cf_clearance=2FrfcOTvC6wFGk1tyx5.TRl.noB2OgwEbwNsvAkBEh0-1714480352-1.0.1.1-Eem0yi7dhUZT3oMzDM8yshS9opPKT.uaWGS_uz2dNMNrAJF0vPsA1wtYNe3xM_RhWcTPHKrmEaNDTw9.2oXhCw; _ga=GA1.1.644856096.1714480353; _fbp=fb.1.1714480372680.168565665; _tt_enable_cookie=1; _ttp=UpsrLWqYkJ_hP236_Fw6_EOovcd; _ga_98JF77GNP2=GS1.1.1714480353.1.1.1714480557.58.0.0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'view': 'classic',
}


import telegram # pip install python-telegram-bot
from datetime import datetime

from bs4 import BeautifulSoup
from datetime import datetime
import time as t
dolar = ""
en_yuksek = 0
channel_id = -1002113620836
BOT_TOKEN = "7144099326:AAHa2zHgkaFmwLORg5aqs4K31uNawTYt-Sg"
bot = telegram.Bot(token = BOT_TOKEN)
def telegram_mesaj_gonder(msj):
    try:
        bot.sendMessage(chat_id = channel_id, text = msj, 
                        parse_mode = telegram.ParseMode.HTML, 
                        disable_web_page_preview = False)
    except Exception as e:
        print("Bildirim mesajı hatası: " + str(e))

while True:
    response = requests.get('https://www.paribu.com/markets/btc_tl', params=params, cookies=cookies, headers=headers)
    if(response.status_code == 200):
        source = BeautifulSoup(response.content, "html.parser")
        dolar_kuru = source.find("p", attrs={"class":"market-ticker-mobile__price my-1"}).text
        if(dolar != dolar_kuru):
            dolar = dolar_kuru
            print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + " " + str(dolar_kuru) + " " + str(float(dolar_kuru)))
            if(float(dolar_kuru) > en_yuksek):
                en_yuksek = float(dolar_kuru)
                msg = str(datetime.now().strftime("%H:%M:%S")) + " -> " + str(dolar_kuru)
                telegram_mesaj_gonder(msg)                
    else:
        print(datetime.now().strftime("%d.%m.%Y %H:%M:%S") + " " + "Sayfa engellemesi")
    t.sleep(0.5)











