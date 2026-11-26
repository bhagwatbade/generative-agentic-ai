from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

filename = "company_policy.pdf"

policies = [
    ("Casual Leave Policy",
     "Employees are eligible for 12 casual leaves per calendar "
     "year. Casual leave requires manager approval."),
    ("Sick Leave Policy",
     "Employees are eligible for 10 sick leaves per calendar "
     "year. A medical certificate is required for sick leave "
     "exceeding three consecutive days."),
    ("Notice Period Policy",
     "Employees must serve a notice period of 60 calendar "
     "days after submitting their resignation."),
    ("Working Hours Policy",
     "Normal office working hours are from 9:00 AM to "
     "6:00 PM, Monday to Friday."),
    ("Work From Home Policy",
     "Employees may work from home only after receiving "
     "approval from their reporting manager."),
    ("Medical Insurance Policy",
     "The company provides medical insurance coverage of "
     "INR 5 lakh per employee."),
    ("Probation Period Policy",
     "New employees must complete a probation period "
     "of six months."),
    ("Annual Leave Policy",
     "Employees are eligible for 18 days of annual leave "
     "per calendar year.")
]

styles = getSampleStyleSheet()
document = SimpleDocTemplate(filename, pagesize=A4)
story = [Paragraph("ABC TECHNOLOGIES - EMPLOYEE POLICY",
                   styles["Title"]), Spacer(1, 20)]

for title, description in policies:
    story.append(Paragraph(title, styles["Heading2"]))
    story.append(Paragraph(description, styles["BodyText"]))
    story.append(Spacer(1, 16))
document.build(story)
print("Sample Company Policy PDF Created!")
print("File Name:", filename)
print("Total Policies:", len(policies))