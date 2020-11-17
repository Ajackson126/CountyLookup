# County Lookup
# Application to retrieve the county related to an address from the USPS website
# and print it to a file
# Author: Avery Jackson c/o RAS Lavrar LLC

#Imports 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import csv
import time
import sys
import os

#Finds full path for driver
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)



#Closes files and exits program
def cleanUp(input_file, output_file, driver):

    input_file.close()
    output_file.close()
    driver.close()
    sys.exit()

    
#Initializes chrome driver and exits on error
def init_driver():
    #Setting web driver path
    DRIVER_PATH = resource_path("chromedriver.exe")
    os.listdir(".")
    #print(DRIVER_PATH)

    #Running Chrome in headless mode for faster POST/REQUEST time
    #opt = webdriver.ChromeOptions()
    #opt.add_argument("--headless")
    #print("Chrome Options Assigned")

    #Setting webdriver
    try:
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    except:
        print("Error:", sys.exc_info())
        time.sleep(7)
        sys.exit()

    return driver
    #print("Chrome Driver initialized")   
    

#Navigates to USPS website, driver.get natively throws and error upon invalid SSL certificate
def usps_navigation(driver):
    #Navigating to the USPS Website
    driver.get('https://www.usps.com/')

    print("Navigated to USPS website")

    time.sleep(2)
    #"Clicking" the drop down menu for the Zip Code Lookup by using the link of the button
    driver.get('https://tools.usps.com/go/ZipLookupAction_input')

    time.sleep(2)

    #"Clicking" the "Search by Address" option by using the link of the button
    driver.get('https://tools.usps.com/zip-code-lookup.htm?byaddress')

    return driver


#Reads from input file, receives response from USPS and writes to output file
def read_and_write():

    
    initialized_driver = init_driver()

    
    driver = usps_navigation(initialized_driver)

    try:
        address_input_file = open('AddressFileDrop\InputAddressFile.csv', 'r')
        input_file_reader = csv.reader(address_input_file)
    except OSError:
        print("Input File Error")
        sys.exit()
        
    try:    
        county_output_file = open('ResultFile\CountyResults.csv', 'w', newline='')
        output_file_writer = csv.writer(county_output_file)
    except OSError:
        print("Output File Error")
        sys.exit()

    for address in input_file_reader:
        
        time.sleep(1)
        #Place Address in Street Address field
        street_address_input = driver.find_element_by_id("tAddress")
        street_address_input.send_keys(address[1])
        
        #Place city in City field
        city_input = driver.find_element_by_id("tCity")
        city_input.send_keys(address[2])
        
        #Select State in drop down menu
        select = Select(driver.find_element_by_id('tState'))
        select.select_by_value(address[3])
        
        #Place zip code in ZIP Code field
        zip_code_input = driver.find_element_by_id('tZip-byaddress')
        zip_code_input.send_keys(address[4])
        
        time.sleep(1)
        
        #Click the "Find" button
        button = driver.find_element_by_id('zip-by-address')
        button.click()
        
        time.sleep(2)
        #try/except block to get around addresses that aren't found
        try:
            container = driver.find_element_by_xpath('/html/body/div[3]/div/div[5]/div/div/div[4]/div/div/ul/li')
        except:
            address_temp = address
            address_temp.append("Not Found")
            address_with_county = address_temp
            print(address_with_county)
            output_file_writer.writerow(address_with_county)
            driver.get('https://www.usps.com/')
            time.sleep(2)
            driver.get('https://tools.usps.com/go/ZipLookupAction_input')
            time.sleep(2)
            driver.get('https://tools.usps.com/zip-code-lookup.htm?byaddress')
            continue
        #Show hidden elements    
        driver.execute_script("arguments[0].setAttribute('class','list-group-item paginate active')", container)

        time.sleep(2)
        #Get county
        county = driver.find_element_by_xpath('/html/body/div[3]/div/div[5]/div/div/div[4]/div/div/ul/li/div[2]/div[1]/div[2]/div[2]/p')
        county_text = county.text
        address_temp = address
        address_temp.append(county_text)
        address_with_county = address_temp
        print(address_with_county)
        
        #write values to csv file
        output_file_writer.writerow(address_with_county)
        
        time.sleep(1)
        
        #Click link to enter new address
        look_up_another_address = driver.find_element_by_xpath('/html/body/div[3]/div/div[5]/div/div/div[7]/div/div[1]/a')
        look_up_another_address.click()

    cleanUp(address_input_file, county_output_file, driver)



read_and_write()
