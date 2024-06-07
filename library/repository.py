from .models.book import BookModel

class BookRepository:
    def get_all_books(self):
        return BookModel.objects.all()

    def get_book_by_id(self, book_id):
        return BookModel.objects.get(id=book_id)

    def create_book(self, title, author, publisher, gender, pages, publish_date, checkin_date=None, is_available=True):
        return BookModel.objects.create(
            title=title,
            author=author,
            publisher=publisher,
            gender=gender,
            pages=pages,
            publish_date=publish_date,
            checkin_date=checkin_date,
            is_available=is_available
        )

    def update_book(self, book_id, title, author, publisher, gender, pages, publish_date, checkin_date=None, is_available=True):
        book = self.get_book_by_id(book_id)
        book.title = title
        book.author = author
        book.publisher = publisher
        book.gender = gender
        book.pages = pages
        book.publish_date = publish_date
        book.checkin_date = checkin_date
        book.is_available = is_available
        book.save()
        return book

    def delete_book(self, book_id):
        book = self.get_book_by_id(book_id)
        book.delete()
