import json
import pymysql

endpoint = 'endpoint_da_instancia_rds'
username = 'seu_user'
password = 'sua_senha_forte'
database_name = 'nome_do_db'

connection = pymysql.connect(host=endpoint, user=username, password=password, db=database_name)

def lambda_handler(event, context):
    
    cursor = connection.cursor()
    cursor.execute('SELECT user.id, user.email, user.username, role.id AS role_id, role.name AS role_name FROM user JOIN user_roles on (user.id=user_roles.user_id) JOIN role on (role.id=user_roles.role_id)')
    
    rows = cursor.fetchall()
    
    return {
        'statusCode': 200,
        'body': json.dumps(rows)
    }
