class ModelOutputHandlerInterface():
    """Any handler that connects the Model's predictions to the UI must implement the following methods"""

    def getPrediction() -> int:
        pass
