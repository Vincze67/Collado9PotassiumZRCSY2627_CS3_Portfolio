class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = None
        self.set_number_of_pages(number_of_pages)

    def set_number_of_pages(self, pages):
        if pages <= 0:
            print("The number of pages must be positive")
        else:
            self.__number_of_pages = pages

    def get_number_of_pages(self):
        return self.__number_of_pages

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.__number_of_pages}")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    def set_issue_number(self, issue):
        if issue <= 0:
            print("The issue number must be positive")
        else:
            self.__issue_number = issue

    def get_issue_number(self):
        return self.__issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")


pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)


print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.display_info()


print("\nMagazine Information:")
mag1.display_info()
