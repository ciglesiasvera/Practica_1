import json

with open("PYTHON/MODULO_4/SESION_9/employees.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    
# Basic operations - Show the json information
print("----------Lista de Empleados----------")
for employee in data["employees"]:
    print(f"Nombre: {employee['name']}, Edad: {employee['age']}, Ciudad: {employee['city']}")

#Get de average age in employee
total_age = sum(employee["age"] for employee in data["employees"])
average_age = total_age / len(data["employees"])
print(f"\nEdad promedio de los empleados: {average_age:.2f} años")

#Find employee by city
city = "London"
employees_in_city = [emp['name'] for emp in data["employees"] if emp["city"] == city]
print(f"\n Empleados en la ciudad {city}: {', '.join(employees_in_city)}")

# Adding a new employee
new_employee = {"name": "Roberto", "age": 38, "city": "Tlaxcala"}
data['employees'].append(new_employee)
new_employee = {"name": "Cristian", "age": 55, "city": "Temuco"}
data['employees'].append(new_employee)

# Save the changes
with open("PYTHON/MODULO_4/SESION_9/employees.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent = 4)
    
print("\n Nuevo empleado agregado con éxito")