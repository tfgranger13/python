CREATE DEFINER=`root`@`localhost` PROCEDURE `NewFav4th`()
BEGIN
DECLARE counter INT DEFAULT 0;
    WHILE counter <= COUNT(books) DO
	INSERT INTO favorites (author_id, book_id) VALUE ((SELECT id FROM authors WHERE id = (SELECT id FROM authors ORDER BY id LIMIT 3,1)), (SELECT id FROM books WHERE id = (SELECT id FROM books ORDER BY id LIMIT counter, 1)));
	SET counter = counter + 1;
    END WHILE;
END