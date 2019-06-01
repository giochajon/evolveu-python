select comm_code, name, sector, class, res_cnt,dwell_cnt, multipolygon,comm_structure, gcoord,gcenter from census2018 where class = 'Residential'


select '{"name":' ||'""'|| name ||'", ' ||'"sector":"'|| sector ||'", ' ||'"class":"'|| class ||'", '||'"res_cnt":"'|| res_cnt ||'", '||'"dwell_cnt":"'|| dwell_cnt ||'", '||'"comm_structure":"'|| comm_structure ||'"}', gcoord,gcenter from census2018 where class = 'Residential'


select array_to_json(array_agg(row_to_json(t)))
    from (
      select comm_code, name, sector, class, res_cnt,dwell_cnt, comm_structure, gcoord,gcenter from census2018
    ) t


--cinco

  select array_to_json(array_agg(row_to_json(t)))
    from (
      select comm_code, name, sector, class, res_cnt,dwell_cnt, comm_structure, gcoord,gcenter from census2018 where class = 'Residential' order by name limit 5
    ) t
	