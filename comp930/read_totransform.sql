


/* query to create my own nhood table and modify the coordinates  */
select comm_code, name, sector, class, res_cnt, multipolygon from census2018


/* query with emstation with converted coordinates for google */

select emstations.name, emstations.address, census2018.sector, '{lat:' || emstations.latitude || ', lng: ' || emstations.longitude || '}' as coord  
from emstations
inner join census2018 on emstations.comm_code = census2018.comm_code 


/* query with firestations  with converted coordinates for google */
select name,address, point, '{lat:' || rtrim(substring("point" from position(' ' in substring("point" from 8 for 34)) for 25),')') || ', lng:' || substring("point" from 8 for 17) || '}' as coord from firestations

