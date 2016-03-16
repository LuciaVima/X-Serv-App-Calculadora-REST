import webapp

class App(webapp.webApp):
	def parse(self, request):
		metodo = request.split(' ',2)[0]
		try:
			recurso = request.split(' ',2)[1]
		except:
			recurso = "/"
		try:
			cuerpo = request.split('\r\n\r\n')[1]
		except IndexError:
			cuerpo = ""
		return metodo, recurso, cuerpo

	def process(self, peticion):
		metodo, recurso, cuerpo = peticion
		if (metodo == "GET"):
			httpCode = "200 OK"
			htmlBody = "<html><body>" \
			+ 'Bienvenido a la calculadora, introduzca los sumandos mediante POST.' \
			+ "</body></html>"

		elif (metodo == "POST"):
			numero1 = cuerpo.split(' ')[0]
			numero2 = cuerpo.split(' ')[1]
			if (recurso == '/suma'):
				try:
					resultado = int(numero1) + int(numero2)
					httpCode = "200 OK"
					htmlBody = str(resultado)
				except ValueError:
					httpCode = "200 OK"
					htmlBody = "Introduzca sumandos validos"

			elif (recurso == '/resta'):
				try:
					resultado = int(numero1) - int(numero2)
					httpCode = "200 OK"
					htmlBody = str(resultado)
				except ValueError:
					httpCode = "200 OK"
					htmlBody = "Introduzca sumandos validos"


			elif (recurso == '/division'):
				try:
					resultado = int(numero1) / int(numero2)
					httpCode = "200 OK"
					htmlBody = str(resultado)
				except ValueError:
					httpCode = "200 OK"
					htmlBody = "Introduzca sumandos validos"

			elif (recurso == '/multiplicacion'):
				try:
					resultado = int(numero1) * int(numero2)
					httpCode = "200 OK"
					htmlBody = str(resultado)
				except ValueError:
					httpCode = "200 OK"
					htmlBody = "Introduzca sumandos validos"


			else:
				httpCode = "200 OK"
				htmlBody = "Recurso no valido. Introduzca otro de nuevo."
				
			
				
		else:
			httpCode = "450 Method Not Allowed"
			htmlBody = "Go Way!"

		return (httpCode, htmlBody)



if __name__ == "__main__":
	try:
		myWebApp = App("localhost", 1234)
	except KeyboardInterrupt:
		print "Gracias por utilizar la aplicacion."
