from random import choice

with open("random_6000_words.txt", "r") as f:
    words = f.read().splitlines()

def get_username():
    name = []
    while True:
        name.append(choice(words).title())
        name.append(choice(words).title())
        
        if name[1] == name[0]:
            break

        return " ".join(name)
    
if __name__ == "__main__":
    print(get_username())