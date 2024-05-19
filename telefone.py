import re 

def validate_numero_telefone(phone_number):
    pattern = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    validacao = "Número de telefone inválido."
   
    if re.match(pattern, phone_number):  
       validacao = "Número de telefone válido."
   
    return validacao

def main():
    phone_number = input("Informe o número de telefone")
    result = validate_numero_telefone(phone_number)
    print(result)

if __name__ == "__main__":
  main()