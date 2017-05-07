#!/usr/bin/python
import smtplib
def mail(subject_header,body) :
	mail_server = 'smtpz.univ-avignon.fr'
	mail_server_port = 465
	from_addr = 'omar.sy@alumni.univ-avignon.fr'
	to_addr = 'omarsysy@gmail.com'
	from_header = 'From:%s\r\n' % from_addr
	to_header = 'To: %s\r\n\r\n' % to_addr 
	email_message = '%s\n%s\n%s\n\n%s' % (from_header,to_header,subject_header,body)	
	s = smtplib.SMTP_SSL(mail_server,mail_server_port)
	s.set_debuglevel(1)
	s.login('omar.sy@alumni.univ-avignon.fr','')
	s.sendmail(from_addr,to_addr,email_message)
	s.quit()
