from runstats import Statistics
import unittest
import flask_testing
import sys
sys.path.append("../..")
from app import app



class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        # Test app instance tearDown Steps 
        pass

    def test_health(self):
        resp = self.app.get('/ping')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_data(as_text=True), "pong")
        print "--- Health Status Check Successful ---"

    def test_encryptdecrypt(self):
        test_num = 9.0
        resp = self.app.post('/api/pushrecalculateandencrypt', data=str(test_num))
        self.assertEqual(resp.status_code, 200)
        resp = self.app.post('/api/decrypt', data=resp.get_data(as_text=True))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_data(as_text=True).encode('ascii'), str(float(test_num)))
        print " --- Encrypt Decrypt Methods Validation Successful ---"
    
    def test_pushandrecalculate(self):
        rstat = Statistics()
        resp = self.app.get('/api/reset')
        self.assertEqual(resp.status_code, 200)
        test_array = [4,7,6,9,1]
        for i in test_array:
            resp = self.app.post(
                '/api/pushandrecalculate', data=str(i))
        print resp.get_data(as_text=True)
        avg = 0
        for i in test_array:
            avg = avg+i
        avg = float(avg)/float(len(test_array))
        self.assertEqual(resp.get_data(as_text=True).split(
            "{")[1].split(",")[0].encode('ascii'), str(avg))
        for i in test_array:
            rstat.push(i)
        self.assertEqual(str(rstat.stddev(ddof=0)), resp.get_data(as_text=True).split(
            "}")[0].split(",")[-1].encode('ascii'))
        print "--- Push and Recalculate Statistics Validation Successful ---"

if __name__ == '__main__':
    unittest.main()
    
