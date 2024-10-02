import requests
import pymongo

# ... (CDC API interaction code - Replace with your API call) ...
api_url = "https://data.cdc.gov/resource/7vg3-e5u2.json" # CDC API URL

try:
    response = requests.get(api_url)
    response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
    data = response.json() # Assuming JSON response

    client = pymongo.MongoClient("mongodb://mongodb:27017")
    db = client["asd_db"] # Replace with your database name
    collection = db["asd_data_cdc"]
    collection.insert_many(data) #or insert_one if only one document
    print("Data inserted successfully into MongoDB")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from CDC API: {e}")
except Exception as e:
    print(f"An error occurred: {e}")