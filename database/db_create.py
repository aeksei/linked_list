from database.db import DBConnection

db = DBConnection('users.db')

with db as cursor:
    # CREATE A DB WITH TABLES
    sqlite_create_users_table = '''CREATE TABLE users_table (
                            tg_id INTEGER PRIMARY KEY,
                            state INTEGER NOT NULL,
                            editing_stage INTEGER NOT NULL,
                            name TEXT NOT NULL,
                            age INTEGER NOT NULL,
                            email TEXT NOT NULL,
                            paid INTEGER NOT NULL,
                            phone INTEGER NOT NULL
                            );'''
    sqlite_create_tasks_table = '''CREATE TABLE tasks_table (
                            tg_id INTEGER PRIMARY KEY,
                            edu_day INTEGER NOT NULL,
                            days_completed INTEGER NOT NULL,
                            task_id INTEGER NOT NULL,
                            clarification INTEGER NOT NULL,
                            feedback_day INTEGER NOT NULL,
                            day_1_task_1 INTEGER NOT NULL,
                            day_1_task_2 INTEGER NOT NULL,
                            day_1_task_3 INTEGER NOT NULL,
                            day_1_task_4 INTEGER NOT NULL,
                            day_1_task_5 INTEGER NOT NULL,
                            day_2_task_1 INTEGER NOT NULL,
                            day_2_task_2 INTEGER NOT NULL,
                            day_2_task_3 INTEGER NOT NULL,
                            day_2_task_4 INTEGER NOT NULL,
                            day_2_task_5 INTEGER NOT NULL,
                            day_3_task_1 INTEGER NOT NULL,
                            day_3_task_2 INTEGER NOT NULL,
                            day_3_task_3 INTEGER NOT NULL,
                            day_3_task_4 INTEGER NOT NULL,
                            day_3_task_5 INTEGER NOT NULL,
                            day_4_task_1 INTEGER NOT NULL,
                            day_4_task_2 INTEGER NOT NULL,
                            day_4_task_3 INTEGER NOT NULL,
                            day_4_task_4 INTEGER NOT NULL,
                            day_4_task_5 INTEGER NOT NULL,
                            day_5_task_1 INTEGER NOT NULL,
                            day_5_task_2 INTEGER NOT NULL,
                            day_5_task_3 INTEGER NOT NULL,
                            day_5_task_4 INTEGER NOT NULL,
                            day_5_task_5 INTEGER NOT NULL,
                            day_6_task_1 INTEGER NOT NULL,
                            day_6_task_2 INTEGER NOT NULL,
                            day_6_task_3 INTEGER NOT NULL,
                            day_6_task_4 INTEGER NOT NULL,
                            day_6_task_5 INTEGER NOT NULL,
                            day_7_task_1 INTEGER NOT NULL,
                            day_7_task_2 INTEGER NOT NULL,
                            day_7_task_3 INTEGER NOT NULL,
                            day_7_task_4 INTEGER NOT NULL,
                            day_7_task_5 INTEGER NOT NULL
                            );'''


    cursor.execute(sqlite_create_users_table)
    cursor.execute(sqlite_create_tasks_table)
    print("SQLite tables created")
