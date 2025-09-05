import random
def load_quotes(filename):
    try:
        with open(filename) as quotes:
            file = quotes.readlines()
        return file
    except FileNotFoundError: print("File not found")

def get_random_quote(quotes):
    return random.choice(quotes) if quotes else "ERROR: NO QUOTES"

def add_to_favorites(random_quote):
    try:
        with open("favorites.txt", 'a') as file:
            file.write(random_quote)
    except FileNotFoundError: print("File not found")
def view_favorites():
    try:
        with open('favorites.txt') as file:
            return [f.strip() for f in file.readlines()]
    except FileNotFoundError: print("File not found")

if __name__ == "__main__":
    some_quote = get_random_quote(load_quotes("quotes.txt"))
    add_to_favorites(some_quote)
    some_quote = get_random_quote(load_quotes("quotes.txt"))
    add_to_favorites(some_quote)
    some_quote = get_random_quote(load_quotes("quotes.txt"))
    add_to_favorites(some_quote)
    print(view_favorites())



