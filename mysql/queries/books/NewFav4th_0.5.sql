CREATE DEFINER=`root`@`localhost` PROCEDURE `NewFav4th`()
BEGIN
DECLARE counter INT;
SET counter = 0;
    WHILE counter < (SELECT COUNT(id) FROM books) DO
	INSERT INTO favorites (author_id, book_id) VALUE ((SELECT id FROM authors WHERE id = (SELECT id FROM authors ORDER BY id LIMIT 3,1)), (SELECT id FROM books WHERE id = (SELECT id FROM books ORDER BY id LIMIT counter, 1)));
	SET counter = counter + 1;
    END WHILE;
END