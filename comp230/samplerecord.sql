
-- one record
select array_to_json(array_agg(row_to_json(t)))from (select comm_code, name, sector, class, res_cnt,dwell_cnt, comm_structure, gcoord,gcenter from census2018 where name = 'SUNALTA') t

-- array of cities 
SELECT json_agg( name::TEXT ) from census2018 where class = 'Residential'
