import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
valor_anterior = 0

while True:           #BITCOIN

    data_e_hora_em_texto = datetime.now().strftime("%d/%m/%Y %H:%M")
    url = 'https://www.infomoney.com.br/cotacoes/bitcoin-btc/'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    Raspagem = soup.find(class_='value')
    bit = list()
    
    for value in Raspagem:
        bit.append(value.next_element)
    
    ValorAtual = bit[1]
    
    if ValorAtual != valor_anterior:
        print(f"Valor Do Bitcoin Atualmente: R${ValorAtual} em {data_e_hora_em_texto}")
    
    sleep(5)
    
    valor_anterior = ValorAtual
