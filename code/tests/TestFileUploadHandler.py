import FileUploadHandlerInterface as mOI

class TestMinimalFileUploadHandler(mOI.ModelOutputHandlerInterface):
    """Select file from user's computer."""
    def uploadFile(self)->Image:
        return Image.open(filename)
       
