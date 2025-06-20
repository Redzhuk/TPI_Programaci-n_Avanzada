from abc import ABC, abstractmethod

# Clase Interfaz------------

class EstrategiaCalculo(ABC):
    @abstractmethod
    def calcular(self, datos: dict) -> float:
        pass

class SeguroBase(ABC):
    @abstractmethod
    def calcular(self) -> float:
        pass
    
# Clases concretas-----------

class CalculoSeguroAuto(EstrategiaCalculo):
    def calcular(self, datos: dict) -> float:
        anio_actual = 2025
        tarifa_base = 10000
        antiguedad = anio_actual - datos.get("anio_auto", anio_actual)
        return tarifa_base + antiguedad * 500

class CalculoSeguroVida(EstrategiaCalculo):
    def calcular(self, datos: dict) -> float:
        tarifa_base = 20000
        edad = datos.get("edad", 30)
        return tarifa_base + edad * 300

class SeguroConcreto(SeguroBase):
    def __init__(self, estrategia: EstrategiaCalculo, datos: dict):
        self.estrategia = estrategia
        self.datos = datos
        
    def calcular(self) -> float:
        return self.estrategia.calcular(self.datos)


# Decorador --------

class DescuentoClienteNuevo(SeguroBase):
    def __init__(self, seguro: SeguroBase):
        self.seguro = seguro

    def calcular(self) -> float:
        return self.seguro.calcular() * 0.9  # 10% de descuento

# Fábrica de estrategias--------

class SeguroFactory:
    @staticmethod
    def crear_seguro(tipo: str) -> EstrategiaCalculo:
        if tipo == "auto":
            return CalculoSeguroAuto()
        elif tipo == "vida":
            return CalculoSeguroVida()
        else:
            raise ValueError("Tipo de seguro no reconocido")

# --------------------------
# Ejemplo de uso
# --------------------------

if __name__ == "__main__":
    # Datos del cliente
    datos_auto = {"anio_auto": 2020}
    datos_vida = {"edad": 40}

    # Crear estrategias desde la fábrica
    estrategia_auto = SeguroFactory.crear_seguro("auto")
    estrategia_vida = SeguroFactory.crear_seguro("vida")

    # Crear seguros
    seguro_auto = SeguroConcreto(estrategia_auto, datos_auto)
    seguro_vida = SeguroConcreto(estrategia_vida, datos_vida)

    # Aplicar decorador de descuento
    seguro_auto_descuento = DescuentoClienteNuevo(seguro_auto)

    # Resultados
    print("Seguro de auto:", seguro_auto.calcular())  # sin descuento
    print("Seguro de auto con descuento:", seguro_auto_descuento.calcular())
    print("Seguro de vida:", seguro_vida.calcular())
