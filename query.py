from config import *

import psycopg2
from psycopg2 import Error

def find_book(book_title):
    try:
        with psycopg2.connect(host=host, 
                              user=user, 
                              password=password,
                                database=db_name)    as connection:

            with connection.cursor() as cursor:
                # query = """INSERT INTO books (bname, authors, publisher, byear, isbn, annotation, chapter)
                # VALUES 
                #     ('1984', 'George Orwell', 'Harcourt, Brace and Company', 1949, '0451524934', '1984, published in 1949, is a dystopian novel by George Orwell.', 'Part 1, Chapter 1'),
                #     ('To Kill a Mockingbird', 'Harper Lee', 'J. B. Lippincott & Co.', 1960, '0061120081', 'To Kill a Mockingbird is a novel by Harper Lee published in 1960.', 'Chapter 1'),
                #     ('The Great Gatsby', 'F. Scott Fitzgerald', 'Charles Scribners Sons', 1925, '9780743', 'The Great Gatsby is a 1925 novel by American writer F. Scott Fitzgerald.', 'Chapter 1'),
                #     ('Moby-Dick', 'Herman Melville', 'Richard Bentley', 1851, '1853260084', 'Moby-Dick; or, The Whale is an 1851 novel by American writer Herman Melville.', 'Chapter 1'),
                #     ('Pride and Prejudice', 'Jane Austen', 'T. Egerton, Whitehall', 1813, '9780569', 'Pride and Prejudice is a romantic novel of manners written by Jane Austen in 1813.', 'Chapter 1'),
                #     ('The Catcher in the Rye', 'J.D. Salinger', 'Little, Brown and Company', 1951, '978031', 'The Catcher in the Rye is a novel by J. D. Salinger, partially published in serial form in 1945–1946 and as a novel in 1951.', 'Chapter 1'),
                #     ('Don Quixote', 'Miguel de Cervantes', 'Francisco de Robles', 1605, '9780047', 'Don Quixote, novel published in two parts (part 1, 1605; part 2, 1615) by Miguel de Cervantes.', 'Chapter 1'),
                #     ('War and Peace', 'Leo Tolstoy', 'The Russian Messenger', 1869, '977934', 'War and Peace is a novel by the Russian author Leo Tolstoy, first published serially, then published in its entirety in 1869.', 'Chapter 1'),
                #     ('Alices Adventures in Wonderland', 'Lewis Carroll', 'Macmillan', 1865, '9780323', 'Alices Adventures in Wonderland is an 1865 novel written by English author Charles Lutwidge Dodgson under the pseudonym Lewis Carroll.', 'Chapter 1'),
                #     ('One Hundred Years of Solitude', 'Gabriel García Márquez', 'Harper & Row', 1967, '978006', 'One Hundred Years of Solitude is a landmark 1967 novel by Colombian author Gabriel García Márquez.', 'Chapter 1')
                # """
                # cursor.execute(query, (book_title,))

                query = """SELECT count(*) FROM books WHERE bname = %s"""
                cursor.execute(query, (book_title,))
                res = cursor.fetchone()
                print(res[0])
                
                


    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)



if __name__ == "__main__":
    find_book("To Kill a Mockingbird")
