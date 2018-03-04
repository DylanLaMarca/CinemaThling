import sqlite3
import os.path
import datetime
from ThlingCrawler import Movie

class MovieDataBase:
    DATABASE_DIR = "Movies.db"

    def __init__(self):
        connection = self.connect()
        self.disconnect(connection)

    def connect(self):
        new = not os.path.isfile(self.DATABASE_DIR)
        connection = sqlite3.connect(self.DATABASE_DIR)
        if new:
            cursor = connection.cursor()
            self.create_tables(cursor)
        return connection

    def disconnect(self, connection):
        connection.commit()
        connection.close()

    def create_tables(self, cursor):
        new_table = """
            CREATE TABLE new ( 
            title VARCHAR(50), 
            slug VARCHAR(60) PRIMARY KEY, 
            year YEAR,
            added DATE);
        """
        cursor.execute(new_table)
        pending_table = """
                CREATE TABLE pending ( 
                title VARCHAR(50), 
                slug VARCHAR(60) PRIMARY KEY, 
                made YEAR,
                added DATE,
                pended DATE);
            """
        cursor.execute(pending_table)
        downloaded_table = """
            CREATE TABLE downloaded ( 
            title VARCHAR(50), 
            slug VARCHAR(60) PRIMARY KEY, 
            made YEAR,
            added DATE,
            pended DATE,
            downloaded DATE);
        """
        cursor.execute(downloaded_table)

    def add_command(self,cursor, title, slug, year, date):
        if slug not in self.get_slugs('new'):
            print 'INSERTING {} [{}] INTO new...'.format(title, slug)
            add_command = """INSERT INTO new VALUES ("{}", "{}", {}, "{}");""".format(title, slug, year, date)
            cursor.execute(add_command)
        else:
            print 'Already in new...'

    def add_to_new(self, movie):
        today = self.get_date()
        connection = self.connect()
        cursor = connection.cursor()
        title = movie.get('title')
        slug = movie.get('slug')
        year = movie.get('year')
        if year == None:
            year = 0000
        self.add_command(cursor, title, slug, year, today)
        self.disconnect(connection)

    def get_date(self):
        current = datetime.datetime.now()
        return "{}-{}-{}".format(current.year, current.month, current.day)

    def get_slugs(self, table):
        connection = self.connect();
        cursor = connection.cursor()
        command = """SELECT slug FROM {};""".format(table)
        raw_slugs = cursor.execute(command).fetchall()
        self.disconnect(connection)
        slugs = range(len(raw_slugs))
        for count in range(len(raw_slugs)):
            slugs[count] = raw_slugs[count][0].encode('utf-8')
        return slugs
