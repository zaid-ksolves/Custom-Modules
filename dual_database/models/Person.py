from odoo import models, fields, api, SUPERUSER_ID, sql_db
import contextlib
import psycopg2
import pyodbc
from sqlalchemy import create_engine ,MetaData, Table
from datetime import datetime


class Person(models.Model):
    _inherit = 'res.partner'
    _description = 'Person Information'

    name = fields.Char(string='Name')
    age = fields.Char(string='Age')
    # date_of_birth = fields.Char(string='DOB')
    # maths = fields.Integer(string='Maths')
    # chemistry = fields.Integer(string='Chemistry')
    # marks_obtained = fields.Integer(string='Obtained Marks', compute='_compute_total_marks', store=True)
    #
    # @api.onchange('date_of_birth')
    # def calculate_age(self):
    #     self.age = self.date_of_birth
    #     # today = datetime.now().date()
    #     # for record in self:
    #     #     if record.date_of_birth:
    #     #         dob = fields.Date.from_string(record.date_of_birth)
    #     #         age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    #     #         record.age = age
    #     #     else:
    #     #         record.age = 0
    #
    # @api.depends('maths', 'chemistry')
    # def _compute_total_marks(self):
    #     for record in self:
    #         total = 0
    #         subjects = ['maths', 'chemistry']
    #         for subject in subjects:
    #             marks = getattr(record, subject, '0') or '0'
    #             total += int(marks)
    #         record.marks_obtained = total

    # def create_record(self):
    #     connection = sql_db.db_connect('new_db')
    #     with contextlib.closing(connection.cursor()) as cr:
    #         cr._cnx.autocommit = True
    #         env = api.Environment(cr, SUPERUSER_ID, {})
    #         env['dual_database.person'].create({'name': self.name, 'age': self.age})

    # def create_record(self):
    #     self.env['dual_database.person'].create({'name': self.name, 'age': self.age})
    #
    #     connection = sql_db.db_connect('new_db')
    #     with contextlib.closing(connection.cursor()) as cr:
    #         cr.execute("INSERT INTO dual_database_person (name, age) VALUES (%s, %s)", (self.name, self.age))

    # def create(self, vals_list):
    #     new_db_name = 'new_db'
    #
    #     with registry(self.env.cr.dbname).cursor() as cr:
    #         env = api.Environment(cr, SUPERUSER_ID, {})
    #         new_db_model = env['dual_database.person'].sudo()
    #
    #         new_db_model.create({
    #             'name': vals_list.get('name'),
    #             'age': vals_list.get('age'),
    #         })
    #
    #     return super('dual_database.person', self).create(vals_list)





    #   PYODBC
    # def create_record(self):
    #     user = "odoo16"
    #     password = "odoo16"
    #     database = "new_db_1"
    #     host = "localhost"
    #     port = "5432"
    #     dsn = "new_db"
    #
    #     # connection_string = f"DSN={dsn};UID={user};PWD={password};DATABASE={database};SERVER={host};PORT={port}"
    #     # connection_string = pyodbc.connect(f"DRIVER={dsn};SERVER={host};DATABASE={database};UID={user};PWD={password}")
    #     # connection_string = f"DRIVER={dsn};SERVER={host};DATABASE={database};UID={user};PWD={password}"
    #     connection_string = f"DRIVER={{PostgreSQL ANSI}};SERVER={host};DATABASE={database};UID={user};PWD={password}"
    #
    #     conn = pyodbc.connect(connection_string)
    #
    #     cursor = conn.cursor()
    #     #cursor.execute("INSERT INTO dual_database_person (name, age) VALUES ('Zaid', '24')")
    #     # name = 'John'
    #     # age = '34'
    #     cursor.execute(f"INSERT INTO res_partner(name) VALUES('{self.name}')")
    #     #cursor.execute("INSERT INTO dual_database_person(name, age) VALUES( %s, %s )",('John','34'))
    #     conn.commit()
    #     conn.close()

    #   PSYCOPG
    # def create_record(self):
    #
    #     conn = psycopg2.connect(
    #         dbname="new_db_1",
    #         user="odoo16",
    #         password="odoo16",
    #         host="localhost",
    #         port="5432"
    #     )
    #
    #     cursor = conn.cursor()
    #
    #     cursor.execute("INSERT INTO res_partner (name) VALUES (%s)", (self.name))
    #
    #     conn.commit()
    #     conn.close()


    # SQLALCHEMY
    def create_record(self):
        dbname = "new_db"
        user = "odoo16"
        password = "odoo16"
        host = "localhost"
        port = "5432"

        engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")

        connection = engine.connect()

        table_name = 'res_partner'
        metadata = MetaData(bind=engine)
        res_partner = Table(table_name, metadata, autoload=True)

        data = {'name':self.name,'age':self.age}
        query = res_partner.insert().values(data)

        #query = res_partner.select().limit(5)
        #result = connection.execute(query).fetchall()
        connection.execute(query)
        