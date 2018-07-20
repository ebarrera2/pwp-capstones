class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.address = address
        self.email = self.address
        print("Your email has been updated to {new_email}".format(new_email = self.email))

    def __repr__(self):
        return "User {user}, email: {email}, books read: {books_read}".format(user = self.name, email = self.email, books_read = len(self.books.keys()))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else: return False

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        added_values = 0
        for value in self.books.values():
            if value:
                added_values += value
        return added_values / len(self.books.keys())

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.new_isbn = new_isbn
        self.isbn = self.new_isbn
        print("The ISBN for {book} has been updated to {isbn}".format(book = self.title, isbn = self.isbn))

    def add_rating(self, rating):
        if rating and rating > 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            return "Invalid Rating"

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else: return False

    def get_average_rating(self):
        summed_values = 0
        for value in self.ratings:
            summed_values += value
        return summed_values / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{title} - ISBN: {isbn}".format(title = self.title, isbn = self.isbn)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    #Get Creative! Determining if two TomeRater objects are equal
    def __eq__ (self, other_rater):
      if self == other_rater:
        return True
      else: return False

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] +=1
            else: self.books[book] = 1
        else: print("No user with email {email}".format(email = email))

    def add_user(self, name, email, books = None):
        new_user = User(name, email)
        self.users[email] = new_user
        if books != None:
            for book in books:
                self.add_book_to_user(book, email)

    #Get Creative! Error message for adding a user that already exists.
    def check_for_email(self, name, email):
        if email in self.users:
          print("A user with this email already exists. Please add a different email.")
        else: self.add_user(name, email) 

    #Get Creative! check for valid email address
    def check_for_valid_email(self, name, email):
      if "@" not in email:
        print("Invalid email address.")
      elif email.endswith((".com", ".org", ".edu")) == False:
        print("Invalid email address.")
      else: self.check_for_email(name, email)

    def print_catalog(self):
        for key in self.books.keys():
            print(key)
    
    def print_users(self):
        for value in self.users.values():
            print(value)
    
    def most_read_book(self):
        most_read = ""
        highest_num = 0
        for key, value in self.books.items():
            if value > highest_num:
                highest_num = value
                most_read = key
        return most_read

    def highest_rated_book(self):
        highest_rated = ""
        highest_rating = 0
        for key in self.books.keys():
            if key.get_average_rating() > highest_rating:
                highest_rating = key.get_average_rating()
                highest_rated = key
        return highest_rated

    def most_positive_user(self):
        max_rating = 0
        most_positive = None
        for user in self.users.values():
            if user.get_average_rating() > max_rating:
                max_rating = user.get_average_rating()
                most_positive = user
        return most_positive.name