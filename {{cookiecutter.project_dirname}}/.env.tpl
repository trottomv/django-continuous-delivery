DATABASE_URL=postgres://__USERNAME__:__PASSWORD__@__HOST__:__PORT__/__NAME__
DJANGO_ADMINS=admin,errors@{{cookiecutter.domain_url}}
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DJANGO_CONFIGURATION=Local
DJANGO_DEBUG=True
DJANGO_DEFAULT_FROM_EMAIL=info@{{cookiecutter.domain_url}}
DJANGO_SECRET_KEY=__SECRETKEY__
DJANGO_SERVER_EMAIL=server@{{cookiecutter.domain_url}}
EMAIL_URL=console:///
