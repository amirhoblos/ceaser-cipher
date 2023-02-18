from artwork import logo
alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
  't', 'u', 'v', 'w', 'x', 'y', 'z'
]
def encrypt(texted,shifted):
  crypted_message=''
  for letter in texted:
    if letter in alphabet:
      index_in_alphabet=alphabet.index(letter)
      crypted_message+=alphabet[(index_in_alphabet + shifted)%26]
    else:
      crypted_message+=letter
  print(f"encrypted message :{crypted_message}")

def decrypt(texted,shifted):
  decrypt_message=''
  for letter in texted:
    if letter in alphabet:
      index_in_alphabet=alphabet.index(letter)
      decrypt_message+=alphabet[(index_in_alphabet - shifted)%26]
    else:
      encrypted_message+=letter
  print(f"decrypted message :{decrypt_message}")
print(logo)
print('***CEASER CYPHER PROGRAM***')
request='yes'
while request=='yes':
  direction=input('type e to encrypt and d to decrypt:\n ')
  while direction != "e" and direction != "d":
    print('type e or d')
    direction=input('type e to encrypt , type d to decrypt:\n')
  text=input('type your message:\n')
  if text!=alphabet:
    print('you can only use letters')
    input('type your message:\n')
  shift=int(input('type the shift number:\n'))
  while shift>26:
    print('enter a number between 0 and 26')
    shift=int(input('type the shift number:\n'))
  if direction =='e':
    encrypt(texted=text,shifted=shift) 
  else :
    decrypt(texted=text,shifted=shift)
  request=input ("type 'yes' if you want to go again,'no' to stop the program:\n")       