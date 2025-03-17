import sys
import pikepdf

def unlock_pdf(input_pdf, output_pdf, password):
    try:
        pdf = pikepdf.open(input_pdf, password=password)
        pdf.save(output_pdf)
        print(f"✅ PDF ปลดล็อกสำเร็จ! บันทึกที่: {output_pdf}")
    except pikepdf._qpdf.PasswordError:
        print("❌ รหัสผ่านไม่ถูกต้อง")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("⚠️ ใช้งาน: python unlock_pdf.py <input.pdf> <output.pdf> <password>")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    password = sys.argv[3]
    
    unlock_pdf(input_pdf, output_pdf, password)
