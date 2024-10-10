class Producto:
    #Constructor clase producto
    def __init__(self, nombre, categoria, precio, cantidad):        
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad
        
    #Definicion de los getters y setters
    def getNombre(self):
        return self._nombre
        
    def setNombre(self, nombre):
        self._nombre = nombre   

    def getCategoria(self):
        return self._categoria
        
    def setCategoria(self, categoria):
        self._categoria = categoria   

    def getPrecio(self):
        return self._precio
        
    def setPrecio(self, precio):
        self._precio = precio   

    def getCantidad(self):
        return self._cantidad
        
    def setCantidad(self, cantidad):
        self._cantidad = cantidad   
        
        
class Inventario:
    def __init__(self):
        self._productos = []
        
    #Definicion metodos
    def add(self, producto):
        if (producto.getPrecio() <= 0):
            print("El producto " + producto.getNombre() + " no puede añadirse ya que el precio introducido no es válido.")
        else:
            #Buscamos el producto, si existe actualizamos la cantidad, si no existe lo añadimos
            existeProducto = False
            for existingProduct in self._productos:
                if (existingProduct.getNombre() == producto.getNombre()):
                    existeProducto = True
                    existingProduct.setCantidad(producto.getCantidad() + existingProduct.getCantidad())
                
            if (not existeProducto):
                self._productos.append(producto)
                
    def searchProduct(self, nombre):        
        for existingProduct in self._productos:
            if (existingProduct.getNombre() == nombre):
                print("El producto: " + existingProduct.getNombre() + ", pertenece a la categoría de " + existingProduct.getCategoria() + ". Tenemos una cantidad de " + str(existingProduct.getCantidad()) + " y cada uno cuesta: " + str(existingProduct.getPrecio()) + " euros.")
            else:
                print("El producto " + nombre + " no se ha encontrado en el inventario.")


                
    def update(self, nombre, tipo, valor):
        existeProducto = False
        for existingProduct in self._productos:
            if (existingProduct.getNombre() == nombre):
                existeProducto = True      
                if ((tipo == "Precio") and (valor>0)):
                    existingProduct.setPrecio(valor)
                elif ((tipo == "Precio") and (valor<=0)):
                    print("Error, el precio no se puede actualizar ya que es 0.")
                elif ((tipo == "Cantidad") and (valor>=0)):
                    existingProduct.setCantidad(valor)
                else:
                    print("Error, la cantidad no puede ser menor que 0.")
                    
        if (not existeProducto):
            print("El producto " + nombre + " no se ha encontrado.")        
    
    def delete(self, nombre):
        for existingProduct in self._productos:
            if (existingProduct.getNombre() == nombre):
                self._productos.remove(existingProduct)
    
    def showInventory(self):
        for producto in self._productos:
            print("El producto: " + producto.getNombre() + ", pertenece a la categoría de " + producto.getCategoria() + ". Tenemos una cantidad de " + str(producto.getCantidad()) + " y cada uno cuesta: " + str(producto.getPrecio()) + " euros.")
    
    
#Creamos 3 productos, el último tiene el mismo nombre, con lo que actualizamos la cantidad.
producto1 = Producto("Manzanas", "Fruta", 10, 1)
producto2 = Producto("Peras", "Fruta", 10, 1)
producto3 = Producto("Manzanas", "Fruta", 10, 7)

#Creamos el inventario y añadimos los 3 productos
inventario = Inventario()
inventario.add(producto1)
inventario.add(producto2)
inventario.add(producto3)
inventario.showInventory()
inventario.searchProduct("Peras")
print("**************************************************************************************************")
#Borramos un producto
inventario.delete("Peras")
inventario.showInventory()
print("**************************************************************************************************")
#Actualizamos un producto y cambiamos la cantidad y el precio
inventario.update("Manzanas", "Precio", -10)
inventario.update("Manzanas", "Precio", 15)
inventario.showInventory()
print("**************************************************************************************************")
inventario.update("Manzanas", "Cantidad", 0)
inventario.update("Manzanas", "Precio", 15)
inventario.showInventory()
        
