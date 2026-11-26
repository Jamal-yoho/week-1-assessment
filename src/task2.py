import csv
import json
import requests

with open("data/employees.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

with open("data/employees.json", "w") as file:
    json.dump(employees, file, indent = 4)

print("Total employees:", len(employees))
print("Json file created successfull")

with open ("data/high_earners.csv","w",newline="") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()

    for emp in employees:
        if int(emp["salary"])> 50000:
            writer.writerow(emp)

print("High earners csv creadted")

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

print("API Key loaded:", api_key is not None)


try:
    response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=5)
    response.raise_for_status()
    users = response.json()

    with open("data/users.json", "w")as file:
        json.dump(users, file, indent=4)
    print("Users JSON saved successfully")

    for user in users[:3]:
        print(user["id"],user["name"],user["email"])
        print(user.get("address", {}).get("city"))


except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")

except requests.exceptions.HTTPError as e:
    print("HTTP Error", e)

try:
    response = requests.get("https://jsonplaceholder.typicode.com/9999", timeout=5)
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("404 Error: User not found")
