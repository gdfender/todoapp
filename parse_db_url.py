# -*- encoding: utf-8 -*-

def parse_db_url(db_link):
    if 'sqlite' in db_link.split('///')[0]:
        exit = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': db_link.split('///')[1],
        }
        return exit
    elif 'postgres' in db_link.split(':')[0]:
        exit = {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': db_link.split(':')[1][2:],
            'PASSWORD': db_link.split(':')[2].split('@')[0],
            'HOST': db_link.split(':')[2].split('@')[1],
            'PORT': db_link.split(':')[-1].split('/')[0],
            'NAME': db_link.split(':')[-1].split('/')[1],
        }
        return exit
    raise ValueError('Ошибка')