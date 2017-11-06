import sqlite3

db_name = 'students_info.db'

# connectivity database
def run_query(query, parameters=()):
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        query_re = c.execute(query, parameters)
        conn.commit()
    # print(query_re)
    return query_re

#create table into database
def create_table():
    query = 'CREATE TABLE students_info(Name text, Roll integer,Reg integer, Course text, Address text, DOB text, PRIMARY KEY(Reg))'
    run_query(query)

#for creating table
create_table()

