import unittest
from web import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING']=True
        app.config['DEBUG']=False
        self.app=app.test_client()

        def tearDown(self):
            pass
        def test_root(self):
            response=self.app.get('/',follow_redirects=True)
            self.assertEqual(response.status_code,200)
        
        def test_api_model(self):
            tester=app.test_cliet(self)
            response=tester.post('/api/model',data=dic(),follow_redirects=True)
            self.assertEqual(response.status_code,200)

        def test_api_model(self):
            tester=app.test_cliet(self)
            response=tester.post(
                '/api/model/model_id',data=dict(user_name="hi",category_no="1"),
                follow_redirects=True
            )
            self.assertIn(b"success update",response.data)



if __name__=="__main__":
    unittest.main()
