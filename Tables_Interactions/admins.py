import general_functions

file = "Tables\\admins.csv"
data = general_functions.get_data(file)

#### BASIC FUNCTIONS ####

def add(first_name, last_name, position, email, password):
    if not general_functions.search(email, data) != None:
        max_id = max([int(line["Id"]) for line in data]) + 1 if len(data) > 0 else 1
        password = general_functions.hash_password(password)
        
        data.append(
            {"Id" : max_id,
             "First Name" : first_name,
             "Last Name" : last_name,
             "Position" : position,
             "Email" : email,
             "Password" : password}
        )
        general_functions.rewrite_data(file, data)

#### ADVANCED OPTIONS FOR SOME POSITIONS ####

def find_positions(position):
    result = []
    for line in data:
        if line["Position"] == position:
            result.append(line)
    return result

def search_by_position(search_position, position):
    search_position = search_position.title()
    position = position.title()
    if position == "Super Admin":
        return find_positions(search_position)
    return "You don't have access to this feature"

# TODO: Remove these lines
# add("Shushanna", "Hakobyan", "Sysadmin", "shushanna_hakobyan@gmail.com", "Something!")
# remove("shushanna_hakobyan@edu.aua.am")
# print(search("shushanna_hakobyan@gmail.com"))
# print(search_by_position("Super Admin", "Super Admin"))