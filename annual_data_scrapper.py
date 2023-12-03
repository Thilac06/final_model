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

username_field.send_keys("thilacramesh@gmail.com")
password_field.send_keys("TAFpfm#2133")

login_button = driver.find_element(By.ID, "wp-submit")
login_button.click()

wait = WebDriverWait(driver, 10)


local_authorities = ['Chavakachcheri PS', 'Chavakachcheri UC', 'Delft PS', 'Jaffna MC', 
                     'Karainagar PS', 'Kayts PS', 'Nallur PS', 'Point Pedro PS', 'Point Pedro UC', 
                     'Vadamaradchi South West PS', 'Valikamam East PS', 'Valikamam North PS',
                     'Valikamam South PS', 'Valikamam South West PS', 'Valikamam West PS', 
                     'Valvetithurai UC', 'Velanai PS', 'Karachchi PS', 'Pachchilaipalli PS', 
                     'Poonakary PS', 'Manthai East PS', 'Maritimepattu PS', 'Puthukudiyiruppu PS', 
                     'Thunukkai PS', 'Mannar PS', 'Mannar UC', 'Manthai West PS', 'Musali PS', 
                     'Nanattan PS', 'Vavuniya North PS', 'Vavuniya South (Sinhala) PS', 
                     'Vavuniya South (Tamil) PS', 'Vavuniya UC', 'Vengalasettikula PS', 
                     'Anuradhapura MC', 'Galenbindunuwewa PS', 'Galnewa PS', 'Horowpothana PS', 
                     'Ipalogama PS', 'Kahatagasdigiliya PS', 'Kebithigollewa PS', 'Kekirawa PS',
                     'Medawachchiya PS', 'Mihintale PS', 'Nochchiyagama PS', 'Nuwaragam Palatha Central PS', 
                     'Nuwaragam Palatha East PS', 'Padaviya PS', 'Palagala PS', 'Rajanganaya PS', 'Rambewa PS', 
                     'Talawa PS', 'Tirappane PS', 'Dimbulagala PS', 'Elehera PS', 'Hingurakgoda PS', 'Lankapura PS',
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
    target_url = 'https://pfm.smartcitylk.org/wp-admin/admin.php?page=annualBudget'
    username = 'thilacramesh@gmail.com'
    password = 'TAFpfm#2133'

    # Create a session to persist the login credentials
    session = requests.Session()

    # Perform login
    login_payload = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'redirect_to': target_url,
    }
    login_response = session.post(login_url, data=login_payload)

    # Check if login was successful
    if 'wp-admin' in login_response.url:
        print("Login successful")
        
        
        # Fetch the target page
        target_page = session.get(target_url)
        
        # Parse HTML content
        soup = BeautifulSoup(target_page.content, 'html.parser')
        
        # Find all tables on the page
        tables = soup.find_all('table')
        x, y, z = 'Local Authority', 'Other Key', 'Another Key'
        local_authority_info = {cols[0].text.strip(): cols[1].text.strip() for cols in [row.find_all('td') for row in soup.find('table').find_all('tr') if len(row.find_all('td')) == 2]}

        N = (local_authority_info.get(x, f"{x} not found"))

        # Create a new Excel workbook
        workbook = openpyxl.Workbook()
        # Create a new sheet
        sheet = workbook.active
        
        # Extract and add data from each table to the sheet
        for index, table in enumerate(tables):
            # Add a new sheet for each table
            sheet = workbook.create_sheet(title=f'Table {index + 1}')
            for row in table.find_all('tr'):
                # Extract data from each row
                columns = row.find_all(['th', 'td'])
                data = [column.text.strip() for column in columns]
                # Add data to the sheet
                sheet.append(data)

        # Save the workbook to a file
        workbook.save(N +'.xlsx')
        print("Excel file created successfully.")

    else:
        print("Login failed")


    
