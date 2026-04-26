def total_reservas(lista):
 if len(lista) == 0: 
  return 0
 return 1 + total_reservas(lista[1:])
