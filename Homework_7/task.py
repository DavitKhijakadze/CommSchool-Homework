import requests

#task3
products = [
    {"id": 1, "price": 50},
    {"id": 2, "price": 200},
    {"id": 3, "price": 150}
]

expensive_products = []

for product in products:
    if product["price"] > 100:
        expensive_products.append(product)

print(expensive_products)


#task4

company_data = {
    "company": {
        "departments": [
            {"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
            {"name": "HR", "employees": [{"name": "Nino"}]}
        ]
    }
}

departments = company_data["company"]["departments"]

for dept in departments:
    for employee in dept["employees"]:
        print(employee["name"])

#task5

students = [
    {"name": "Ana", "grades": [90, 80, 95]},
    {"name": "Beka", "grades": [70, 85, 88]},
    {"name": "Nino", "grades": [100, 95, 99]}
]

best_student = None
highest_average = 0

for student in students:
    current_average = sum(student["grades"]) / len(student["grades"])
    
    if current_average > highest_average:
        highest_average = current_average
        best_student = student["name"]

print(f"{best_student} has the highest score - {highest_average}")


#task6

data = {
    "companies": [
        {
            "name": "TechCorp",
            "employees": [
                {"name": "Ana", "salary": 3000},
                {"name": "Beka", "salary": 4500}
            ]
        },
        {
            "name": "SoftPlus",
            "employees": [
                {"name": "Nino", "salary": 5000},
                {"name": "Giorgi", "salary": 2500}
            ]
        }
    ]
}

for company in data["companies"]:
    company_name = company["name"]    
    for employee in company["employees"]:
        if employee["salary"] > 4000:
            print(f"name: {employee['name']}, company: {company_name}")


#task7

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json()

first_user_name = users[0]["name"]

print(first_user_name)


#task8

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Test",
    "body": "Hello World",
    "userId": 5
}

response = requests.post(url, json=payload)

if response.status_code == 201:
    print("Post created successfully")
    
    created_post = response.json()
    print(f"sercer response: {created_post}")
else:
    print(f"error!: {response.status_code}")


#task9

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

if response.status_code == 200:
    todos = response.json()
    
    incomplete_count = 0
        
    for task in todos:
        if not task["completed"]:
            print(f"ID: {task['id']} | Title: {task['title']}")
            incomplete_count += 1
            
    print(f"Total number of incomplete tasks: {incomplete_count}")
else:
    print(f"Error! Status code: {response.status_code}")


#task10

posts_url = "https://jsonplaceholder.typicode.com/posts"
users_url = "https://jsonplaceholder.typicode.com/users"

posts_response = requests.get(posts_url)
users_response = requests.get(users_url)

if posts_response.status_code == 200 and users_response.status_code == 200:
    posts = posts_response.json()
    users = users_response.json()
    
    user_mapping = {user["id"]: user["name"] for user in users}
        
    for post in posts:
        post_title = post["title"]
        user_id = post["userId"]    
        author_name = user_mapping.get(user_id, "Unknown Author")
        
        print(f"{post_title} – {author_name}")       
else:
    print("Failed to fetch data from one or both endpoints")