try:
    with open('profile.txt','r') as file:
        content=file.read()
    print(content)
except FileNotFoundError:
    print("File Not Found")