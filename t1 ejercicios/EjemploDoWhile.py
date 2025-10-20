email = ""

while True:
    email = input("Introduce un email: ")

    if print(email.endswith("@fundacionmontessori.com")):
        break
    else:
        print("Email invalido")
print("Email: ", email)