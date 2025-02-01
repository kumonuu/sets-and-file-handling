file = open("credentials.txt", "w")

social_media = input("What is your social media: ")
username = input("What is your username? ")
password = input("What is your password? ")

file.write(f"Website: {social_media}\n")
file.write(f"Password: {password}\n")
file.write(f"Username: {username}")

file.close()