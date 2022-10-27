##################### Extra Hard Starting Project ######################
import random
import pandas
import datetime as dt
import smtplib

my_email = "testc1386@gmail.com"
password = "wxpljviwkfzazsl"

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dic = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.today()
today_tuple = (today.month, today.day)

if today_tuple in birthdays_dic:
    letter_nb = random.randint(1, 3)
    birthday_person = birthdays_dic[today_tuple]
    with open(f"letter_templates/letter_{letter_nb}.txt", "r") as letter:
        words = letter.read()
        words = words.replace("[NAME]", birthday_person["name"])
    print(birthday_person)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Birthday\n\n{words}")


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.


