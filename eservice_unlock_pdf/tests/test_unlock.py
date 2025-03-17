import os
import unittest
from eservice_unlock_pdf.unlock import unlock_pdf

class TestUnlockPDF(unittest.TestCase):
    def setUp(self):
        """กำหนด path ให้แน่นอน"""
        self.input_pdf = os.path.abspath("files/simple.pdf")  # ✅ ใช้ absolute path
        self.output_pdf = os.path.abspath("outputs/simple-unlocked.pdf")

    def test_unlock_pdf(self):
        """ทดสอบการปลดล็อก PDF ด้วยรหัสผ่านที่ถูกต้อง"""
        result = unlock_pdf(self.input_pdf, self.output_pdf, "123456789A")  
        self.assertTrue(result)

    def test_wrong_password(self):
        """ทดสอบกรณีใส่รหัสผิด ต้องคืนค่า False"""
        result = unlock_pdf(self.input_pdf, self.output_pdf, "wrongpassword")  
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()