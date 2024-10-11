class Producto:
    #Constructor clase producto
    def __init__(self, nombre, categoria, precio, cantidad):        
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad
        
        #Llamamos a las validaciones 
        self.setPrecio(precio)
        self.setCantidad(cantidad)
        
    #Definicion de los getters y setters
    def getNombre(self):
        return self.__nombre
        
    def setNombre(self, nombre):
        self.__nombre = nombre   

    def getCategoria(self):
        return self.__categoria
        
    def setCategoria(self, categoria):
        self.__categoria = categoria   

    def getPrecio(self):
        return self.__precio
        
    def setPrecio(self, precio):
        if (precio > 0):
            self.__precio = precio
        else: 
            raise ValueError("El precio tiene que ser mayor a 0. No tenemos productos gratis.")

    def getCantidad(self):
        return self.__cantidad
        
    def setCantidad(self, cantidad):
        if (cantidad >= 0):
            self.__cantidad = cantidad   
        else: 
            raise ValueError("La cantidad tiene que ser mayor o igual a 0.")
        
    # Método por mostrar por pantalla el producto.
    def __str__(self):
        return f"Nombre: {self.__nombre}, Categoría: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"    
        
        
class Inventario:
    def __init__(self):
        self.__productos = []
        
    #Definicion metodos
    def AgregarProducto(self, producto):
        #Buscamos el producto, si existe actualizamos la cantidad, si no existe lo añadimos
        existeProducto = False
        for existingProduct in self.__productos:
            if (existingProduct.getNombre() == producto.getNombre()):
                existeProducto = True
                existingProduct.setCantidad(producto.getCantidad() + existingProduct.getCantidad())
                print("El producto ya existía, se ha actualizado la cantidad.")
            
        if (not existeProducto):
            self.__productos.append(producto)
            print("El producto se ha agregado correctamente.")
                

    def ActualizarProducto(self, nombre, tipo, valor):
        existeProducto = False
        for existingProduct in self.__productos:
            if (existingProduct.getNombre() == nombre):
                match tipo:
                    case "Precio":
                        try:
                            existingProduct.setPrecio(valor)
                            print("El precio del producto " + nombre + " se ha actualizado correctamente")
                        except ValueError as e:
                            print(e)
                    case "Cantidad":
                        try:
                            existingProduct.setCantidad(valor)
                            print("La cantidad del producto " + nombre + " se ha actualizado correctamente")
                        except ValueError as e:
                            print(e)                        
                    case _:
                        print("El tipo de actualización " + tipo + " no es correcto.")
                return
            
        print("El producto " + nombre + " no se ha encontrado.")      
    
    def BorrarProducto(self, nombre):
        for existingProduct in self.__productos:
            if (existingProduct.getNombre() == nombre):
                self.__productos.remove(existingProduct)
                print("El producto " + nombre + " se ha eliminado correctamente")
                return
            
        print("El producto no se ha podido eliminar ya que no ha sido encontrado")
                
    def BuscarProducto(self, nombre):        
        for existingProduct in self.__productos:
            if (existingProduct.getNombre() == nombre):
                print(existingProduct)
                return
                
        print("El producto " + nombre + " no se ha encontrado en el inventario.")                
    
    def MostrarInventario(self):
        for producto in self.__productos:
            print(producto)
    
    
#Creamos 3 productos, el último tiene el mismo nombre, con lo que actualizamos la cantidad.
producto1 = Producto("Manzanas", "Fruta", 2, 4)
producto2 = Producto("Peras", "Fruta", 3, 9)
producto3 = Producto("Manzanas", "Fruta", 10, 7)
producto4 = Producto("Melocotones", "Fruta", 4, 25)
producto5 = Producto("Melón", "Fruta", 6, 10)

#Creamos el inventario y añadimos 3 productos
inventario = Inventario()
print("Añadimos algunos productos")
inventario.AgregarProducto(producto1)
inventario.AgregarProducto(producto2)
inventario.AgregarProducto(producto3)
inventario.AgregarProducto(producto4)
inventario.AgregarProducto(producto5)
inventario.MostrarInventario()
print("**************************************************************************************************")
#Buscamos un producto
print("Buscamos un producto")
inventario.BuscarProducto("Peras")
print("**************************************************************************************************")
#Borramos un producto
print("Borramos un producto")
inventario.BorrarProducto("Peras")
inventario.MostrarInventario()
print("**************************************************************************************************")
#Actualizamos un producto y cambiamos el precio
print("Actualizamos precio producto")
inventario.ActualizarProducto("Manzanas", "Precio", -10)
inventario.ActualizarProducto("Manzanas", "Precio", 0)
inventario.ActualizarProducto("Manzanas", "Precio", 15)
inventario.MostrarInventario()
print("**************************************************************************************************")
#Actualizamos un producto y cambiamos la cantidad
print("Actualizamos cantidad producto")
inventario.ActualizarProducto("Manzanas", "Cantidad", -3)
inventario.ActualizarProducto("Manzanas", "Cantidad", 0)
inventario.ActualizarProducto("Manzanas", "Cantidad", 5)
inventario.MostrarInventario()

inventario.ActualizarProducto("Manzanas", "Ordenadores", 5)        
