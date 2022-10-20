import snakemd

from functions.nbp import Nbp_table
import snakemd

class MarkdownDoc:

    def __init__(self, filename: str, code: str, table: str = "A"):
        self.file: str = filename
        self.code: str = code
        self.mid: float = 0
        self.doc = snakemd.new_doc(self.file)

