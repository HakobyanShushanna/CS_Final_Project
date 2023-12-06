import general_functions

file = "Tables\\users.csv"
data = general_functions.get_data(file)

def add(first_name, last_name, cards_ids, email, birth, passport_no, password, phone, currency, picture, addresses, balance):
    if general_functions.search(email, data) == None:
        max_id = max([int(line["Id"]) for line in data]) + 1 if len(data) > 0 else 1
        password = general_functions.hash_password(password)
        
        data.append({
            "Id" : max_id,
            "First Name" : first_name,
            "Last Name" : last_name,
            "Cards Ids" : cards_ids,
            "Email" : email,
            "Birth" : birth,
            "Passport No" : passport_no,
            "Password" : password,
            "Phone Number" : phone,
            "Preffered Currency" : currency,
            "Profile Picture" : picture,
            "Addresses" : addresses,
            "Balance" : balance
        })

        general_functions.rewrite_data(file, data)