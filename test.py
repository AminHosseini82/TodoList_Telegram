from pypdf import PdfReader, PdfWriter


def add_password_to_pdf(input_pdf_path, output_pdf_path, password):
    """
    This function reads a PDF, adds a password to it, and saves it as a new file.
    """
    try:
        # ۱. خواندن فایل PDF اصلی
        reader = PdfReader(input_pdf_path)
        writer = PdfWriter()

        # ۲. کپی کردن تمام صفحات از فایل اصلی به فایل جدید
        for page in reader.pages:
            writer.add_page(page)

        # ۳. اضافه کردن رمز عبور به فایل جدید
        # می‌توانید رمز فقط برای کاربر (user_password) یا برای مالک (owner_password) هم تعیین کنید
        writer.encrypt(password)

        # ۴. ذخیره کردن فایل PDF رمزگذاری شده جدید
        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)

        print(f"فایل '{output_pdf_path}' با موفقیت رمزگذاری و ذخیره شد. ✅")

    except Exception as e:
        print(f"خطایی رخ داد: {e} ❌")


# --- اجرای تابع ---
# مسیر فایل PDF اصلی شما
input_pdf = "original.pdf"
# مسیری که می‌خواهید فایل رمزدار در آن ذخیره شود
output_pdf = "protected.pdf"
# رمز عبور مورد نظر
my_password = "my-secret-password-123"

# فراخوانی تابع برای انجام کار
add_password_to_pdf(input_pdf, output_pdf, my_password)