import random
def load_quotes(filename):
    file = open(filename)
    quotes = file.readlines()
    file.close()
    return quotes

def get_random_quote(quotes):
    random_quote = random.choice(quotes)
    return random_quote

def add_to_favorites(random_quote):
    file = open("favorites.txt", 'a')
    file.write(random_quote)
    file.close()
def view_favorites():
    file = open('favorites.txt')
    favorites = file.readlines()
    file.close()
    new_favorites = []
    for f in favorites:
        new = f.strip()
        new_favorites.append(new)
    return new_favorites

if __name__ == "__main__":
    some_quote = get_random_quote(load_quotes("quotes.txt"))
    add_to_favorites(some_quote)
    some_quote = get_random_quote(load_quotes("quotes.txt"))
    add_to_favorites(some_quote)
    some_quote = get_random_quote(load_quotes("quotes.txt"))
    add_to_favorites(some_quote)
    print(view_favorites())



