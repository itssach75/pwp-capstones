
class User(object):
    """
    User has a name, an email, and a dictionary of books with optional ratings
    for each book. It will be used by TomeRater class to link with instances of Books.
    """
    def __init__(self, name, email):
        """
        Constructor to set the name and email instance attributes based on the
        arguments passed. Creates an empty dictionary of books to be populated
        through the read_book method.
        """
        if email.find("@") == -1 or (email.find(".com") == -1 and email.find(".edu") == -1 and email.find(".org") == -1):
            print("The email {email} is invalid, please ensure it has an @ and a .com, .edu, or .org domain.".format(email=email))
        else:
            self.name = name
            self.email = email
            self.books = {}

    def __repr__(self):
        """
        Returns a human readable message giving the name, email, count of books,
        and average rating of books.
        """
        cnt = 0
        for item in self.books.keys():
            cnt += 1
        return "User {name} with email {email} has read {count} book(s) with an average rating of {rating}".format(name=self.name,email=self.email,count=cnt,rating=self.get_average_rating())

    def __eq__(self, other_user):
        """
        Evaluates equivalency between two User objects. If argument other_user
        is not of type User, it will print a message asking for the other_user
        to be of type User.
        """
        if isinstance(other_user, User):
            return self.name == other_user.name and self.email == other_user.get_email()
        else:
            print("Object on the right side of the equality is of type {type}, and should be of type User".format(type=type(other_user)))

    def get_email(self):
        """
        Returns the email of the User instance.
        """
        return self.email

    def get_name(self):
        """
        Returns the name of the User instance.
        """
        return self.name

    def change_email(self, address):
        """
        Alters the email based on the argument passed, and prints a human
        readable messeage to indicate the changes made.
        """
        if address.find("@") == -1 or address.find(".com") == -1 or address.find(".edu") == -1 or address.find(".org") == -1:
            print("The eamil {email} is invalid, please ensure it has an @ and a .com, .edu, or .org domain.".format(email=address))
        else:
            old_email = self.email
            self.email = address
            print("{name}'s email has changed from {old} to {new}".format(name=self.name,old=old_email,new=self.email))

    def read_book(self, book, rating=None):
        """
        Adds a book to the books dictionary with an optional rating. The default
        for rating is None. Dictionary books is only updated if the book
        argument is of type Book. Otherwise, it prints a message asking for an
        argument of type Book.
        """
        if isinstance(book, Book):
            self.books.update({book: rating})
        else:
            print("Argument book is not of type Book. Please pass a Book instance.")

    def get_average_rating(self):
        """
        Returns the average rating for all books with a rating. Any books with a
        rating of None will be ignored. If there are no books, or all ratings
        are None, then a human readable message about that is printed.
        """
        total = 0
        n = 0
        if len(self.books) > 0:
            for rating in self.books.values():
                if rating:
                    total += rating
                    n += 1
                else:
                    continue
        if n > 0:
            return total/n
        else:
            print("There are no books with ratings for {user}".format(user=self.name))

    def get_books_read(self):
        """
        Returns the number of books read by the User instance.
        """
        return len(self.books)

class Book(object):
    """
    Book has a title, an isbn, and a list of ratings. It is subclassed by Fiction
    and Non-Fiction.
    """
    def __init__(self, title, isbn, price):
        """
        Constructor to set the tital and isbn instance attributes based on the
        arguments passed. Creates an empty list of ratings to be populated
        through the add_rating method.
        """
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    def __eq__(self, other_book):
        """
        Evaluates equivalency between two Book objects. If argument other_book
        is not of type Book, it will print a message asking for the other_book
        to be of type Book.
        """
        if isinstance(other_book, Book):
            return self.title == other_book.title and self.isbn == other_book.isbn
        else:
            print("Object on the right side of the equality is of type {type}, and should be of type User".format(type=type(other_book)))

    def __hash__(self):
        """
        Creates a hash method for the Book object. This is used to have the Book
        instances used as keys in the books dictionary in the User object.
        """
        return hash((self.title, self.isbn))

    def get_title(self):
        """
        Returns the title of the Book instance.
        """
        return self.title

    def get_price(self):
        """
        Returns the price of the Book instance.
        """
        return self.price

    def get_isbn(self):
        """
        Returns the isbn of the Book instance.
        """
        return self.isbn

    def set_isbn(self, isbn):
        """
        Alters the isbn based on the argument passed, and prints a human
        readable messeage to indicate the changes made.
        """
        old_isbn = self.isbn
        self.isbn = isbn
        print("{title}'s isbn has changed from {old} to {new}".format(title=self.title,old=old_isbn,new=self.isbn))

    def add_rating(self, rating):
        """
        Adds a rating to the self.ratings list if the rating is between 0 and 4
        inclusively. Prints a human readable message if the rating is invalid.
        """
        if not rating or rating < 0 or rating > 4:
            print("{rating} is invalid. Please pass a numeric rating between 0 and 4 inclusive.".format(rating=rating))
        else:
            self.ratings.append(rating)

    def get_average_rating(self):
        """
        Returns the average rating for this Book instance with a rating. If
        there are no ratings, then prints a message stating that.
        """
        total = 0
        n = 0
        if len(self.ratings) > 0:
            for rating in self.ratings:
                total += rating
                n += 1
            return total/n
        else:
            print("There are no ratings for {title}".format(title=self.title))

