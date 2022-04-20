from db.run_sql import run_sql
from models.book import Book
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, author_id, year_published) VALUES (%s,%s,%s) RETURNING *"
    values = [book.title, book.author.id, book.year_published]
    results = run_sql(sql,values)
    id = results[0]['id']
    book.id =id
    return book

def select_all():
    books =[]
    sql="SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'],author,row['year_published'], row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id =%s"
    values = [id]
    results = run_sql(sql,values)

    if len(results) > 0:
        result = results[0]
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author,result['year_published'],result['id'])
        return book

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)
