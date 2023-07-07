##################### Normal Starting Project ######################
import pandas
import random
import datetime as dt
import smtplib

my_email = "godstand.aimiuwu@gmail.com"
my_password = "Osadebamen12345+"

today = dt.datetime.today()
today_tuple = (today.month, today.day)

# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
# Dictionary comprehension template for pandas DataFrame looks like this:
birthday_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}
# HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthday_dict:
    try:
        birthday_person = birthday_dict[today_tuple]
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(file_path) as letter:
            contents = letter.read()
            contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person["email"],
                msg=f"Subject: Happy Birthday{birthday_person['name']}!\n\n{contents}",
            )
        print("Email sent successfully")
    except smtplib.SMTPConnectError as error:
        print(f"An error occurred while sending the email: {error}")

