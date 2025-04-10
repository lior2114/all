from app_function import Cities_function as c
from app_function import Workers_function as f
from app_function import Projects_function as p

#Cities
try:
    c.create_table()
    c.create_added_cities()
    c.search_city_id()
    
except ValueError as err:
    print(err)

except Exception as err:
    print(err)


#workers
try:
    f.workers_crate_table()
    f.workers_info()
    f.show_cities_info_in_workers()
except ValueError as err:
    print(err)

except Exception as err:
    print(err)


#projects
try:
    p.create_projects_table()
    p.insert_projects()
    p.search_project_by_id()
    p.show_projects_coast_over_10000()
    p.search_project_by_id()
    p.show_workers_names_and_projects()
    p.return_count_of_projects()
except ValueError as err:
    print(err)

except Exception as err:
    print(err)