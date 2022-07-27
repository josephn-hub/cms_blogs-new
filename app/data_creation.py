import psycopg2
import csv
from config import config


class DatabaseTable(object):
    def __init__(self, connection):  # Initialise server with database connection
        self.db = connection
        cursor = self.db.cursor()
        """ Drop table  """
        droptablesql = "DROP TABLE IF EXISTS cms.blogs cascade;"
        cursor.execute(droptablesql)
        # commit the changes to the database
        # conn.commit()
        # close communication with the database
        """ create tables in the PostgreSQL database"""
        createtablequery = """
            CREATE TABLE IF NOT EXISTS cms.blogs (
            id  integer,
            author varchar(20),
            published_on date default null,
            blog_text text,
            created_on timestamp
            );
            """
        cursor.execute(createtablequery)
        # close communication with the PostgreSQL database server

    def insert_authors_blog_data(self):
        cursor = self.db.cursor()
        with open('app/insert_data.csv','r') as f:
            reader= csv.reader(f)
            next(f)
            for row in reader:
                # """ insert author blog data to the table  """
                cursor.copy_from(f, 'cms.blogs', sep=',', null="")
        # commit the changes to the databas
        # close communication with the database
                cursor.close()

    def published_blogs_view(self):
        cursor = self.db.cursor()
        pub_query = """CREATE OR REPLACE VIEW  cms.published_blogs 
                    as select id,author,published_on,blog_text,created_on from cms.blogs where published_on
                    is not null;
                    """
        cursor.execute(pub_query)
        # close communication with the PostgreSQL database server
        cursor.close()       
    
    def draft_blogs_view(self):
        cursor = self.db.cursor()
        draft_query ="""CREATE OR REPLACE VIEW cms.draft_blogs as select id,author, published_on,blog_text,created_on  
        from cms.blogs where published_on is null;
        """
        cursor.execute(draft_query)
        cursor.close()

