from HTMLTestRunner_cn import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
import smtplib
import unittest
import time
import os

# 定义发送邮件
def send_mail(file_new, filename):

    smtpserver = 'smtp.qq.com'
    username = '272316377@qq.com'
    password = 'ehdodmcjmnqkcbbi'

    sender = '272316377@qq.com'
    receiver = 'luffy000000@126.com'

    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEMultipart()

    # 邮件标题
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    # 邮件内容
    text = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(text)
    
    # 发送附件
    att = MIMEApplication(open(filename, 'rb').read())
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(att)
    
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        time.sleep(5)
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print(e)

# 查找最新的测试报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + '/' + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == "__main__":
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './panda/report/' + now + 'result.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(stream=fp, title='测试报告', description='环境:Linux　　浏览器:Chrome')
    discover = unittest.defaultTestLoader.discover('./panda/testcase', pattern='*_sta.py')
    runner.run(discover)
    fp.close()

    file_path = new_report('./panda/report')
    send_mail(file_path, filename)