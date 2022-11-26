import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

#Site com a lista de países
url = "https://www.iban.com/currency-codes"
r= requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')

table = soup.find("table")
rows = soup.find_all("tr")[1:]

countries = []
i = 0

for row in rows:
  items = row.find_all('td')
  name = items[0].text
  coin =  items[2].text
  if items[1].text == "No universal currency":
      continue
  else:
    country = {
    "index": i,
    "name": name.capitalize(),
    "coin": coin
    } 
    countries.append(country)
    i += 1

a = True
conversao = 0
print("Bem-vindo ao Negociador de Moedas")
print("Escolha pelo número os dois países que deseja negociar moedas.\n")
for country in countries:
  print(f"#{country['index']} {country['name']}")   
while a == True:
  try:
    print("\nInforme pelo número o país de origem da moeda.\n\n")       
    #país 1
    choice = int(input("=> "))
    while choice > country['index']:
      print("Não existe. Escolha uma opção da lista: ")
      choice = int(input("=> "))
    country1 = countries[choice]['coin']  
    print(f"$$$ {choice}")
    print(f"\n (x) {countries[choice]['name']}\n")    
    #país 2
    print("Quer negociar com qual outro país?\n\n")
    choice = int(input("=> "))
    while choice > country['index']:
      print("Não existe. Escolha uma opção da lista: ")
      choice = int(input("=> "))
    country2 = countries[choice]['coin']      
    print(f"\nQuantos {country1} você quer converter para {country2}\n")  
    a = False
  except:
    print("Isso não é um número. Escolha uma opção da lista: ")

country1 = country1.lower()
country2 = country2.lower()
try:
  quantidade = float(input("=>"))
  link = f"https://www.forbes.com/advisor/money-transfer/currency-converter/{country1}-{country2}/?amount={quantidade}"
  r= requests.get(link)
  html = r.text
  soup1 = BeautifulSoup(html, 'html.parser')
  teste = soup1.find("div",{"class": "result-box-c1-c2"}).text
  teste = teste.split()
  if teste[3]<teste[8]:
    conversao = quantidade * float(teste[3])
  else:
    conversao = quantidade/ float(teste[3])
  
  country1 = country1.upper()
  country2 = country2.upper()
  
  pais1 = format_currency(quantidade, country1, locale='pt_BR')
  pais2 = format_currency(conversao, country2, locale='pt_BR')
  print(f"\n{pais1} é igual a {pais2}")
except:
  print("\nNão é possível converter a mesma moeda")