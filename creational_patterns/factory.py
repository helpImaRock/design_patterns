import abc


class Product(metaclass=abc.ABCMeta):

    '''
        abstract base class
    '''

    
    @abc.abstractmethod
    def doStuff(self):
        pass

class MyProductA(Product):
    
    def doStuff(self) -> str:
        return "{Result of the ConcreteProduct1}"

class MyProductB(Product):

    def doStuff(self) -> str:
        return "{Result of the ConcreteProduct2}"

'''
    CREATOR CLASS

'''

class Creator(metaclass=abc.ABCMeta):
    '''
       Creator class, responsible for declaring the factory method
    '''

    @abc.abstractmethod
    def factory_method(self):
        '''
            method to be implemented by subclass ( code that uses the factory method )
            can provide a default implementation
        '''
        pass


    def some_operation(self) -> str:
        '''
        calls the factory method
        '''
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.doStuff()}"


'''
    Implementing creator classes

'''


class ConcreteCreatorA(Creator):


    def factory_method(self) -> Product:
        '''
            factory method
        '''
        return MyProductA()



class ConcreteCreatorB(Creator):


    def factory_method(self) -> Product:
        '''
            factory method
        '''
        return MyProductB()


def client_code(creator: Creator) -> str:
    print(f'client code'
            f"{creator.some_operation()}"
    )


if __name__ == '__main__':


    productA = client_code(ConcreteCreatorA())
    
    productB = client_code(ConcreteCreatorB())