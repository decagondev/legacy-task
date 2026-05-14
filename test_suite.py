import unittestimport jsonfrom app import appfrom database import init_db
class LegacyAppTestCase(unittest.TestCase):
    def setUp(self):
        init_db()
        self.client = app.test_client()

    def test_search_baseline(self):
        response = self.client.get('/tickets/search?q=loginn')
        data = json.loads(response.data.decode('utf-8'))

        self.assertTrue(len(data) > 0, "Search failed to surface relevant result for query with typo.")
        self.assertEqual(data[0]['id'], 1)

    def test_automated_triage(self):
        payload = {"id": 2, "category": "Auto-Detect"} 
        response = self.client.post('/tickets/triage', data=json.dumps(payload), content_type='application/json')
        
        self.assertEqual(response.status_code, 200)

        check = self.client.get('/tickets/search?q=refund')
        check_data = json.loads(check.data.decode('utf-8'))
        self.assertEqual(check_data[0]['category'], 'Billing', "Automated categorization pipeline failed.")

    def test_data_normalization_schema(self):
        payload = {"description": "i cant login help my email is john_doe@gmail.com"}
        response = self.client.post('/tickets/extract', data=json.dumps(payload), content_type='application/json')
        data = json.loads(response.data.decode('utf-8'))

        self.assertIn("extracted_email", data)
        self.assertEqual(data["extracted_email"], "john_doe@gmail.com")
if __name__ == '__main__':
    unittest.main()
