"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os

with psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='416286'
) as conn:
    with conn.cursor() as cur:
        file = f'{os.path.dirname(os.path.realpath(__file__))}/north_data/customers_data.csv'
        sql_customers = f"""COPY customers(customer_id,company_name,contact_name
        )FROM '{file}'
        DELIMITER ','
        CSV HEADER;"""

        file = f'{os.path.dirname(os.path.realpath(__file__))}/north_data/employees_data.csv'
        sql_employees = f"""COPY employees(employee_id,first_name,last_name,title,birth_date,notes
        )FROM '{file}'
        DELIMITER ','
        CSV HEADER;"""

        file = f'{os.path.dirname(os.path.realpath(__file__))}/north_data/orders_data.csv'
        sql_orders = f"""COPY orders(order_id,customer_id,employee_id,order_date,ship_city
        )FROM '{file}'
        DELIMITER ','
        CSV HEADER;"""

        cur.execute(sql_customers)
        cur.execute(sql_employees)
        cur.execute(sql_orders)
conn.close()
