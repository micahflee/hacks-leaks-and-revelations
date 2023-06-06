# Exercise 12-2: Query Your SQL Database

Following the instructions in this book, practice running SQL queries.

After creating the books and authors tables in Exercise 12-1, use INSERT statements to insert data into them with these queries:

```sql
INSERT INTO authors (name) VALUES ('Micah Lee');
INSERT INTO authors (name) VALUES ('Carl Sagan');
INSERT INTO books (title, author_id) VALUES ('Hacks, Leaks, and Revelations', 1);
INSERT INTO books (title, author_id) VALUES ('Pale Blue Dot', 2);
INSERT INTO books (title, author_id) VALUES ('Contact: A Novel', 2);
```

And try running some SELECT statements:

```sql
SELECT * FROM books;
SELECT title FROM books;
SELECT * FROM books ORDER BY title;
SELECT * from books ORDER BY title DESC;
SELECT * from books ORDER BY author_id, title;
SELECT COUNT(*) FROM books;
```

Filter results of SELECT statements with WHERE clauses:

```sql
SELECT title FROM books WHERE author_id=1;
SELECT * FROM books WHERE id >= 10 AND id < 100;
SELECT * FROM authors WHERE name='Carl Sagan';
SELECT * FROM authors WHERE name LIKE 'carl sagan';
SELECT * FROM authors WHERE name LIKE '%lee%';
SELECT * FROM authors WHERE name LIKE '% lee';
SELECT * FROM books WHERE author_id=2 AND title LIKE '%blue%';

SELECT *
FROM books
WHERE 
    author_id=2 AND 
    (
        title LIKE '%red%' OR 
        title LIKE '%green%' OR
        title LIKE '%blue%'
    );
```

Select from multiple tables at once with JOIN clauses:

```sql
SELECT
    books.title,
    authors.name
FROM books
JOIN authors ON books.author_id = authors.id;

SELECT books.title
FROM books
LEFT JOIN authors ON books.author_id = authors.id
WHERE authors.name = 'Carl Sagan';
```

Update data with UPDATE statements:

```sql
UPDATE books 
SET title='Hacks, Leaks, and Revelations: The Art of Analyzing Hacked and Leaked Data' 
WHERE id=1;
```