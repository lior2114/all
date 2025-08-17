from models.user_model import User
from models.role_model import Role
from models.country_model import Country
from models.vacation_model import Vacation
from datetime import datetime

Role.insert_default_roles()
Country.insert_default_countries()


# Create user admin if not exists
User.create_user(
    first_name="Laura",
    last_name="Admin",
    email="laura-admin@johnbryce.com",
    password="@dmin!77",
    role_id=1
)

# Create regular user if not exists
User.create_user(
    first_name="Charles",
    last_name="Kent",
    email="ckent@gmail.com",
    password="mypass!!word9",
    role_id=2
)


vacations = [
    (10, "Beach in Thailand", "2025-07-01", "2025-07-10", 1200, "thailand.jpg"),
    (2, "Cultural tour in Spain", "2025-08-05", "2025-08-15", 1500, "spain.jpg"),
    (3, "Wine tasting in France", "2025-09-01", "2025-09-08", 1800, "france.jpg"),
    (6, "Hiking in Argentina", "2025-10-10", "2025-10-20", 950, "argentina.jpg"),
    (4, "Island hopping in Greece", "2025-06-15", "2025-06-25", 2100, "greece.jpg"),
    (7, "Adventure in Brazil", "2025-11-01", "2025-11-10", 1400, "brazil.jpg"),
    (5, "Temples in Japan", "2025-07-20", "2025-07-30", 3000, "japan.jpg"),
    (1, "Relaxation in Italy", "2025-08-01", "2025-08-10", 1600, "italy.jpg"),
    (8, "Food tour in Mexico", "2025-09-15", "2025-09-25", 1000, "mexico.jpg"),
    (9, "Coastal trip in Portugal", "2025-10-01", "2025-10-12", 1100, "portugal.jpg"),
    (10, "Night markets in Thailand", "2025-12-05", "2025-12-15", 950, "thailand2.jpg"),
    (2, "Art and history in Spain", "2025-12-20", "2025-12-30", 1250, "spain2.jpg"),
]

def vacation_exists(description):
    all_vacations = Vacation.get_all()
    for v in all_vacations:
        if v["description"].lower() == description.lower():
            return True
    return False

def is_valid(start_date, end_date, price):
    today = datetime.now().date()
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return False

    if price < 0 or price > 10000:
        print(f"Invalid price: {price}")
        return False
    if end < start:
        print(f"Invalid date range: {start_date} to {end_date}")
        return False
    if start < today:
        print(f"Start date {start_date} is in the past.")
        return False

    return True

for v in vacations:
    country_id, description, start_date, end_date, price, image = v

    if vacation_exists(description):
        print(f"Vacation '{description}' already exists. Skipping.")
    elif not is_valid(start_date, end_date, price):
        print(f"Vacation '{description}' is invalid. Skipping.")
    else:
        result = Vacation.add_vacation(*v)
        print(result.get('message', result))


#     SELECT 
#     vacations.vacation_id,
#     vacations.description,
#     vacations.start_date,
#     vacations.end_date,
#     vacations.price,
#     vacations.image_filename,
#     countries.country_name
# FROM vacations
# LEFT JOIN countries ON vacations.country_id = countries.country_id;


# DELETE FROM likes;
