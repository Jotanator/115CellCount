import modelOutputInterface as mOI


class TestModelOutputHandler(mOI.ModelOutputHandlerInterface):
    """Extract text from an email."""

    def getPrediction(self):
        return 5
