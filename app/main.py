import psycopg2
import csv
import pandas as pd
from  data_creation import DatabaseTable
from config import config


class CmsBlogs(object):
    def __init__(self, connection, path):
        self.path = path
        self.db = connection

    def published_blogs(self):
        cur = self.db.cursor()
        query = """select * from cms.published_blogs"""
        header_list = ['Id', 'Name', 'Published_date', 'blog_Text', 'created_date']
        cur.execute(query)
        for record in cur.fetchall():
            pub_filename=self.path + record[1] + "-" + record[4].strftime(
                "%b") + "-" + "Published-blogs.csv"
            with open(pub_filename, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(record)

            df = pd.read_csv(pub_filename, sep=",")
            df.drop_duplicates(subset=None, inplace=True)
            df.to_csv(pub_filename, header=header_list, index=False)
        cur.close()

    def draft_blogs(self):
        cur = self.db.cursor()
        query = """select * from cms.draft_blogs"""
        header_list = ['Id', 'Name', 'Published_date', 'blog_Text', 'created_date']
        cur.execute(query)
        for record in cur.fetchall():
            draft_filename=self.path + record[1] + "-" + record[4].strftime(
                "%b") + "-" + "Draft-blogs.csv"
            with open(draft_filename, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(record)
            df = pd.read_csv(draft_filename, sep=",")
            df.drop_duplicates(subset=None, inplace=True)
            df.to_csv(draft_filename, header=header_list, index=False)
        cur.close()

    def close(self):
        self.db.close()


if __name__ == "__main__":
    conn = None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        conn.autocommit = True
        # create a cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    db = DatabaseTable(conn)
    print("Table created")
    db.insert_authors_blog_data()
    print("Data inserted")
    db.published_blogs_view()
    print("published view created")
    db.draft_blogs_view()
    print("Draft view created")

    db1 = CmsBlogs(conn, "/data/blog_data/")
    db1.published_blogs()
    print("Published blogs loaded to csv")
    db1.draft_blogs()
    print("Draft Blogs loaded to csv ")
    db1.close()
    print("Postgres Db connection closed")
