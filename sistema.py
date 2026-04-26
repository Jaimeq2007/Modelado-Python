from lista import total_reservas


class Usuario:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.contador += 1

    def __str__(self):
        return f"Usuario: {self.nombre}"

    @classmethod
    def total_usuarios(cls):
        return cls.contador


class Cliente(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)
        self._reservas = []

    @property
    def reservas(self):
        return self._reservas

    def agregar_reservas(self, reserva):
        self._reservas.append(reserva)

    def cancelar_reserva(self, codigo):
        for r in self._reservas:
            if r.codigo == codigo:
                self._reservas.remove(r)   
                print("Reserva cancelada")
                return
        print("No encontrada")

    def __str__(self):
        return f"Nombre del cliente: {self.nombre}, su reserva: {len(self._reservas)}"


class Reserva:
    def __init__(self, codigo, numero_mesa, precio):
        self.codigo = codigo
        self.numero_mesa= numero_mesa
        self.precio = precio

    def __str__(self):
        return f"codigo de la reserva: {self.codigo}, numero de mesa: {self.numero_mesa}, precio: ${self.precio}"


class Sistema:
    def __init__(self):
        self.clientes = {}   
        self.codigos = set() 
        self.mesas_ocupadas = set()  

    def agregar_cliente(self, cliente):
        self.clientes[cliente.nombre] = cliente

    def crear_reserva(self, nombre, codigo, numero_mesa, precio):
        if codigo in self.codigos:
            print("Código ya existe")
            return
        
        if numero_mesa in self.mesas_ocupadas:
            print("La mesa ya esta ocupada")
            return

        if nombre not in self.clientes:
            print("Cliente no existe")
            return

        reserva = Reserva(codigo,numero_mesa, precio)
        self.codigos.add(codigo)
        self.mesas_ocupadas.add(numero_mesa)
        self.clientes[nombre].agregar_reservas(reserva)

    def mostrar_reservas(self, nombre):
        cliente = self.clientes[nombre]

        for r in cliente.reservas:   
            print(r)

    def total_reservas_cliente(self, nombre):
        
        return total_reservas(self.clientes[nombre].reservas)

    def eliminar_codigo(self, codigo):
        self.codigos.discard(codigo)  

    def limpiar_codigos(self):
        self.codigos.clear()  

sistema = Sistema()


cliente1 = Cliente("Juan")
sistema.agregar_cliente(cliente1)
print("Total usuarios:", Usuario.total_usuarios())

sistema.crear_reserva("Juan", 1, 7, 100)
sistema.crear_reserva("Juan", 2, 8, 150)


print("Reservas hechas:")
sistema.mostrar_reservas("Juan")


print("Total reservas:", sistema.total_reservas_cliente("Juan"))

cliente1.cancelar_reserva(1)

print("Reservas restantes:")
sistema.mostrar_reservas("Juan")

    
