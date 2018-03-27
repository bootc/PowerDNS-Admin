import os
basedir = os.path.abspath(os.path.dirname(__file__))


def _boolify(envvar, default=True):
    value = os.getenv(envvar)
    if not value:
        return default

    return (value.upper() == 'TRUE')


def _listify(envvar, default=[]):
    value = os.getenv(envvar)
    if not value:
        return default

    return [x.strip() for x in value.split(',')]


# BASIC APP CONFIG
WTF_CSRF_ENABLED = True
SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))
BIND_ADDRESS = '127.0.0.1'
PORT = int(os.getenv('POWERDNS_ADMIN_PORT', '9393'))
LOGIN_TITLE = os.getenv('LOGIN_TITLE', 'PDNS')

# TIMEOUT - for large zones
TIMEOUT = int(os.getenv('TIMEOUT', '10'))

# LOG CONFIG
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
LOG_FILE = ''

# Upload
UPLOAD_DIR = os.getenv('UPLOAD_DIR', os.path.join(basedir, 'upload'))

# DATABASE CONFIG
SQLA_DB_HOST = os.getenv('SQLA_DB_HOST')
SQLA_DB_USER = os.getenv('SQLA_DB_USER', 'powerdnsadmin')
SQLA_DB_PASSWORD = os.getenv('SQLA_DB_PASSWORD')

if SQLA_DB_HOST:
    # Default to MySQL if a hostname was given
    SQLA_DB_TYPE = os.getenv('SQLA_DB_TYPE', 'mysql')
    SQLA_DB_NAME = os.getenv('SQLA_DB_NAME', 'powerdnsadmin')
    SQLALCHEMY_DATABASE_URI = SQLA_DB_TYPE + '://' + SQLA_DB_USER + ':' + \
        SQLA_DB_PASSWORD + '@' + SQLA_DB_HOST + '/' + SQLA_DB_NAME
else:
    # Default to SQLite if no hostname was given
    SQLA_DB_TYPE = os.getenv('SQLA_DB_TYPE', 'sqlite')
    SQLA_DB_NAME = os.getenv('SQLA_DB_NAME', '/tmp/powerdnsadmin.db')
    SQLALCHEMY_DATABASE_URI = SQLA_DB_TYPE + ':///' + SQLA_DB_NAME

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# LDAP CONFIG
try:
    LDAP_TYPE = os.environ['LDAP_TYPE']
except KeyError:
    # Don't even set LDAP_TYPE at all if it's not in the environment
    pass

LDAP_URI = os.getenv('LDAP_URI')
LDAP_USERNAME = os.getenv('LDAP_USERNAME')
LDAP_PASSWORD = os.getenv('LDAP_PASSWORD')
LDAP_SEARCH_BASE = os.getenv('LDAP_SEARCH_BASE')

# Only used if LDAP_TYPE=ldap:
LDAP_USERNAMEFIELD = os.getenv('LDAP_USERNAMEFIELD', 'uid')
LDAP_FILTER = os.getenv('LDAP_FILTER', '(objectClass=inetorgperson)')
# When LDAP_TYPE=ad (or any other value), the following values are used:
# LDAP_USERNAMEFIELD = 'samaccountname'
# LDAP_FILTER = '(objectcategory=person)'

# Github Oauth
GITHUB_OAUTH_ENABLE = True if os.getenv('GITHUB_OAUTH_KEY') else False
GITHUB_OAUTH_KEY = os.getenv('GITHUB_OAUTH_KEY')
GITHUB_OAUTH_SECRET = os.getenv('GITHUB_OAUTH_SECRET')
GITHUB_OAUTH_SCOPE = os.getenv('GITHUB_OAUTH_SCOPE', 'email')
GITHUB_OAUTH_URL = os.getenv('GITHUB_OAUTH_URL')
GITHUB_OAUTH_TOKEN = os.getenv('GITHUB_OAUTH_TOKEN')
GITHUB_OAUTH_AUTHORIZE = os.getenv('GITHUB_OAUTH_AUTHORIZE')

# Default Auth
BASIC_ENABLED = _boolify('BASIC_ENABLED')
SIGNUP_ENABLED = _boolify('SIGNUP_ENABLED')

# POWERDNS CONFIG
PDNS_STATS_URL = os.getenv('PDNS_STATS_URL')
PDNS_API_KEY = os.getenv('PDNS_API_KEY')
PDNS_VERSION = os.getenv('PDNS_VERSION', '4.0.0')  # Assume modern by default

# RECORDS ALLOWED TO EDIT
RECORDS_ALLOW_EDIT = _listify('RECORDS_ALLOW_EDIT', [
    'A', 'AAAA', 'CNAME', 'SPF', 'PTR', 'MX', 'TXT'])

# EXPERIMENTAL FEATURES
PRETTY_IPV6_PTR = _boolify('PRETTY_IPV6_PTR', False)
