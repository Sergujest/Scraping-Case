import lxml.html
import requests
import urllib.request
import writeonsheet
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def scrape(creds):


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(100)
    searchCount=1
    totalProductCount=2

    # This loop checks if there is still a search page with that search count
    while True:
        url='https://www.defacto.com.tr/arama?q=&page=%d'%searchCount
        page = requests.get(url)
        
        # This if is the control mechanism of the outer loop.  
        if page.status_code!=200:
            break


        searchPage=lxml.html.fromstring(page.content)
        productsInSearch=searchPage.xpath('//div[@id="products"]/div/div')

        productInPageCount=1

        listOfProducts=[]
        
        for x in productsInSearch :

            # This loop is to check if there is something wrong at stock states. Sometimes page does not work properly so this loop refreshes 
            # the page. 
            loopCount=0
            while True:
                loopCount=loopCount+1
                tempUrl=searchPage.xpath('//div[@id="products"]/div/div[%d]/div/div[1]/a/@href'%productInPageCount)
                productUrl='https://www.defacto.com.tr{0}'.format(tempUrl[0])
                print(productUrl)
                
                # If there is a time exception while trying to get the page, try it again
                isSuccess=False
                while not isSuccess:
                    try:
                        driver.get(productUrl)
                        isSuccess=True
                    except TimeoutException as ex:
                        print("Can not get the page. Trying again.....")
                
                
                productPage=lxml.html.fromstring(driver.page_source)

                # These are the wanted variables
                price=productPage.xpath('//div[@class="product-info-prices-new"]/text()')[0]
                SKU=productPage.xpath('//div[@id="productDetailInfoSection"]/div[1]/span/text()')[0]
                stockStates=productPage.xpath('//div[@id="productDetailSizeQuantityAndButtons"]/div[1]/div[2]/div/div/a/@class')


                # This part is rate of out of stock sizes of a product to all sizes of the same product
                outStock=0
                for state in stockStates:
                    if state=='dropdown-item product-no-stock':
                        outStock=outStock+1
                # This if is the control mechanism of inner while loop
                if len(stockStates)!=0:
                    productInPageCount=productInPageCount+1
                    optionScore=outStock/len(stockStates)
                    tempList=[]
                    tempList.append(SKU[11:])
                    tempList.append(productUrl)
                    tempList.append(price)
                    tempList.append(optionScore)

                    listOfProducts.append(tempList)
                    
                    #listOfProducts[productInPageCount].append(SKU[11:],productUrl,price,optionScore)
                    
                    # Writing part starts here
                    #writeONsheet.write(SKU[11:],productUrl,price,optionScore,(totalProductCount),creds)
                    break

                if loopCount==10 :
                    productInPageCount=productInPageCount+1
                    break

        writeONsheet.write(listOfProducts,totalProductCount,len(listOfProducts),creds)
        totalProductCount=totalProductCount+len(listOfProducts)
        searchCount=searchCount+1


    return
