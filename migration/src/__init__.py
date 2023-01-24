from yoyo import read_migrations, get_backend
import os

if __name__ == '__init__':
    user=os.environ['USER']
    password=os.environ['PASSWORD']
    database=os.environ['DATABASE']
    host=os.environ['HOST']
    backend = get_backend(f'postgres://{user}:{password}@{host}/{database}')
    migrations = read_migrations('./migrations')
    backend.apply_migrations(backend.to_apply(migrations))
    
