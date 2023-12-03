from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd

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

    url = "https://pfm.smartcitylk.org/wp-login.php"
    target_url = "https://pfm.smartcitylk.org/wp-admin/admin.php?page=generalInfo"
    username = "kiruba00004@gmail.com"
    password = "TAFpfm#99283"

    payload = {
        'log': username,
        'pwd': password
    }

    session = requests.Session()

    try:
        response = session.post(url, data=payload)
        response.raise_for_status()

        if response.ok:
            print("Login successful.")

            
            page_response = session.get(target_url)
            page_response.raise_for_status()

            soup = BeautifulSoup(page_response.content, 'html.parser')

            
            details = {}

            sections = soup.find_all('section', {'class': 'content-header'})
            for section in sections:
                header = section.find('h3')
                if header and "Part B : Service related assets and infrastructure of LAs" in header.text:
                    form = section.find('form', {'id': 't37'})
                    if form:
                        tables = form.find_all('table')
                        for table in tables:
                            rows = table.find_all('tr')
                            for row in rows:
                                columns = row.find_all(['td', 'th'])
                                if len(columns) == 3:
                                    field_name = columns[0].text.strip()
                                    input_tag = columns[2].find('input')
                                    if input_tag:
                                        field_value = input_tag.get('value', '').strip()
                                        details[field_name] = field_value

            
            details_excel_file_path = 'details_output.xlsx'
            try:
                existing_details_df = pd.read_excel(details_excel_file_path, sheet_name='Details')
            except FileNotFoundError:
                existing_details_df = pd.DataFrame()

            
            new_details_df = pd.DataFrame([details])
            details_df_combined = pd.concat([existing_details_df, new_details_df], ignore_index=True)

            
            with pd.ExcelWriter(details_excel_file_path, engine='openpyxl') as writer:
                details_df_combined.to_excel(writer, index=False, sheet_name='Details')

           
            print(f"Details have been appended to the next row in {details_excel_file_path}")

        else:
            print(f"Login failed with status code {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

    finally:
        session.close()
    url = "https://pfm.smartcitylk.org/wp-login.php"
    target_url = "https://pfm.smartcitylk.org/wp-admin/admin.php?page=generalInfo"
    username = "kiruba00004@gmail.com"
    password = "TAFpfm#99283"

    payload = {
        'log': username,
        'pwd': password
    }

    session = requests.Session()

    try:
        response = session.post(url, data=payload)
        response.raise_for_status()

        if response.ok:
            page_response = session.get(target_url)
            page_response.raise_for_status()

            soup = BeautifulSoup(page_response.content, 'html.parser')
            form = soup.find('form', {'id': 't10'})

            if form:
                form_data = {}

                input_fields = form.find_all('input')
                for field in input_fields:
                    field_name = field.get('name')
                    field_value = field.get('value')
                    form_data[field_name] = field_value

                select_fields = form.find_all('select')
                for field in select_fields:
                    field_name = field.get('name')
                    field_value = field.find('option', {'selected': 'selected'}).get('value')
                    form_data[field_name] = field_value

                df = pd.DataFrame([form_data])

                excel_file_path = 'form_data_output.xlsx'

                
                try:
                    existing_df = pd.read_excel(excel_file_path, sheet_name='FormData')
                    df = pd.concat([existing_df, df], ignore_index=True)
                except FileNotFoundError:
                    pass

                with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='w') as writer:
                    df.to_excel(writer, index=False, sheet_name='FormData')

                print(f"Form data has been appended to the next row in {excel_file_path}")

            else:
                print("No form found on the page.")

        else:
            print(f"Login failed with status code {response.status_code}")

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

    finally:
        session.close()






























    
