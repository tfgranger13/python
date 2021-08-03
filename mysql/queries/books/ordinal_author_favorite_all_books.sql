CREATE PROCEDURE ordinal_author_favorite_all_books (
	auth INT
)
BEGIN
DECLARE counter INT;
DECLARE auth_subtract INT;
SET counter = 0;
SET auth_subtract = auth -1;
    WHILE counter < (SELECT COUNT(id) FROM books) DO
	INSERT INTO favorites (author_id, book_id) VALUE ((SELECT id FROM authors WHERE id = (SELECT id FROM authors ORDER BY id LIMIT auth_subtract, 1)), (SELECT id FROM books WHERE id = (SELECT id FROM books ORDER BY id LIMIT counter, 1)));
	SET counter = counter + 1;
    END WHILE;
END
