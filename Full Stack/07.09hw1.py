#Создайте функцию, которая принимает вложенный словарь (представляющий собой информацию о компаниях и их сотрудниках)
# и возвращает новый словарь, содержащий только сотрудников определенной должности (например, "developer").
company_info = {
    "Company A": [
        {"name": "Alice", "position": "developer"},
        {"name": "Bob", "position": "manager"}
    ],
    "Company B": [
        {"name": "Charlie", "position": "developer"},
        {"name": "David", "position": "designer"}
    ]
}


print({k:[employee for employee in v if employee["position"] == "developer"]for k,v in company_info.items()})

filtered_companies = {k: [employee for employee in v if employee["position"] == "developer"] for k, v in company_info.items()}
for company, employees in filtered_companies.items():
    print(f"{company}: {employees}")

print({k:[employee for employee in v if employee["position"] == "developer"]for k,v in company_info.items()}, sep="\n")

print({k:[employee for employee in v if employee["position"] == "developer"] for k,v in company_info.items()})