class Fiction(Book):
    """
    Fiction is a subclass of Book with an additional author attribute. It is used by
    TomeRater class to combine with Users instances.
    """
    def __init__(self, title, isbn, author, price):
        """
        Constructor using the Book superclass' constructor passing title and isbn.
        Adds subject and level to the instance based on arguments.
        """
        #super().__init__(title, isbn, author, price)
        super().__init__(title, isbn, price)
        self.author = author

    def __repr__(self):
        """
        Returns a human readable message with the title and author of the instance.
        """
        return "{title} by {author} for ${price}".format(title=self.title,author=self.author,price=self.price)

    def get_author(self):
        """
        Returns the author of the instance.
        """
        return self.author

class Non_Fiction(Book):
    """
    Non_Fiction is a subclass of Book with additional level and subject attributes.
    It is used by TomeRater class to combine with Users instances.
    """
    def __init__(self, title, isbn, level, subject, price):
        """
        Constructor using the Book superclass' constructor passing title and isbn.
        Adds subject and level to the instance based on arguments.
        """
        super().__init__(title, isbn, price)
        self.level = level
        self.subject = subject

    def __repr__(self):
        """
        Returns a human readable message with the title, level, and subject of the
        instance.
        """
        return "{title}, a {level} manual on {subject} for ${price}".format(title=self.title,level=self.level,subject=self.subject,price=self.price)

    def get_subject(self):
        """
        Returns the subject of the instance.
        """
        return self.subject

    def get_level(self):
        """
        Returns the level of the instance.
        """
        return self.level

