from eve import Eve
# from eve.auth import BasicAuth
#
#
# class Authenticate(BasicAuth):
#     def check_auth(self, username, password, allowed_roles, resource,
#                    method):
#         if resource == 'user' and method == 'GET':
#             user = app.data.driver.db['user']
#             user = user.find_one({'username': username,'password':password})
#             if user:
#                 return True
#             else:
#                 return False
#         elif resource == 'user' and method == 'POST':
#             return username == 'admin' and password == 'admin'
#         else:
#             return True

#app = Eve(auth=Authenticate)

app = Eve()

if __name__ == '__main__':
    app.run()

