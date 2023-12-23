from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "post":
		message_name = request.post['message-name']
		message_email = request.post['mesasage-email']
		message = request.post['message']

		# send an email
		send_mail(
			message_name,
			message,
			message_email,
			['apotheekwesterbork@gmail.com'],


			)



		return render(request, 'contact.html', {'message_name': message_name})


	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})


def service(request):
	return render(request, 'service.html', {})


