import re

def verificar_senha(senha):
  erros = []
  if len(senha) < 8:
    erros.append('Senha deve ter pelo menos 8 caracteres.')
  if not re.search('[A-Z]', senha):
    erros.append('Senha deve conter pelo menos uma letra maiúscula.')
  if not re.search('[0-9]', senha):
    erros.append('Senha deve conter pelo menos um número.')
  
  if len(erros) == 0:
    return True, 'Senha válida'
  else:
    return False, f'Sua senha não atinge o padrão de segurança exigido pela empresa! Verifique os erros: {erros}' 
