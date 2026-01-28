#Exerci 02, demander l'âge de l'utilisateur et afficher s'il est majeur ou mineur

age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")