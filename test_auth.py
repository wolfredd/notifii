import unittest

from website import auth

from website import db

from main import app

from website.models import Note

from datetime import date

class TestAuth(unittest.TestCase):

    # def setUpClass():
    #     print("Set Up")
    

    # def setUp(self):
    #     self.note1 = Note(50, "df", date.today(), 50)



    #Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response =  tester.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code , 200)

    
    #Ensure that the Log In page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response =  tester.get('/login', content_type = 'html/text')
        self.assertTrue(b"Please Login" in response.data)

    #Ensure that the Sign Up page loads correctly
    def test_sign_up_page_loads(self):
        tester = app.test_client(self)
        response =  tester.get('/sign-up', content_type = 'html/text')
        self.assertTrue(b"Please Sign Up" in response.data)

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertIn(b'You Need To Log In First', response.data)

    
    # def test_login(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/login')
    #     self.assertEqual(response.status_code, 200)
    #     response = tester.post('/login',
    #                             data = {'email':'admin', 'password':'cat'},
    #                             follow_redirects = True)
    #     self.assertEqual(response.status_code, 200)

    
    # def test_signup_works(self):
    #     tester = app.test_client(self)
    #     response = tester.post('auth.login()',
    #     data = {
    #             "email" : "admin@admin",
    #             "password" : "adminadmin"},
    #         follow_redirects=True
    #     )
    #     self.assertEqual(result,  redirect(url_for('auth.login')))

    

    # # Ensure that posts show up on the main page
    # def test_posts_show_up_on_main_page(self):
    #     tester = app.test_client(self)
    #     response = tester.post(
    #         '/login',
    #        data = {
    #             "email" : "admin@admin",
    #             "password" : "adminadmin"},
    #         follow_redirects=True
    #     )
    #     self.assertIn(render_template("login.html", user=current_user), response)
    #     #Account created!


    
    # #Ensure that the Log In page behaves correctly with correct credentials
    # def test_correct_login(self):
    #     tester = app.test_client(self)
    #     response =  tester.get('/login', 
    #     data = dict(
    #         username = "qwer@qwer", password = "zxcvbnm"
    #     ),
    #     follow_redirects = True
    #     )
    #     self.assertIn(b"Logged in successfully!", response.data)

    # response = tester.post('/login',data=dict(Email="admiin", Password="admin"),follow_redirects=True)


    # def test_posts(self):
    #     tester = app.test_client(self)
    #     response = tester.post(
    #         '/login',
    #         data=dict(Email="admiin", Password="admin"),
    #         follow_redirects=True
    #     )
    #     self.assertIn(b'success', response.data)





    # def test_login(self):
    #     tester = app.test_client(self)
    #     response = tester.post(
    #         '/login', data = {
    #             "email" : "user@example.com",
    #             "password" : "asdfghjkl"}   )
    #     self.assertEqual(response.status_code , 200)


    # def test_signup(self):
    #     tester = app.test_client(self)
    #     response = tester.post(
    #         '/sign-up', data = {
    #             "email" : "qwer@qwer",
    #             "first_name": "lopol",
    #             "password1" : "zxcvbnm",
    #             "password2" : "zxcvbnm"}   )
    #     self.assertEqual(response.status_code , 200)

    
    # def test_newNote(self):
    #     tester = app.test_client(self)
    #     response = tester.post(
    #         '/', data = {
    #             "note" : "I am a boy",
    #             }   )
    #     self.assertEqual(response.status_code , 302)


if __name__ =='__main__':
    unittest.main()