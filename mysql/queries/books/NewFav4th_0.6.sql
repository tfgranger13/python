CREATE DEFINER=`root`@`localhost` PROCEDURE `NewFav4th`()
BEGIN
DECLARE counter INT;
DECLARE max INT;
SET counter = 0;
SET max = (SELECT COUNT(id) FROM books);

    WHILE counter < max DO
	INSERT INTO favorites (author_id, book_id) VALUE ((SELECT id FROM authors WHERE id = (SELECT id FROM authors ORDER BY id LIMIT 3,1)), (SELECT id FROM books WHERE id = (SELECT id FROM books ORDER BY id LIMIT counter, 1)));
	SET counter = counter + 1;
    END WHILE;
END