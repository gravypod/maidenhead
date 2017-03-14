DELIMITER // 
CREATE FUNCTION grid2lat(gridsquare VARCHAR(6)) RETURNS FLOAT(8, 4) BEGIN
	DECLARE lat FLOAT(8, 4) DEFAULT -90;
	IF LENGTH(gridsquare) >= 2 THEN
		SET lat = lat + ((ORD(SUBSTR(gridsquare, 2, 1)) - ORD('A')) * 10);
	END IF;
	IF LENGTH(gridsquare) >= 4 THEN
		SET lat = lat + (CAST(SUBSTR(gridsquare, 4, 1) as UNSIGNED) * 1);
	END IF;
	IF LENGTH(gridsquare) >= 6 THEN
		SET lat = lat + ((ORD(SUBSTR(gridsquare, 6, 1)) - ORD('a')) * (2.5 / 60));
	END IF;

	RETURN lat;
END //

CREATE FUNCTION grid2lon(gridsquare VARCHAR(6)) RETURNS FLOAT(8, 4) BEGIN
	DECLARE lon FLOAT(8, 4) DEFAULT -180;
	IF LENGTH(gridsquare) >= 2 THEN
		SET lon = lon + ((ORD(SUBSTR(gridsquare, 1, 1)) - ORD('A')) * 20);
	END IF;
	IF LENGTH(gridsquare) >= 4 THEN
		SET lon = lon + (CAST(SUBSTR(gridsquare, 3, 1) as UNSIGNED) * 2);
	END IF;
	IF LENGTH(gridsquare) >= 6 THEN
		SET lon = lon + ((ORD(SUBSTR(gridsquare, 5, 1)) - ORD('a')) * (5   / 60));
	END IF;

	RETURN lon;
END //

CREATE PROCEDURE grid2latlon(IN gridsquare VARCHAR(6), OUT olon FLOAT(8, 4), OUT olat FLOAT(8, 4)) BEGIN
	SET olat = grid2lat(gridsquare);
	SET olon = grid2lat(gridsquare);
END //
DELIMITER ;

