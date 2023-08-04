def login():
    username = input("Usuario: ")
    password = input("Password: ")

    if username == "Papi" and password == "040823":
        print("HAPPY BIRTHDAY DAN! You managed to decipher the messages makes me proud.I hope you have an excellent birthday. I wish you all the beauty that this world has to offer. Wishing you liked this little detail (I don't want my red ass) I couldn't think of anything else so that you could receive it from a distance. You are a very important person to me, I receive the gift by having you in my life today and thank you for all the beautiful things you do for all the people around you. TE QUIERO MUCHO!")
    else:
        print("ARE YOU REALLY BAD WITH DATES")
        login()
login()        