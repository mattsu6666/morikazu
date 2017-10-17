import pymysql.cursors
import configparser


def find_all():
    config = configparser.ConfigParser()
    config.read('common.ini')
    # Connect to the database
    connection = pymysql.connect(host=config['guile_master_db']['host'],
                                 user=config['guile_master_db']['user'],
                                 password=config['guile_master_db']['pass'],
                                 db=config['guile_master_db']['db'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT id, campaign_id, ad_id, target_param, threshold FROM threshold_settings WHERE status='active'"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()


def update_to_inactive(target_id):
    config = configparser.ConfigParser()
    config.read('common.ini')
    # Connect to the database
    connection = pymysql.connect(host=config['guile_master_db']['host'],
                                 user=config['guile_master_db']['user'],
                                 password=config['guile_master_db']['pass'],
                                 db=config['guile_master_db']['db'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = f"UPDATE threshold_settings SET status = 'inactive' WHERE id = {target_id}"
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()
