class Book:
    #pass esto significa,(pass), que la clase no hará nada
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
#Class Newspaper
class Newspaper:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
#Class magazine
class Magazine:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
#Class brochure
class Brochure:
    def __init__(self, title, author):
        self.title = title
        self.author = author

#Main
#Creationg an object
book1 = Book("100 anios de soledad", "Gabriel Garcia Marquez")
book2 = Book("Codigo limpio", "Robert C. Martin")
newspaper = Newspaper("New York TImes", "John Tripe")
newspaper2 = Newspaper("El Diario Austral", "Peter Red")
magazine = Magazine("IA Today", "Carl Smart")
magazine2 = Magazine("IoT", "Peter Selllers")
brochure = Brochure("Health", "Anne Brooks")
brochure2 = Brochure("Java esentials", "John Johnsson")

#Calling an object from book class
print(book1)
print(book2)
print(book2.title)
print(book1.author)
print(book2.author)

#Calling an object from newspaper class
print(newspaper)
print(newspaper2)
print(newspaper2.title)
print(newspaper.author)
print(newspaper2.author)

#Calling an object from magazine class
print(magazine)
print(magazine2)
print(magazine2.title)
print(magazine.author)
print(magazine2.author)

#Calling an object from brochure class
print(brochure)
print(brochure2)
print(brochure2.title)
print(brochure.author)
print(brochure2.author)