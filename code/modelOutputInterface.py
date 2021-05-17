class ModelOutputMeta(type):
    """Any handler that connects the Model's predictions to the UI must implement the following methods"""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'getPrediction') and 
                callable(subclass.getPrediction) and 

class ModelOutputInterface(metaclass=ModelOutputMeta):
    pass
