from lista.py import total_reservas
class Usuario:
  contador = 0
  def __init__(self, nombre):
   self.nombre= nombre

  def __str__(self):
    return f"Usuario: {self.nombre}"
    
class Cliente(Usuario):
  def __init__ (self, nombre):
   super().__init__(nombre)
    self._reservas= []
    
  @property
  def reservas(self):
    return self._reservas
    
  def agregar_reservas(self, reservas):
    self._reservas.append()

  def cancelar_reserva():
    for r in self._reservas: 
            if r.codigo == codigo:
                self._reservas.remove(r)
                print("Reserva cancelada")
                return
        print("No encontrada")
    
  def __str__(self):
    return f"Nombre del cliente: {self.nombre}, su reserva: {len(self._reservas)}"

class Reserva():
  def __init__(self, codigo, precio):
    self.codigo = codigo
    self.precio = precio
  def __str__():
    return f"codigo de la reserva: {self.codigo}, precio: (${self.precio})"

class sistema():
  def __init__(self):
        self.clientes = {}  
        self.codigos = set()  

    def agregar_cliente(self, cliente):
        self.clientes[cliente.nombre] = cliente

    def crear_reserva(self, nombre, codigo, destino, precio):
        if codigo in self.codigos:
            print("Código ya existe")
            return

        reserva = Reserva(codigo, destino, precio)
        self.codigos.add(codigo)

        self.clientes[nombre].agregar_reserva(reserva)

    def mostrar_reservas(self, nombre):
        cliente = self.clientes[nombre]

        for r in cliente.reservas: 
            print(r)

    def total_reservas_cliente(self, nombre):
        return total_reservas(self.clientes[nombre].reservas)

    def limpiar_codigos(self):
        self.codigos.clear()


    
