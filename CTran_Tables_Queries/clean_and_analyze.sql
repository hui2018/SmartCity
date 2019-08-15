select location_id, stop_name, B.stop_lon, B.stop_lat, count(ctran_2019.location_id) as total, B.greater_98, AVG(location_distance) as average_distance, 
B.greater_98/count(location_id) as pct_error
from ctran_2019
	left join(
		select location_id as loc_id, stop_name, stop_lon, stop_lat, count(location_id) as greater_98
		from(
			select * 
			from ctran_2019
			left join stops_janapr_2019
			on (location_id = stops_janapr_2019.stop_code) 
		)as A
		where location_distance > 98
        and x_coordinate != 0
		and y_coordinate != 0
		and schedule_status != 0
		and schedule_status != 1
		and schedule_status != 3
		and location_id != 106
		and location_id != 110
		and location_id != 111
		and location_id != 6137
		and location_id != 0
		group by loc_id, stop_name, stop_lon, stop_lat) as B
	on location_id = B.loc_id
where x_coordinate != 0
and y_coordinate != 0
and schedule_status != 0
and schedule_status != 1
and schedule_status != 3
and location_id != 106
and location_id != 110
and location_id != 111
and location_id != 6137
and location_id != 0
group by location_id, B.stop_name, B.stop_lon, B.stop_lat, B.greater_98
order by pct_error desc
