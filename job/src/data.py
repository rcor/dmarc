from configparser import ConfigParser
import psycopg2
import os

def config():
    try:
        user=os.environ['USER']
        password=os.environ['PASSWORD']
        database=os.environ['DATABASE']
        host=os.environ['HOST']
        connection = psycopg2.connect(database=database,
                                user=user,
                                password=password,
                                host=host,
                                port=5432)
        return connection
    except(Exception) as error:
        print(error)
    

def save_report(report):
    try:
        connection=config()
        cursor = connection.cursor()
        query="INSERT INTO report (report_id, org_name, file_name, date_begin, date_end) VALUES('{report_id}', '{org_name}', '{file_name}', '{date_begin}', '{date_end}');".format(
            report_id=report.report_id,
            org_name=report.org_name
            file_name=report.file_name
            date_begin=report.date_begin
            date_end=report.date_end
        )
        records = cursor.execute()
    except(Exception) as error:
        print(error)
    finally:
        cursor.close()
        connection.close()

def exist_report(report_id):
    try:
        connection=config()
        cursor = connection.cursor()
        query="select report_id from report where report_id={report_id}".format(report_id=report_id)
        cursor.execute(query)
        records=cursor.fetchall()
        return True if records.count() > 0 else False
    except(Exception) as error:
        print(error)
    finally:
        cursor.close()
        connection.close()


def save_policy(report):
    try:
        connection=config()
        cursor = connection.cursor()
        query="INSERT INTO report (report_id, org_name, file_name, date_begin, date_end) VALUES('{report_id}', '{org_name}', '{file_name}', '{date_begin}', '{date_end}');".format(report_id=report.report_id,
            org_name=report.org_name
            file_name=report.file_name
            date_begin=report.date_begin
            date_end=report.date_end
        )
        records = cursor.execute()
    except(Exception) as error:
        print(error)
    finally:
        cursor.close()
        connection.close()

def save_report_info(report):
    try:
        connection=config()
        cursor = connection.cursor()
        records = cursor.execute()
    except(Exception) as error:
        print(error)
    finally:
        cursor.close()
        connection.close()
