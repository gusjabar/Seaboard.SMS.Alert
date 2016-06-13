import smtplib


def send_sms(msg):
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('mail.seaboardmarine.com')
    s.sendmail('gustavo.barreto@seaboardmarine.com', '7866269496@txt.att.net', 'Error demo', msg)
    s.quit()
