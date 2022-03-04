import time
import json
import requests
from pycoingecko import CoinGeckoAPI
from os.path import join
import os
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy, ProxyType
import pandas as pd
import matplotlib.pyplot as mp
cg = CoinGeckoAPI()
# print(cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd'))

whale_address = "0xae4d837caa0c53579f8a156633355df5058b02f3"

# Main Func - User input address
def main():
    crypto_address = input("Please enter: ")
    print(F"The address you would like to use is {crypto_address}. ")

# Scrape Func
def scrape():
    crypto_address = "0xfe3e6a25e6b192a42a44ecddcd13796471735acf"
    date = "11-11-2021"
    token_info = requests.get("http://api.coingecko.com/api/v3/coins/ethereum/contract/" + crypto_address)
    tjson = token_info.json()
    token_name = tjson['id']
    print(f"Selected token: ", token_name)
    r = requests.get(F"http://api.coingecko.csom/api/v3/coins/{token_name}/history?date={date}&localization=false")
    # print(r.status_code)
    # print(r.text)
    json_response = r.json()
    # print(json_response)
    value = json_response["market_data"]["current_price"]["usd"]
    print("The token " + token_name + " was worth " + str(value) + " on " + date)


def get_token_value_on_date(address, date, id):
    try:
        r = requests.get(F"http://api.coingecko.com/api/v3/coins/{id}/history?date={date}&localization=false")
        jsonresponse = r.json()
        value = jsonresponse["market_data"]["current_price"]["usd"]
        value = str(value)
        print(F"Token {id} was worth {value} on {date}")
    except KeyError:
        print("Unable to access token ID. Please try a different method")


def ids():
    tokeninfo = requests.get(F"https://api.coingecko.com/api/v3/coins/list")
    tjson = tokeninfo.json()
    print(F"{tjson}")

def ACTUALget_json_info(address, date, addresses):
    for address in addresses:
        try:
            id = "binance-smart-chain"
            contract_address = address
            tokeninfo = requests.get(F"http://api.coingecko.com/api/v3/coins/{id}/contract/{contract_address}")
            tjson = tokeninfo.json()
            # print(F"{tjson}")
            with open(F"~/Desktop/{address}.json", "a") as o:
                # print(json.dumps(tjson, indent=4))
                # Try and change file name to the name of the coin
                o.write(str(json.dumps(tjson, indent=4)))

        except KeyError:
            print(F"Unable to access token ID for {address}. Please try a different method")

def get_json_info(address, date, addresses):
    for address in addresses:
        try:
            id = "binance-smart-chain"
            contract_address = address
            tokeninfo = requests.get(F"http://api.coingecko.com/api/v3/coins/{id}/contract/{contract_address}")
            tjson = tokeninfo.json()
            # print(F"{tjson}")
            """with open(F"/Desktop/{address}.json", "a") as o:
                # print(json.dumps(tjson, indent=4))
                # Try and change file name to the name of the coin
                o.write(str(json.dumps(tjson, indent=4)))"""
            print('Outputting to desktop')
            path = "/Desktop/"

            name = input('Enter a name for your file: ')+'.txt'  # Name of text file coerced with +.txt

            try:
                file = open(join(path, name),'w')   # Trying to create a new file or open one
                file.close()


            except:
                print('Something went wrong! Cannot tell what?')
                title = "Error"
                message = "----"
                command = f'''
                osascript -e 'display notification "{message}" with title "{title}"'
                '''
                os.system(command)

        except KeyError:
            print(F"Unable to access token ID for {address}. Please try a different method")


def transaction_history():
    id = "binance-smart-chain"
    whale_address = "0xae4d837caa0c53579f8a156633355df5058b02f3"
    contract_address = "0x622a1297057ea233287ce77bdbf2ab4e63609f23"
    tokeninfo = requests.get(F"http://api.coingecko.com/api/v3/coins/{id}/contract/{whale_address}")
    # tokeninfo = requests.get(F"http://api.coingecko.com/api/v3/asset_platforms")
    tjson = tokeninfo.json()
    print(tjson)
    # ID = binance-smart-chain


