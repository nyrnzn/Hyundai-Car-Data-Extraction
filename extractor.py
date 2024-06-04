import requests  # Library for making HTTP requests
import json  # Library for working with JSON data
import csv  # Library for working with CSV files
from datetime import datetime  # Library for working with date and time

def get_model_list():
  """
  Fetches a list of car models from Hyundai's Click to Buy platform.

  Returns:
      A dictionary containing the list of car models if successful, None otherwise.
  """
  url = "https://clicktobuy.hyundai.co.in/ctb/customer/modelList.ctb"
  payload = {}

  try:
    response = requests.post(url, data=payload)
    if response.status_code == 200:
      data = response.json()
      return data
    else:
      print("Error: Unexpected response from the server")
      return None
  except requests.exceptions.RequestException as e:
    print("Error:", e)
    return None


def select_a_car(model_code, modl_aem_id, model_desc):
  """
  Retrieves details (including variant and price) for a specific car model.

  Args:
      model_code (str): The code of the car model.
      modl_aem_id (str): The AEM ID of the car model.
      model_desc (str): The description of the car model.

  Returns:
      A dictionary containing car details if successful, None otherwise.
  """
  url = "https://clicktobuy.hyundai.co.in/ctb/customer/selectACar.ctb"
  payload = {
      "modelCode": model_code,
      "stteCode": "",
      "modlAemId": modl_aem_id,
      "cityCode": "",
      "cstmId": "",
      "delrId": "",
      "modelId": modl_aem_id,
      "modelDesc": model_desc
  }

  try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
      data = response.json()
      return data
    else:
      print("Error: Unexpected response from the server")
      return None
  except requests.exceptions.RequestException as e:
    print("Error:", e)
    return None

# Call the function to get the model list
model_list_response = get_model_list()

print("Model List:")
print(model_list_response)  # Print the retrieved model list for debugging (optional)

# Check if model list is retrieved successfully
if model_list_response and 'modelList' in model_list_response:
  model_list = model_list_response['modelList']

  current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
  export_file_name = f"car_data_{current_datetime}.csv"

  with open(export_file_name, 'w', newline='') as csvfile:
    fieldnames = ['Model', 'Varient', 'ExShowroomPrice']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for model in model_list:
      model_code = model.get("modelCode")
      modl_aem_id = model.get("modlAemId")
      model_desc = model.get("modelDesc")
      if model_code and modl_aem_id and model_desc:
        print("Selected Model Code:", model_code)
        # Call select_a_car function with the selected model code
        response = select_a_car(model_code, modl_aem_id, model_desc)
        if response and response["modelList"]:
          for single_model in response["modelList"]:
            varient = single_model["vrntDesc"]
            car_data = {
              "Model": model_desc,
              "Varient": single_model["vrntDesc"],
              "ExShowroomPrice": single_model["exSwrmPrce"]
            }
            writer.writerow(car_data)
        else:
          print("Failed to retrieve varients data from selectACar API response")
      else:
        print("Failed to extract necessary information from model list")
    print("Data extraction completed")
else:
    print("Failed to retrieve model list")