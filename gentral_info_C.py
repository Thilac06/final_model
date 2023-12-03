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


    login_url = "https://pfm.smartcitylk.org/wp-login.php"
    target_url = "https://pfm.smartcitylk.org/wp-admin/admin.php?page=generalInfo"
    username = "thilacramesh@gmail.com"
    password = "TAFpfm#2133"

    session = requests.Session()

    login_data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'redirect_to': target_url,
    }
    login_response = session.post(login_url, data=login_data)

    if 'wp-admin' in login_response.url:
        target_response = session.get(target_url)

        if target_response.status_code == 200:
            soup = BeautifulSoup(target_response.content, 'html.parser')
            table = soup.find('table', {'id': 'table26'})
            x, y, z = 'Local Authority', 'Other Key', 'Another Key'
            local_authority_info = {cols[0].text.strip(): cols[1].text.strip() for cols in [row.find_all('td') for row in soup.find('table').find_all('tr') if len(row.find_all('td')) == 2]}

            N = (local_authority_info.get(x, f"{x} not found"))
            


            data = []

            for row in table.find_all('tr')[1:]:
                columns = row.find_all('td')

                if len(columns) >= 4:
                    input_2 = columns[2].find('input')
                    input_3 = columns[3].find('input')

                    in_running_condition = int(input_2['value']) if input_2 and 'value' in input_2.attrs and input_2['value'].isdigit() else None

                    not_running_condition = None
                    if input_3 and 'value' in input_3.attrs:
                        not_running_condition = int(input_3['value']) if input_3['value'].isdigit() else None

                    data.append({
                        f'In Running Condition:_{N}': in_running_condition,
                        f'Not Running Condition:_{N}': not_running_condition
                    })

            if data:
                # Check if the Excel file exists, if not create a new one
                try:
                    df = pd.read_excel('rutput_data.xlsx')
                except FileNotFoundError:
                    df = pd.DataFrame()

                new_data = pd.DataFrame(data)
                df = pd.concat([df, new_data], axis=1)

                # Save the DataFrame to an Excel file
                df.to_excel('rutput_data.xlsx', index=False)
                print("Data saved to output_data.xlsx")
            else:
                print("No data to display.")
        else:
            print(f"Failed to retrieve the target webpage. Status code: {target_response.status_code}")
    else:
        print("Login failed. Please check your credentials.")
driver.quit()
