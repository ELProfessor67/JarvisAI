import smtplib
myContact = {
	"name":"+919999999999", 
	"name":"+919999999999",
	"name":"+919999999999",
	"name":"+919999999999",
	"name":"+919999999999",
	"name":"+919999999999"
}

mailContact = {
	"name":"example@gmail.com", 
	"name":"example@gmail.com",
	"name":"example@gmail.com",
	"name":"example@gmail.com",
	"name":"example@gmail.com",
}


def mailer(to,text):
	try:
		s = smtplib.SMTP("smtp.gmail.com",587)
		s.starttls()
		s.login("example@gmail.com","email password")
		s.sendmail("example@gmail.com",to,text)
	except Exception as e:
		return "send failed"
	s.quit()
	return "send succesfully"