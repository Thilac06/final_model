from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
import openpyxl

driver = webdriver.Chrome()
driver.get("https://pfm.smartcitylk.org/wp-admin/profile.php")

username_field = driver.find_element(By.NAME, "log")
password_field = driver.find_element(By.NAME, "pwd")

username_field.send_keys("tafuser1@gmail.com")
password_field.send_keys("TAF#asia2293")

login_button = driver.find_element(By.ID, "wp-submit")
login_button.click()

wait = WebDriverWait(driver, 10)


local_authorities = ['Rajanganaya PS', 'Rambewa PS','Talawa PS', 'Tirappane PS', 'Dimbulagala PS', 'Elehera PS', 'Hingurakgoda PS', 'Lankapura PS',
                     'Medirigiriya PS', 'Polonnaruwa MC', 'Polonnaruwa PS', 'Welikanda PS', 'Gomarankadawala PS', 'Kantale PS',
                     'Kinniya PS', 'Kinniya UC', 'Kuchchaweli PS', 'Morawewa PS', 'Muttur PS', 'Padavisiripura PS',
                     'Seruvila PS', 'Thambalagamuwa PS', 'Trincomalee Town and Gravets PS', 'Trincomalee UC',
                     'Verugal PS', 'Addalachenai PS', 'Akkaraipattu MC', 'Akkaraipattu PS', 'Alaiyadivembu PS',
                     'Ampara UC', 'Damana PS', 'Dehiattakandiya PS', 'Irakkamam PS', 'Kalmunai MC', 'Karaitivu PS',
                     'Lahugala PS', 'Maha Oya PS', 'Namal Oya PS', 'Naveethanveli PS', 'Ninthavur PS', 'Padiyatalawa PS', 
                     'Pottuvil PS', 'Sammanthurai PS', 'Thirukkovil PS', 'Uhana PS', 'Batticaloa MC', 'Eravur Pattu PS',
                     'Eravur UC', 'Kattankudi UC', 'Koralaipattu North PS', 'Koralaipattu PS', 'Koralepattu West PS', 
                     'Manmunal Pattu PS', 'Manmunal South and Eruvil Pattu PS', 'Manmunal South West PS',
                     'Manmunal West (Vavunatheev) PS', 'Porativpattu PS', 'Badulla MC', 'Badulla PS', 'Bandarawela MC', 
                     'Bandarawela PS', 'Ealla PS', 'Haldummulla PS', 'Hali-Ela PS', 'Haputale PS', 'Haputale UC',
                     'Kandeketiya PS', 'Lunugala PS', 'Mahiyanganaya PS', 'Meegahakivula PS', 'Passara PS', 
                     'Ridimaliyadda PS', 'Soranathota PS', 'Uva-Paranagama PS', 'Welimada PS', 'Badalkumbura PS',
                     'Bibila PS', 'Buttala PS', 'Kataragama PS', 'Madulla PS', 'Medagama PS', 'Moneragala PS',
                     'Siyambalanduwa PS', 'Tanamalwila PS', 'Wellawaya PS', 'Ambalangoda PS', 'Karandeniya PS', 'Rajgama PS',
                     'Akmeemana PS', 'Baddegama PS', 'Niyagama PS', 'Bentota PS', 'Elpitiya PS', 'Neluwa PS', 'Tawalama PS',
                     'Habaraduwa PS', 'Yakkalamulla PS', 'Balapitiya PS', 'Bope Poddala PS', 'Nagoda PS', 'Welivitiya-Divithura PS', 
                     'Imaduwa PS', 'Ambalangoda UC', 'Hikkaduwa UC', 'Galle MC', 'Matara PS', 'Weligama PS', 'Thihagoda PS',
                     'Hakmana PS', 'Malimbada PS', 'Devinuwara PS', 'Akuressa PS', 'Dikwella PS', 'Kamburupitiya PS', 
                     'Mulatiyana PS', 'Kotapola PS', 'Pasgoda PS', 'Pitabeddara PS', 'Kirinda Puhulwella PS', 'Athuraliya PS', 
                     'Weligama UC', 'Matara MC', 'Beliatta PS', 'Katuwana PS', 'Ambalanthota PS', 'Hambanthota PS', 'Tangalle PS',
                     'Angunukolapelessa PS', 'Tissamaharamaya PS', 'Lunugamwehera PS', 'Sooriyawewa PS', 'Weeraketiya PS', 'Tangalle UC', 
                     'Hambanthota MC', 'Homagama PS', 'Kotikawatta Mulleriya PS', 'Sitawaka PS', 'Kolonnawa UC', 'Seetawakapura UC',
                     'Maharagama UC', 'Kesbewa UC', 'Boralesgamuwa UC','Colombo MC','Dehiwala  Mount Levaniya MC','Moratuwa MC',
                     'Sri Jayawardanapura Kotte MC ', 'Kaduwela MC', 'Attanagalla PS', 'Biyagama PS', 'Divulapitiya PS',
                     'Dompe PS', 'Gampaha PS', 'Ja Ela PS', 'Katana PS', 'Kelaniya PS', 'Mahara PS', 'Meerigama PS',
                     'Minuwangoda PS', 'Wattala PS', 'Ja Ela UC', 'Minuwangoda UC', 'Peliyagoda UC', 'Wattala Mabole UC', 
                     'Katunayaka  Seeduwa UC', 'Gampaha MC', 'Negambo MC', 'Agalawaththa PS', 'Bandaragama PS', 'Beruwala PS', 
                     'Bulathsinhala PS', 'Dodangoda PS', 'Horana PS', 'Kaluthara PS', 'Mathugama PS', 'Panadura PS', 'Walallawita PS',
                     'Madurawela PS', 'Palindanuwara PS', 'Millaniya PS', 'Beruwela UC', 'Horana UC', 'Kalutara UC', 'Panadura UC',
                     'Giribawa PS', 'Maho PS', 'Polgahawela PS', 'Galgamuwa PS', 'Kurunegala PS', 'Ibbagamuwa PS', 'Kobeigane PS', 
                     'Pannala PS', 'Wariyapola PS', 'Panduwasnuwara PS', 'Narammala PS', 'Alawwa PS', 'Nikaweratiya PS', 'Bingiriya PS', 
                     'Ridigama PS', 'Kuliyapitiya PS', 'Mawathagama PS', 'Polpithigama PS', 'Udubaddawa PS', 'Kuliyapitiya UC',
                     'Kurunegala MC', 'Kalpitiya PS', 'Karuwalagaswewa PS', 'Chilaw PS', 'Puttalama PS', 'Nattandiya PS',
                     'Nawagaththegama PS', 'Wennappuwa PS', 'Arachchikattuwa PS', 'Anamaduwa PS', 'Wanathawilluwa PS', 
                     'Chillaw UC', 'Puttalam UC', 'Harispaththuwa PS', 'Pasbage Korale PS', 'Tumpane PS', 'Kundasale PS', 
                     'Meda Dumbara PS', 'Patha Dumbara PS', 'Udapalatha PS', 'Ganga Ihala Korale PS', 'Akurana PS', 
                     'Minipe PS', 'Udunuwara PS', 'Yatinuwara PS', 'Panwila PS', 'Patha Hewaheta PS', 'Gangawata Korale PS',
                     'Ududumbara PS', 'Poojapitiya PS', 'Nawalapitiya UC', 'Gampola UC', 'Wattegama UC', 'Kadugannawa UC',
                     'Kandy MC', 'Matale  PS', 'Ambanganga Korale  PS', 'Dambulla  PS', 'Pallepola  PS', 'Ukuwela  PS', 'Wilgamuwa  PS', 
                     'Laggala-Pallegama  PS', 'Galewela  PS', 'Naula  PS', 'Rattota  PS', 'Yatawatta  PS', 'Matale MC', 'Dambulla MC', 
                     'Nuwara-Eliya  PS', 'Ambagamuwa  PS', 'Hanguranketha  PS', 'Walapane  PS', 'Kothmale  PS', 'Maskeliya  PS', 'Norwood  PS',
                     'Kotagala  PS', 'Agarapathana  PS', 'Hatton-Dickoya UC', 'Talawakelle-Lindula UC', 'Nuwara - Eliya MC', 'Aranayaka PS',
                     'Warakapola PS', 'Mawanella PS', 'Rabukkana PS', 'Yatiyanthota PS', 'Deraniyagala PS', 'Galigamuwa PS', 'Dehiovita PS',
                     'Kegalle PS', 'Ruwanwella PS', 'Bulathkohupitiya PS', 'Kegalle UC', 'Kuruwita PS', 'Ayagama PS', 'Nivitigala PS', 'Kolonna PS',
                     'Eheliyagoda PS', 'Pelmadulla PS', 'Kalawana PS', 'Balangoda PS', 'Weligepola PS', 'Imbulpe PS', 'Ratnapura PS', 'Embilipitiya PS',
                     'Godakawela PS', 'Kahawatta PS', 'Embilipitiya UC', 'Balangoda UC', 'Rathnapura MC']



