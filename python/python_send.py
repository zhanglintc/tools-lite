# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

to_addr = [
    "mailto@domain.com",
]

from_addr   = "youremail@domain.com"
alias       = "Admin"
password    = "yourpassword"
smtp_server = "smtp.domain.com"

subject = "Python Email Tool"
content = "hello, send by Python..."

msg = MIMEText(content, 'plain', 'utf-8')
msg['From']    = _format_addr(u'{0} <{1}>'.format(alias, from_addr))
msg['Subject'] = Header(subject, 'utf-8').encode()

if __name__ == '__main__':
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


