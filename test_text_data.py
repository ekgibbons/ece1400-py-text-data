import io
import contextlib
import random
import subprocess
import unittest

import numpy as np

import windanalysis
import windanalysis_sol
import moviedata
import moviedata_sol

class TestTextData(unittest.TestCase):

    def test_windanalysis_usage(self):
        result = subprocess.run(["python", "windanalysis.py"],
                            stdout=subprocess.PIPE)
        sub = result.stdout.decode("UTF-8").strip()

        sol = "Usage:\n    $ python windanalysis.py <data_file>"

        self.assertEqual(sol, sub)

    def test_windanalysis(self):
        result = subprocess.run(["python", "windanalysis.py",
                                 "KOGD.txt"],
                            stdout=subprocess.PIPE)
        sub = result.stdout.decode("UTF-8").strip()

        result = subprocess.run(["python", "windanalysis_sol.pyc",
                                 "KOGD.txt"],
                            stdout=subprocess.PIPE)
        sol = result.stdout.decode("UTF-8").strip()

        self.assertEqual(sol, sub)

    def test_moviedata_usage(self):
        result = subprocess.run(["python", "moviedata.py"],
                            stdout=subprocess.PIPE)
        sub = result.stdout.decode("UTF-8").strip()

        sol = ("Usage:\n    $ python moviedata.py <filename> "
                  "[min_ratings_threshold (default=30)]")

        self.assertEqual(sol, sub)

    def test_moviedata_default(self):
        result = subprocess.run(["python", "moviedata.py",
                                 "u.data"],
                                stdout=subprocess.PIPE)
        sub = result.stdout.decode("UTF-8").strip()
        
        result = subprocess.run(["python", "moviedata_sol.pyc",
                                 "u.data"],
                                stdout=subprocess.PIPE)
        sol = result.stdout.decode("UTF-8").strip()

        self.assertEqual(sol, sub)


    def test_moviedata_variable_min_threshold(self):
        min_thresh = np.random.randint(10,50,size=1)[0]
        
        result = subprocess.run(["python", "moviedata.py",
                                 "u.data",str(min_thresh)],
                                stdout=subprocess.PIPE)
        sub = result.stdout.decode("UTF-8").strip()
        
        result = subprocess.run(["python", "moviedata_sol.pyc",
                                 "u.data",str(min_thresh)],
                                stdout=subprocess.PIPE)
        sol = result.stdout.decode("UTF-8").strip()

        self.assertEqual(sol, sub)

        
if __name__ == '__main__':
    unittest.main()




