class User:
    def __init__(self, user_id, username, followers):
        self.id = user_id
        self.username = username
        self.followers = 0 # ovako se setuje default vrednost
        self.following = 0
        print("New user created...") # __init__ funkcija/konstruktor se poziva svaki put kada se instancira objekat klase pa ce i ovaj print svaki put biti izvrsen

    # kada se kreira metoda klase kao prvi parametar mora da bude self
    # objektu user koji se prosledi povecava broj followers
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "pera password", None)
print(user_1.id)
print(user_1.username)
print(user_1.followers)
