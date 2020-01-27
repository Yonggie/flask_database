#a function used to get database uri used for SQLalchemy

#this function need localization
def get_db_uri(database_info):
    db_type = database_info.get('db') or 'mysql'
    driver = database_info.get('driver') or 'pymysql'
    username = database_info.get('username') or 'root'
    password = database_info.get('password') or '135246'
    host = database_info.get('host') or '127.0.0.1'
    port = database_info.get('port') or '3306'
    db_name = database_info.get('dbname') or 'blog'

    return '{}+{}://{}:{}@{}:{}/{}'.format(db_type,driver,username,password,host,port,db_name)

class SimpleConfig:
    DEBUG = True
    DATABASE = {
        'db_name': 'blog'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
    TEMPLATES_AUTO_RELOAD=True
    SECRET_KEY='$%^&*()345671231adFGHJBHJK,./'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def init_app(app):
    app.config.from_object(SimpleConfig)