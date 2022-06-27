 /*In SQL, a view is an alternative way of representing data that exists in one or more tables. 
Just like a real table, it contains rows and columns. The fields in a view are fields from one or more real tables in the database. 
Though views can be queried like a table, views are dynamic; only the definition of the view is stored, not the data. */

CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

/*How does the syntax of a REPLACE VIEW statement look?*/

CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

/*How does the syntax of a DROP VIEW statement look?*/

DROP VIEW view_name;



/*Procedure_Code_Example1:*/

DELIMITER //

CREATE PROCEDURE RETRIEVE_ALL()

BEGIN

    SELECT *  FROM PETSALE;


END //

DELIMITER ;


/*Procedure Example2 Code:*/

DELIMITER @
CREATE PROCEDURE UPDATE_SALEPRICE ( 
   IN Animal_ID INTEGER, IN Animal_Health VARCHAR(5) )     
BEGIN 

   IF Animal_Health = 'BAD' THEN                           
       UPDATE PETSALE
       SET SALEPRICE = SALEPRICE - (SALEPRICE * 0.25)
       WHERE ID = Animal_ID;

   ELSEIF Animal_Health = 'WORSE' THEN
       UPDATE PETSALE
       SET SALEPRICE = SALEPRICE - (SALEPRICE * 0.5)
       WHERE ID = Animal_ID;

   ELSE
       UPDATE PETSALE
       SET SALEPRICE = SALEPRICE
       WHERE ID = Animal_ID;

   END IF;                                                 

END @

DELIMITER ;


/*Retrieve Command*/


    CALL RETRIEVE_ALL;

    CALL UPDATE_SALEPRICE(1, 'BAD');       

    CALL RETRIEVE_ALL;
	
/*Another condition example:*/


    CALL RETRIEVE_ALL;

    CALL UPDATE_SALEPRICE(3, 'WORSE');     

    CALL RETRIEVE_ALL;
	
/*Droping(Deleting) Stored Procedure Example:*/


	  DROP PROCEDURE UPDATE_SALEPRICE;

      CALL UPDATE_SALEPRICE;
