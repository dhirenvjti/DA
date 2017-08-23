import os

from google.appengine.api import users
from google.appengine.ext import db

ADMIN_USERS = ["jigarbhatt93@gmail.com", "dhirenvjti@gmail.com", "dhiren29p@gmail.com"]


def authenticate_user(self, target_url, email_list=None):
    if 'http://localhost' in self.request.url:
        return 'local-user'

    if not email_list:
        email_list = []

    email_list += ADMIN_USERS
    user = users.get_current_user()
    if user:
        if user.email() in email_list:
            return user.email()
        else:
            self.response.out.write(
                "{user_email} is not authorized.  Please <a href={logout_url}>Logout</a> and re-login.".format(
                    user_email=user.email(),
                    logout_url=users.create_logout_url(target_url)))
            return False

    else:
        self.response.out.write("Please <a href='{login_url}'>Login...</a>".format(
            login_url=users.create_login_url(target_url)
        ))
        return False


def fetch_gql(query_string, fetchsize=50):
    q = db.GqlQuery(query_string)
    cursor = None
    results = []
    while True:
        q.with_cursor(cursor)
        intermediate_result = q.fetch(fetchsize)
        if len(intermediate_result) == 0:
            break
        cursor = q.cursor()
        results += intermediate_result

    return results


def template(file_name, directory="templates"):
    return os.path.join(os.path.dirname(__file__), directory, file_name)
