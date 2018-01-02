import unittest
import os
import HTMLTestRunner
import trello_signUp
import trello_board
from trello_config import log

class MainTestRunner(unittest.TestCase):

    trello_test = unittest.TestSuite()
    trello_test.addTests([
        # unittest.defaultTestLoader.loadTestsFromTestCase(login.Login),
        # unittest.defaultTestLoader.loadTestsFromTestCase(trello_signUp.SignUp),
         unittest.defaultTestLoader.loadTestsFromTestCase(trello_board.Board),

    ])

    outfile = open(os.getcwd() + "/TrelloReport.html", "w")

    runner1 = HTMLTestRunner.HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Trello Tests Report'
    )

    runner1.run(trello_test)


if __name__ == '__main__':
    unittest.main()