for i in local_authorities:
                
    change_button = wait.until(EC.element_to_be_clickable((By.ID, "change")))
    change_button.click()
                        
    la_select_element = wait.until(EC.presence_of_element_located((By.NAME, "la_name")))
    la_select = Select(la_select_element)
    la_select.select_by_visible_text(i)

    change_button1 = driver.find_element(By.ID, "submit")
    change_button1.click()

    login_url = 'https://pfm.smartcitylk.org/wp-login.php'
    target_url = 'https://pfm.smartcitylk.org/wp-admin/admin.php?page=programTitles'
    username = 'tafuser1@gmail.com'
    password = 'TAF#asia2293'


    
    # Session setup for maintaining login state
    session = requests.Session()

    # Login to the website
    login_payload = {'log': username, 'pwd': password}
    login_response = session.post(login_url, data=login_payload)

    # Check if login was successful (you might need to adjust this based on the website's response)
    if 'login_error' in login_response.text:
        print("Login failed. Check your credentials.")
        exit()

    # Fetch the target page with the form
    response = session.get(target_url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table')
    x, y, z = 'Local Authority', 'Other Key', 'Another Key'
    local_authority_info = {cols[0].text.strip(): cols[1].text.strip() for cols in [row.find_all('td') for row in soup.find('table').find_all('tr') if len(row.find_all('td')) == 2]}

    N = (local_authority_info.get(x, f"{x} not found"))


    # Extract data from the form
    program_data = {}
    form = soup.find('form', {'id': 't10'})
    table_rows = form.find_all('tr')

    for row in table_rows:
        columns = row.find_all('td')
        if len(columns) == 2:
            program_name = columns[0].get_text(strip=True)
            input_field = columns[1].find('input')
            if input_field:
                program_data[program_name] = input_field['value']

    # Create Excel file and write data
    excel_file = openpyxl.Workbook()
    sheet = excel_file.active
    sheet.title = 'Program Data'

    # Write headers
    sheet.append(['Program Name', 'Value'])

    # Write data
    for program_name, value in program_data.items():
        sheet.append([program_name, value])

    # Save Excel file
    excel_file.save(f'{N}.xlsx')
    print(f"{N} has been extracted and saved to program_data.xlsx.")
                    



    
