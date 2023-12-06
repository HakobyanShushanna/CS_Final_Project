import general_functions

file = "Tables\\budget.csv"
data = general_functions.get_data(file)

def add(user_id, category, amount, timeframe, start_date, end_date, spent, alert, status):
    max_id = max([int(line["Id"]) for line in data]) + 1 if len(data) > 0 else 1
    data.append({
        "Id" : max_id,
        "User Id" : user_id,
        "Category" : category,
        "Amount" : amount,
        "Timeframe" : timeframe,
        "Start Date" : start_date,
        "End Date" : end_date,
        "Spent Amount" : spent,
        "Alert Threshold" : alert,
        "Status" : status
    })
