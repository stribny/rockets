import os
import unittest
import tempfile
import app as rockets

class RocketsTestCase(unittest.TestCase):
    def setUp(self):
        # create database file and store handle
        self.db_file, rockets.app.config['DATABASE'] = tempfile.mkstemp()

        # set Flask testing mode
        rockets.app.testing = True

        # initialize database
        with rockets.app.app_context():
            rockets.init_db()
            self.db = rockets.get_db()

        # create testing client
        self.client = rockets.app.test_client()

    def tearDown(self):
        # delete database file
        os.close(self.db_file)
        os.unlink(rockets.app.config['DATABASE'])

    def test_email_note_can_be_submitted(self):
        test_email = 'testemail@email.com'
        test_note = 'test note'

        request = self.client.post('/submit_email', data=dict(
            e_m_a_i_l=test_email,
            note=test_note
        ), follow_redirects=True)

        select_submission = """SELECT date, note, email_address FROM submissions
            WHERE email_address = ?"""

        with rockets.app.app_context():
            self.db = rockets.get_db()
            cursor = self.db.cursor()
            cursor.execute(select_submission, (test_email,))
            row = cursor.fetchone()
            assert row["note"] == test_note

        assert 'Thank you for signing up' in str(request.data)

if __name__ == '__main__':
    unittest.main()
