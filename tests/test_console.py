import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            output_str = output.getvalue().strip()
            self.assertTrue(output_str != "")
            self.assertIsInstance(BaseModel().to_dict(), dict)
            self.assertTrue(output_str in BaseModel().to_dict().values())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(obj_id))
            output_str = output.getvalue().strip()
            self.assertTrue(output_str != "")
            self.assertIsInstance(BaseModel().to_dict(), dict)
            self.assertTrue(output_str in BaseModel().to_dict().values())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            self.assertEqual(output.getvalue().strip(), "")
            self.assertFalse(obj_id in BaseModel().to_dict().values())

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("all")
            output_str = output.getvalue().strip()
            self.assertTrue(output_str != "")
            self.assertTrue("BaseModel" in output_str)
            self.assertTrue("User" in output_str)

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("count BaseModel")
            self.assertEqual(output.getvalue().strip(), "2")
            self.console.onecmd("count User")
            self.assertEqual(output.getvalue().strip(), "1")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
            self.console.onecmd("update BaseModel {} first_name 'John'".format(obj_id))
            self.assertEqual(output.getvalue().strip(), "")
            self.assertEqual(BaseModel().to_dict()[obj_id]['first_name'], 'John')

    def test_batch_update(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            obj_id = output.getvalue().strip()
            self.console.onecmd("batch_update BaseModel {} first_name='John' last_name='Doe'".format(obj_id))
            self.assertEqual(output.getvalue().strip(), "")
            self.assertEqual(BaseModel().to_dict()[obj_id]['first_name'], 'John')
            self.assertEqual(BaseModel().to_dict()[obj_id]['last_name'], 'Doe')

    def test_batch_delete(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("create User")
            self.console.onecmd("batch_delete User")
            self.assertEqual(output.getvalue().strip(), "")
            self.assertTrue("User" not in BaseModel().to_dict().values())

    def test_batch_count(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("batch_count BaseModel User")
            self.assertEqual(output.getvalue().strip(), "BaseModel: 2\nUser: 1")

    def test_batch_show(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("batch_show BaseModel")
            output_str = output.getvalue().strip()
            self.assertTrue(output_str != "")
            self.assertTrue("BaseModel" in output_str)
            self.assertTrue("User" not in output_str)

    def test_search(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create User")
            self.console.onecmd("search User email 'test@example.com'")
            self.assertEqual(output.getvalue().strip(), "")

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("help create")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help show")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help destroy")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help all")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help count")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help update")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help batch_update")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help batch_delete")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help batch_count")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help batch_show")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help search")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help help")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help quit")
            self.assertTrue(output.getvalue().strip() != "")
            output.seek(0)
            output.truncate()
            self.console.onecmd("help EOF")
            self.assertTrue(output.getvalue().strip() != "")

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as output:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(output.getvalue().strip(), "")


if __name__ == "__main__":
    unittest.main()

