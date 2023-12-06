import general_functions

file = "Tables\\transactions.csv"
data = general_functions.get_data(file)

def search_by_date(date):
    for line in data:
        if line["Date"] == date:
            return True
    return False

def find_by_reciver(reciver):
    result = []
    for line in data:
        if line["Reciver"] == reciver:
            result.append(line)
    return line

def find_by_from(from_user):
    result = []
    for line in data:
        if line["From"] == from_user:
            result.append(line)
    return line

def find_by_date(date):
    for line in data:
        if line["Date"] == date:
            return line
    return "Not found"

def add(amount, from_user, reciver, date, description, category):
    if not search_by_date(date):
        max_id = max([int(line["Id"]) for line in data]) + 1 if len(data) > 0 else 1

        data.append({
            "Id": max_id,
            "Amount" : amount,
            "From" : from_user,
            "Reciver" : reciver,
            "Date" : date,
            "Description" : description,
            "Category" : category
        })

        general_functions.rewrite_data(file, data)