class TomeRater(object):
    """
    TomeRater orchestrates the interactions between Users and Books instances.
    """
    def __init__(self):
        """
        Constructor creating empty dictionaries of users and books.
        """
        self.users = {}
        self.books = {}

    def __repr__(self):
        """
        Returns a human readable message with the number of books, users,
        most read book, highest rated book, and the most positive user.
        """
        n_books = len(self.books)
        n_users = len(self.users)
        most_read = self.most_read_book()
        highest_rated = self.highest_rated_book()
        most_positive = self.most_positive_user()

        return "This TomeRater has {books} book(s) and {users} user(s).\nWith {most_read} being read the most, {highest} having the highest average rating,\nand {most_positive} giving the most positive reviews.".format(books=n_books,users=n_users,most_read=most_read,highest=highest_rated,most_positive=most_positive)

    def __eq__(self, other_rater):
        """
        Defines the conditions for equality between TomeRater instances. Uses
        __eq__ property of dictionaries for books and users between two
        TomeRater instances.
        """
        if isinstance(other_rater, TomeRater):
            return self.books == other_rater.books and self.users == other_rater.users
        else:
            print("Object on the right side of the equality is of type {type}, and should be of type TomeRater".format(type=type(other_rater)))


    def create_book(self, title, isbn, price):
        """
        Returns an instance of a Books object.
        """
        isbns = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbns:
            print("The isbn {isbn} already exists for another book. Please give a unique isbn.".format(isbn=isbn))
        else:
            return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price):
        """
        Returns an instance of a Fiction object.
        """
        isbns = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbns:
            print("The isbn {isbn} already exists for another book. Please give a unique isbn.".format(isbn=isbn))
        else:
            return Fiction(title, isbn, author, price)

    def create_non_fiction(self, title, level, subject, isbn, price):
        """
        Returns an instance of a Non_Fiction object.
        """
        isbns = [book.get_isbn() for book in self.books.keys()]
        if isbn in isbns:
            print("The isbn {isbn} already exists for another book. Please give a unique isbn.".format(isbn=isbn))
        else:
            return Non_Fiction(title, isbn, subject, level, price)

    def add_book_to_user(self, book, email, rating=None):
        """
        Adds a book to a user in self.users, then increases the value in self.books
        for this book by 1. If it is not already in self.books, then it adds it with
        a value of 1.
        """
        if self.users.get(email):
            self.users[email].read_book(book, rating)
            self.books[book] = self.books.get(book, 0) + 1
            if rating:
                    book.add_rating(rating)
        else:
            print("No user with email {email}!".format(email=email))

    def add_user(self, name, email, books=None):
        """
        Creates a new user instance with name and email. Then, loops thorugh
        books, if provided, and calls add_book_to_user on each.
        """
        if email.find("@") == -1 or (email.find(".com") == -1 and email.find(".edu") == -1 and email.find(".org") == -1):
            print("The eamil {email} is invalid, please ensure it has an @ and a .com, .edu, or .org domain.".format(email=email))
        else:
            user = self.users.get(email)
            if user:
                print("User {name} currently exists with email {email}. Please use a different email.".format(name=user.get_name(),email=email))
            else:
                self.users.update({email: User(name, email)})
                if books:
                    for book in books:
                        self.add_book_to_user(book, email)

    def print_catalog(self):
        """
        Prints all of the books in the self.books dictionary.
        """
        for book in self.books.keys():
            print(book)

    def print_users(self):
        """
        Prints all of the users in the self.users dictionary.
        """
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        """
        Returns the book which has been read the most.
        """
        max_reading = 0
        max_book = ""
        for book, reading in self.books.items():
            if reading > max_reading:
                max_book = book
                max_reading = reading
            else:
                continue
        return max_book

    def highest_rated_book(self):
        """
        Returns the book which has the highest average rating.
        """
        max_rating = 0
        max_book = ""
        for book in self.books.keys():
            rating = book.get_average_rating()
            if rating > max_rating:
                max_book = book
                max_rating = rating
            else:
                continue
        return max_book

    def most_positive_user(self):
        """
        Returns the user which gives the highest average rating.
        """
        max_rating = 0
        max_user = ""
        for user in self.users.values():
            rating = user.get_average_rating()
            if rating > max_rating:
                max_user = user
                max_rating = rating
            else:
                continue
        return max_user

    def get_n_most_read_books(self, n):
        """
        Returns the n books which have been read the most in descending order.
        """
        if type(n) == int:
            books_sorted = [k for k in sorted(self.books, key=self.books.get, reverse=True)]
            return books_sorted[:n]
        else:
            print("The argument n = {n} is not of type int. Please pass an int.".format(n=n))

    def get_n_most_prolific_readers(self, n):
        """
        Returns the n readers which have read the most books in descending order.
        """
        if type(n) == int:
            readers = [(reader, reader.get_books_read()) for reader in self.users.values()]
            readers_sorted = [k[0] for k in sorted(readers, key=lambda reader: reader[1], reverse=True)]
            return readers_sorted[:n]
        else:
            print("The argument n = {n} is not of type int. Please pass an int.".format(n=n))

    def get_n_most_expensive_books(self, n):
        """
        Returns the n books which have the highest price in descending order.
        """
        if type(n) == int:
            books = {book: book.get_price() for book in self.books.keys()}
            books_sorted = [k for k in sorted(books, key=books.get, reverse=True)]
            return books_sorted[:n]
        else:
            print("The argument n = {n} is not of type int. Please pass an int.".format(n=n))

    def get_worth_of_user(self, user_email):
        """
        Determines the total price of all books read by the user associated
        with the user_email argument.
        """
        if user_email.find("@") == -1 or (user_email.find(".com") == -1 and user_email.find(".edu") == -1 and user_email.find(".org") == -1):
            print("The {email} is invalid, please ensure it has an @ and a .com, .edu, or .org domain.".format(email=user_email))
        else:
            user = self.users.get(user_email)
            if not user:
                print("User does not currently exist with email {email}. Please use an email for a valid user.".format(email=user_email))
            else:
                price = 0
                for book in user.books.keys():
                    price += book.get_price()
                return price
