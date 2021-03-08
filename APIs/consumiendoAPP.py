import requests as req
      
#resp = req.get('http://localhost:5000/')
#print(resp.text)



#resp = req.get('http://localhost:5000/saludar/EDGAR_RODRIGUEZ')
#resp= resp.json()
#print(resp["about"])

#Saludar con parametros
#resp2 = req.get('http://localhost:5000/saludar/?nombre=Edgarsito')
#print (resp2.text)

#POST
datos = {'nombre':'Edgar', 'apellido':'Rodriguez'}
resp = req.post('http://localhost:5000/guardar/', data=datos)
print(resp.text)