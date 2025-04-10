from cities import Cities as c
from workers import Workers as w 
from projects import Projects as p

#Cities
try:
    class Cities_function:
        #א
        def create_table():
            answer = input("want to create cities table y/n?")
            if answer == 'n':
                print("not creating")
                pass
            elif answer == 'y':
                c.create_city_table()
            else:
                raise ValueError ("only y / n ")
        #ב
        def create_added_cities():
            answer = input("do you want to create the cities you add y/n?")
            if answer == 'n':
                print("not creating")
                pass
            elif answer == 'y':
                    lis = [
                    ('Tel-Aviv',),
                    ('Ranana',),
                    ('Tel-Mond',)
                    ]
                    c.insert_cities(lis)
            else:
                raise ValueError ("only y / n ")
        #ג
        def search_city_id():
            answer = input("want to search cities by city_id y/n?")
            if answer == 'n':
                print("not creating")
                pass
            elif answer == 'y':
                city_search = int(input("enter the city id you want to search: "))
                if not isinstance(city_search, int):
                    raise ValueError("enter only number!")
                result = c.search_for_city_by_id(city_search)
                if not result:
                    raise ValueError("city_id not in table")
                print(result)
            else:
                raise ValueError ("only y / n ")
except ValueError as err:
    print(err)
except Exception as err:
    print(err)
    
#workers
try:
    class Workers_function:
    #א
        def workers_crate_table():
            answer = input("want to create workers table? y/n")
            if answer == 'y':
                w.create_workers_table()
            elif answer == 'n':
                pass
            else:
                raise ValueError("enter only y/n")
        #ב
        def workers_info():
            answer = input("want to add your list to the table? y/n")
            if answer == 'y':
                lis = [
                ('q1','w1',40000,1),
                ('q2','w2',30000,2),
                ('q3','w3',20000,3)
                ]
                w.insert_workers_lis(lis)
            elif answer == 'n':
                pass
            else:
                raise ValueError ("in info enter only y/n")
        #ג
        def show_cities_info_in_workers():
            answer = input("Want to know where all your workers live? y/n")
            if answer == 'y':
                w.show_cities_names_on_workers()
            elif answer == 'n':
                pass
            else:
                raise ValueError ("in cities info enter only y/n")
except ValueError as err:
    print(err)
except Exception as err:
    print(err)

#projects
try:
    class Projects_function:
        def create_projects_table():
            answer = input("want to create project_table? y/n")
            if answer == 'y':
                p.create_project_table()
            elif answer == 'n':
                pass
            else: 
                raise ValueError("enter only y/n on create_projects_table")
        #ב
        def insert_projects():
            answer = input("want to insert projects to the table? y/n")
            if answer == 'y':
                lis = [
                    ('Tel-Aviv-towers',50000),
                    ('Ranana-towers',40000),
                    ('Tel-Mond-towers',30000)
                ]
                p.insert_projects(lis)
            elif answer == 'n':
                pass
            else:
             raise ValueError("enter only y/n on insert_projects")
        
        #ג
        def search_project_by_id():
            answer = input("want to search workers and they projects by workers id? y/n")
            if answer == 'y':
                project_search = int(input("enter the workers id: "))
                if not isinstance(project_search, int):
                    raise ValueError("enter only number!")
                result = p.show_workers_names_and_projects_by_id(project_search)
                if not result:
                    raise ValueError("project_id not in table")
                print(result)
            elif answer == 'n':
                pass
            else:
                raise ValueError("enter only y/n on search_project_by_id")
        #ד
        def show_projects_coast_over_10000():
            answer = input("Do you want to see projects with a cost over 10,000? y/n")
            if answer == 'y':
                result = p.projects_over_10000()
                if not result:
                    print("No projects found with a cost over 10,000.")
                else:
                    print(result)
            elif answer == 'n':
                pass
            else:
                raise ValueError("Enter only y/n on show_projects_coast_over_10000")
        #v
        def delete_projects_by_budget():
            answer = input("Do you want to delete projects by budget? y/n")
            if answer == 'y':
                budget = int(input("Enter the budget threshold: "))
                if not isinstance(budget, int):
                    raise ValueError("Enter only a number!")
                if not p.delete_projects_by_budget(budget):
                    raise ValueError(f"No projects found with a budget below {budget}.")
                p.delete_projects_by_budget(budget)
                print(f"Projects with a budget below {budget} have been deleted.")
            elif answer == 'n':
                pass
            else:
                raise ValueError("Enter only y/n on delete_projects_by_budget")
            
        #u
        def show_workers_names_and_projects():
            answer = input("Want to see workers and their info along with their projects? y/n")
            if answer == 'y':
                p.show_workers_names_and_projects()
            elif answer == 'n':
                pass
            else:
                raise ValueError("Enter only y/n on show_workers_names_and_projects")
        
        #ז
        def return_count_of_projects():
            answer = input("want to know how many projects you have? y/n")
            if answer == 'y':
                p.return_count_of_projects()
            elif answer == 'n':
                pass
            else: 
                raise ValueError ("enter only y/n on return_count_of_projects")

except ValueError as err:
    print(err)
except Exception as err:
    print(err)