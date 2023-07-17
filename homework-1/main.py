"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

with psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='416286'
) as conn:
    with conn.cursor() as cur:
        sql_customers = """COPY customers(customer_id,company_name,contact_name
        )FROM '/Users/anastasia/PycharmProjects/postgres-homeworks/homework-1/north_data/customers_data.csv'
        DELIMITER ','
        CSV HEADER;"""

        sql_employees = """COPY employees(employee_id,first_name,last_name,title,birth_date,notes
        )FROM '/Users/anastasia/PycharmProjects/postgres-homeworks/homework-1/north_data/employees_data.csv'
        DELIMITER ','
        CSV HEADER;"""

        sql_orders = """COPY orders(order_id,customer_id,employee_id,order_date,ship_city
        )FROM '/Users/anastasia/PycharmProjects/postgres-homeworks/homework-1/north_data/orders_data.csv'
        DELIMITER ','
        CSV HEADER;"""

        cur.execute(sql_customers)
        cur.execute(sql_employees)
        cur.execute(sql_orders)
conn.close()
