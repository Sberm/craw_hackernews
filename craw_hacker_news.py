import requests
from bs4 import BeautifulSoup
import smtplib 
from email.message import EmailMessage
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def craw():
    url = "https://news.ycombinator.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    titles_raw = soup.find_all("span", class_="titleline")
    news_num = 21
    titles = ""
    red = "#DA0C81"
    green = "#01C34A"
    for index, title in enumerate(titles_raw):
        link = title.find('a', href=True)['href']
        if (index < 6):
            titles += f"""<a href="{link}" style="color: {green}; text-decoration:none; font-size:18px;">{title.text}</a><br><br><br>"""
        else:
            titles += f"""<a href="{link}" style="color: {red}; text-decoration:none; font-size:18px;">{title.text}</a><br><br><br>"""
        if index >= news_num - 1:
            break

    html = f"""<html>
    <body>
        <h1>Hacker News Digest</h1>
        {titles}
    </body>
</html>"""

    def send_email(html: str):

        sender_email = "howardchu95@gmail.com"
        Pass = "pmdf eplw fome sunx"

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "骇客新闻"
        msg['From'] = "Sberm Digest"
        msg['To'] = '1007273067@qq.com'

        html = MIMEText(html, 'html')
        msg.attach(html)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(sender_email,Pass)
            smtp.send_message(msg)

    send_email(html)

times_to_send = ['07:50:00']

def check_times_up():
    for t in times_to_send:
        t_p = time.strptime(t, "%H:%M:%S")
        now_ = time.localtime()
        if (t_p.tm_hour == now_.tm_hour and
            t_p.tm_min == now_.tm_min and
            t_p.tm_sec == now_.tm_sec):
            return True
            break
    return False

if __name__ == "__main__":
    while True:
        if check_times_up():
            craw()
        sleep(1)
