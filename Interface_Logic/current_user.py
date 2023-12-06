class User:
    def __init__(self, user):
        self.first_name = user["First Name"]
        self.last_name = user["Last Name"]
        self.cards_ids = user["Cards Ids"]
        self.email = user["Email"]
        self.birth = user["Birth"]
        self.passport = user["Passport No"]
        self.password = user["Password"]
        self.phone_number = user["Phone Number"]
        self.currency = user["Preffered Currency"]
        self.picture = user["Profile Picture"]
        self.addresses = user["Addresses"]
        self.balance = user["Balance"]