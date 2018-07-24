
"""

    En Python cada elemento de información es un objeto (incluso int, string, etc)
    La palabra clave 'pass' significa "no hay más que hacer aquí por ahora ..."
    A cualquier objeto se le pueden agregar directamente campos de información
    (variables de instancia) en tiempo de ejecución! sólo en Python :S
    ~ esto indica que la estructura de datos se mantiene "modificable"
    y por lo tanto algunas instancias pueden o no tener ciertas variables!!

"""

class Person :
    pass

instance_person = Person()
instance_person.name = 'Carlos Soria'
instance_person.nickname = 'Dionisos'

"""

    Los métodos definidos en una clase si es que serán asociados a una
    instancia de la misma, deben llevar 'self' como parámetro en su definición.
    El método __init__ es el constructor en Python, invocado una vez que
    se crea una instancia de la clase ...
    Cuando Python evalua un método a través de un objeto, automáticamente
    pasa un referencia del mismo. Es por ello que se utiliza 'self' :P
    El método __str__ determina que sucede cuando un objeto se convierte a cadena.

"""

class Dog :

    def __init__(self, name, breed) :
        self.name = name
        self.breed = breed

    def __str__(self) :
        return "Cadena instancia > " + self.name

    def speak(self) :
        print("ID instancia:", self.name)

proof_instance = Dog(breed='Purina', name='Roque')
instance_dog = Dog('Jack', 'Eukanuba')
instance_dog.speak()
print(instance_dog)


"""

    Se comenta que Python es un lenguake para pequeños sistema no comerciales :(
    No dispone de modificadores de acceso, nada es privado todo es público!!

"""

class Point3D :

    # Es posible asignar valores por defecto para simular un "constructor default"
    def __init__(self, x, y, z) :
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other) :
        d1 = self.x - other.x
        d2 = self.y - other.y
        d3 = self.z - other.z
        return Point3D(d1, d2, d3)

    def __eq__(self, other) :
        return (self.x==other.x and self.y==other.y and self.z==other.z)

point = Point3D(4, 7, 9)
print("Tipo Point3D:", isinstance(point, Point3D))

# Para indicar argumentos variables se emplea un asterisco ...
def print_them_out(primer_argumento, *args) :
    for thing in args :
        print(thing, end=' ')

print_them_out("Dionisos", 'John', 'Paul', 'George', 'Ringo')

"""

    Cuando una clase hereda de otra, automáticamente obtiene los métodos
    y atributos del padre. Los cuales puede mantener u modificar.
    En Python todos los métodos son heredados incluídos los especiales (__init__)
    Todas la 'variables de clase' son heredadas.
    No obstante las 'variables de instancia' no necesariamente.
    ~ debido a que las variables están atadas a las instancias y no a las clases!

"""

class Pet :
    def __init__(self, name, breed, age) :
        self.name = name
        self.breed = breed
        self.age = age

    def saludo(self) :
        print("\nNiemand verascht!")

class Dog (Pet) :
    def __init__(self, name, breed, age, toy) :
        self.toy = toy
        Pet.__init__(self, name, breed, age)

mascota = Dog("Jack", "DogChow", 3, "Puppet")
mascota.saludo()


from fractions import Fraction

class PFraction(Fraction) :
    def __str__(self) :
        n = self.numerator
        d = self.denominator
        i = n // d
        int_str = str(i)+ ' ' if i > 0 else ''
        n = n % d
        n_str = str(n)+'/'+ str(d) if n > 0 else ''
        return int_str + n_str

    def __add__(self, other) :
        f = Fraction.__add__(self, other)
        return PFraction(f)

f1 = PFraction('1/2')
f2 = PFraction('2/3')

print('El resultado es: ', f1 + f2)

"""

    Para crear una "variable de clase" solamente hay que definirlas dentro
    del cuerpo de la clase (sin un 'self' asociado claro).
    Por otro lado es posible crear métodos estáticos @staticmethod y
    métodos de clase @classmethod (se requiere de la anotación)

    Python resuelve expresiones del tipo "object.var" del modo:
    1. como una variable de instancia
    2. como una variable de clase
    3. como una variable de clase heredada

"""

class Vinyl :
    num_instances = 0
    def __init__(self, name, group) :
        self.name = name
        self.group = group
        Vinyl.num_instances += 1

    @staticmethod
    def metodo_estatico() :
        print('Instancias creadas >', Vinyl.num_instances)

ride_lighting = Vinyl('Ride the Lighting', 'Metallica')
black = Vinyl('Black Album', 'Metallica')
Vinyl.metodo_estatico()


"""
Python Without Fear - Brian Overland
Ed. Addison-Wesley Professional 2017
SECUENCIA
18. Advanced Pythonic Techniques
(Con dicho capítulo terminamos el libro ...)
"""
