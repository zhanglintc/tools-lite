# -*- coding: utf-8 -*-

import os, sys
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

# Refer to: https://my.oschina.net/u/1179554/blog/214387
mailInfo = {
    "from": "发信人用户名@qq.com",
    "to": "收信人用户名@qq.com",
    "hostname": "smtp.qq.com",
    "username": "账户名",
    "password": "密码",
    "mailsubject": "邮件标题",
    "mailtext": "邮件正文",
    "mailencoding": "utf-8",
}
        
if __name__ == '__main__':
    smtp = SMTP_SSL(mailInfo["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mailInfo["hostname"])
    smtp.login(mailInfo["username"],mailInfo["password"])
    
    msg = MIMEText(mailInfo["mailtext"], "plain", mailInfo["mailencoding"])
    msg["Subject"] = Header(mailInfo["mailsubject"], mailInfo["mailencoding"])
    msg["from"] = mailInfo["from"]
    msg["to"] = mailInfo["to"]
    smtp.sendmail(mailInfo["from"], mailInfo["to"], msg.as_string())
    
    smtp.quit()

