import seguranca

print('PIAUÍ INSTITUTO DE TECNOLOGIA - PIT')
print('Bacharelado em Inteligência Artificial')
print()
print('VERIFICAÇÃO DE SENHA')
print()

while True:
  senha_digitada = input('Colaborador, digite sua senha (mínimo de 8 caracteres, necessário pelo menos um número e uma letra maiúscula): ')

  status, mensagem = seguranca.verificar_senha(senha_digitada)

  if status == True:
    print()
    print(f'{mensagem}')
    break
  elif status == False:
    print()
    print(f'{mensagem}')
    print('Por favor, tente novamente')
  else:
    print()
    print('Algo deu errado!')
    print('Por favor, tente novamente')
    break
