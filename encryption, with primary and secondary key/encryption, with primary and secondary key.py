from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

#Criação das chaves privadas e publicas.
modulus_lenght = 256 * 4
private_key = RSA.generate(modulus_lenght, Random.new().read)
public_key = private_key.publickey()

    
#O codigo abaixo é uma funcao que ira criptografar uma mensagem futura com uma chave publica RSA
def encryption(public_key, message):
    encryptor = PKCS1_OAEP.new(public_key)
    ciphertext = encryptor.encrypt(message)
    return base64.b64encode(ciphertext)

#O codigo abaixo é uma funcao que ira descriptografar uma mensagem futura com uma chave privada RSA
def decryption(private_key, message):
    decoded_data = base64.b64decode(message)
    decryptor = PKCS1_OAEP.new(private_key)
    decrypted = decryptor.decrypt(decoded_data)
    return decrypted

#Verificação da distancia do navio da costa e da area de isolamento.
cond = False

while cond == False:
	distancia = int(input(('Informe a distância entre o navio e a costa em km: ')))
	if distancia >= 50:
		cond = True
	else:
		print('Distância insuficiente')
	
area = int(input('Informe o tamanho em km da área isolada no entorno do navio? '))
if area < 10:
	sys.exit()
helicoptero = True	
trajado = True
	
#Mensagem que deseja criptografar.
def mensagem():
	while area >=10 and helicoptero == True and distancia >=50:
		message = input('escreva a mensagem a ser criptografada: ').encode()
		a = encryption(public_key, message)
		b = decryption(private_key, a)
		print(a)
		a = str(input('Deseja descriptografar a mensagem usando sua chave privada? Sim ou Nao?'
))
		if a == 'Sim':
			print(b)
		elif a == 'Nao':
			print('\nacabou')
		else:
			print('Digitado incorretamente')
		
#Colocamos os inpetores que estarão usando de nossa ferramenta e se estão ou não trajados para o trabalho. E criamos uma lista com essas informações.


inspetor1 = ['Gustavo zero', trajado]


inspetor2 = ['Miguel D. Blue', trajado]


inspetor3 = ['Mateus Notes', trajado]


inspetor4 = ['Paula T. Vasconcelos', trajado]


inspetor5 = ['Daniel Jando Mendes', trajado]


inspetor6 = ['Bruna Matilda', trajado]


inspetor7 = ['Ana Arcane Key', trajado]


inspetor8 = ['Bianca Nine Locke', trajado]

inspetor9 = ['Saiki Kusuo']

inspetor10 = ['Hori Teruhashi']



#A pessoa deverá colocar seu nome de cadastro e será verificado se o nome dela consta na lista e se está ou não trajada para o trabalho.


pessoa = str(input('Digite o nome no cadastro do inspetor(a): '))

if pessoa in inspetor1 and trajado in inspetor1:
	mensagem()	
elif pessoa in inspetor2 and trajado in inspetor2:
	mensagem()
elif pessoa in inspetor3 and trajado in inspetor3:
	mensagem()
elif pessoa in inspetor4 and trajado in inspetor4:
	mensagem()
elif pessoa in inspetor5 and trajado in inspetor5:
	mensagem()
elif pessoa in inspetor6 and trajado in inspetor6:
	mensagem()
elif pessoa in inspetor7 and trajado in inspetor7:
	mensagem()
elif pessoa in inspetor8 and trajado in inspetor8:
	mensagem()
elif pessoa in inspetor9 and trajado in inspetor9:
	mensagem()
elif pessoa in inspetor10 and trajado in inspetor10:
	mensagem()
else:
	print('Não possui o cadastro ou não está trajada corretamente')


