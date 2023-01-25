from yoyo import read_migrations, get_backend
import os

if __name__ == '__main__':
    user=os.environ['USER']
    password=os.environ['PASSWORD']
    database=os.environ['DATABASE']
    host=os.environ['HOST']
    db_connection='postgres://{user}:{password}@{host}/{database}'.format(user=user,password=password,host=host,database=database)
    print(user)
    print(host)
    print(db_connection)
    backend = get_backend(db_connection)
    migrations = read_migrations('./migrations')
    print("run migrations")
    backend.apply_migrations(backend.to_apply(migrations))
    print("end migrations")
    