def get_trending_tokens():
    tokeninfo = requests.get(F"https://api.coingecko.com/api/v3/search/trending/")
    # https://api.coingecko.com/api/v3/simple/token_price/{id}?contract_addresses={contract-address}&vs_currencies={currency}
    tjson = tokeninfo.json()
    print(tjson)


def checkIfValidAPI():
    r = requests.get("http://api.coingecko.com/api/v3/coins/unfederalreserve/history?date=05-05-2021&localization=false")
    if r.status_code == requests.codes.ok:
        pass
        print("API connection successful")
    else:
        print("Error")


def LiveTracker(address):
    time.sleep(0.5)
    fp = webdriver.FirefoxProfile()

    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.dir",os.getcwd())
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")
    # Still need to confirm
    #browser = webdriver.Firefox(firefox_profile=fp)
    #driver = webdriver.Firefox()    # tokeninfo = requests.get(F"http://api.coingecko.com/api/v3/coins/{id}/contract/{whale_address}")
    whale_address = address
    # check against prev json


    #driver.get(F'https://app.zerion.io/{whale_address}/history')

    #time.sleep(5)


    #driver.find_element("Button__ButtonElement-sy8p3t-0 bMlPDN").click()
    #try:
        #driver.find_element_by_class_name("bMlPDN").click()

    #driver.click("Button__ButtonElement-sy8p3t-0 bMlPDN")
# Have all coin IDs stored in ids.json
    import glob
    # directory = '~/Downloads'
    # max([os.path.join(directory,d) for d in os.listdir(directory)], key=os.path.getmtime)



def graph():
    #data = [["Australia", 2500, 2021],["Bangladesh", 1000, 2021],["England", 2000, 2021],["India", 3000, 2021],["Srilanka", 1500, 2021]
    #dataFrame = pd.DataFrame(data, columns=["Team","Rank_Points", "Year"])
    #dataFrame.plot(x="Team", y=["Rank_Points","Year" ], kind="line", figsize=(10, 9)
    print("graph")

    Time = [16,17,18,19,20,21,22,23,24,25]
    Money = [0.1, 0.2, 0.3, 0.4, 0.3,0.5, 0.6, 0.77, 0.8, 1]
    CB91_Blue = '#2CBDFE'

    color_list = [CB91_Blue]
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
    plt.plot(Time,Money)
    plt.title('Graph')
    plt.xlabel('Time')
    plt.ylabel('Money')
    plt.show()
    """n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(X, Y)

    plt.scatter(np.arange(5), np.arange(5))

    plt.xticks(())
    plt.yticks(())

    plt.show()"""


def Constant():
            id = "binancecoin"
            coins = requests.get(F"http://api.coingecko.com/api/v3/coins/")
            coinslist = coins.json()
            print(coinslist)
            tokeninfo = requests.get(F"https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd")
            tjson = tokeninfo.json()
            #print(tjson)
            value = tjson[id]["usd"]
            print(value)


address = "0xae4d837caa0c53579f8a156633355df5058b02f3"
date = "1-11-2021"
addresses = ["0xfe3e6a25e6b192a42a44ecddcd13796471735acf", "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"]
id = "binancecoin"

checkIfValidAPI()

#LiveTracker(address)
#graph()
Constant()
#get_json_info(address, date, addresses)
# transaction_history()
# get_new_tokens()
#ids()


# Working functions
#get_token_value_on_date(address, date, id)
# get_trending_tokens()
# scrape()
"""
title = "Error"
message = "----"
command = f'''
osascript -e 'display notification "{message}" with title "{title}"'
'''
os.system(command)
"""

"""    Catch Exception as exc: \
        print(str(exc))
"""
