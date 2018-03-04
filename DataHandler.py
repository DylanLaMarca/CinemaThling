import sqlite3
import os.path
import datetime
from ThlingCrawler import Movie

class MovieDataBase:
    DATABASE_DIR = "Movies.db"

    @staticmethod
    def connect():
        new = not os.path.isfile(MovieDataBase.DATABASE_DIR)
        connection = sqlite3.connect(MovieDataBase.DATABASE_DIR)
        if new:
            cursor = connection.cursor()
            MovieDataBase.create_tables(cursor)
        return connection

    @staticmethod
    def disconnect( connection):
        connection.commit()
        connection.close()

    @staticmethod
    def create_tables( cursor):
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

    @staticmethod
    def add_command(cursor, title, slug, year, date):
        if slug not in MovieDataBase.get_slugs('new'):
            print 'INSERTING {} [{}] INTO new...'.format(title, slug)
            add_command = """INSERT INTO new VALUES ("{}", "{}", {}, "{}");""".format(title, slug, year, date)
            cursor.execute(add_command)
        else:
            print 'Already in new...'

    @staticmethod
    def add_to_new( movie):
        today = MovieDataBase.get_date()
        connection = MovieDataBase.connect()
        cursor = connection.cursor()
        title = movie.get('title')
        slug = movie.get('slug')
        year = movie.get('year')
        if year == None:
            year = 0000
        MovieDataBase.add_command(cursor, title, slug, year, today)
        MovieDataBase.disconnect(connection)

    @staticmethod
    def get_date():
        current = datetime.datetime.now()
        return "{}-{}-{}".format(current.year, current.month, current.day)

    @staticmethod
    def get_slugs(table):
        connection = MovieDataBase.connect();
        cursor = connection.cursor()
        command = """SELECT slug FROM {};""".format(table)
        raw_slugs = cursor.execute(command).fetchall()
        MovieDataBase.disconnect(connection)
        slugs = range(len(raw_slugs))
        for count in range(len(raw_slugs)):
            slugs[count] = raw_slugs[count][0].encode('utf-8')
        return slugs
