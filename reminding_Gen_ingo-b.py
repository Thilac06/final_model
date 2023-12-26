import requests
from bs4 import BeautifulSoup
import pandas as pd

# Authentication details
login_url = "https://pfm.smartcitylk.org/wp-login.php"
target_url = "https://pfm.smartcitylk.org/wp-admin/admin.php?page=generalInfo"
username = "thilacramesh@gmail.com"
password = "TAFpfm#2133"

# Create a session to persist the login credentials
session = requests.Session()

try:
    # Perform login
    login_payload = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Log In',
        'redirect_to': target_url,
    }

    login_response = session.post(login_url, data=login_payload)

    # Check if login was successful (status code 200)
    if login_response.status_code == 200:
        # Make a GET request to the target URL after login
        target_response = session.get(target_url)

        # Check if the request was successful (status code 200)
        if target_response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(target_response.content, 'html.parser')

            # Find all input elements with specific names
            input_elements = soup.find_all('input', {'name': ['table37_22', 'table37_23', 'table37_24', 'table37_25',
                                                               'table37_26', 'table37_27', 'table37_28', 'table37_29',
                                                               'table37_30', 'table37_31', 'table37_32', 'table37_33',
                                                               'table37_34']})

            # Extract details and store them in a dictionary
            details = {}
            for input_element in input_elements:
                input_name = input_element['name']
                input_value = input_element['value']
                details[input_name] = input_value

            # Load existing details if the file exists
            details_excel_file_path = 'details_output.xlsx'
            try:
                existing_details_df = pd.read_excel(details_excel_file_path, sheet_name='Details')
            except FileNotFoundError:
                existing_details_df = pd.DataFrame()

            # Combine existing details with new details
            new_details_df = pd.DataFrame([details])
            details_df_combined = pd.concat([existing_details_df, new_details_df], ignore_index=True)

            # Write combined details to Excel file
            with pd.ExcelWriter(details_excel_file_path, engine='openpyxl') as writer:
                details_df_combined.to_excel(writer, index=False, sheet_name='Details')

            print(f"Details have been appended to the next row in {details_excel_file_path}")

        else:
            print(f"Failed to retrieve the target page. Status code: {target_response.status_code}")

    else:
        print(f"Login failed. Status code: {login_response.status_code}")

except requests.RequestException as e:
    print(f"An error occurred: {e}")

finally:
    session.close()
