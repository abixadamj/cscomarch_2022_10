def markdown_doc(filename: str, code: str, mid: float, table_no: str):
    import snakemd
    doc = snakemd.new_doc(filename)
    doc.add_header("Kurs Waluty z dnia.")
    doc.add_horizontal_rule()
    doc.add_paragraph(f"Tablica nr: {table_no}")
    doc.add_horizontal_rule()
    doc.add_code(f"Wartość kursu: {mid}")
    doc.add_horizontal_rule()
    doc.output_page()



class MarkdownDoc:

    def __init__(self, filename: str, code: str, table: str = "A"):
        from functions.nbp import Nbp_table
        import snakemd
        self.file: str = filename
        self.code: str = code
        self.table: str = table
        self.mid: float = 0
        self.doc = snakemd.new_doc(self.file)
        self.nbp = Nbp_table(self.table, self.code)

        if self.nbp.get_table():
            self.mid = self.nbp.kurs
            self.doc.add_header("Kurs Waluty z dnia.")
            self.doc.add_horizontal_rule()
            self.doc.output_page()


if __name__ == "__main__":
    test_md = MarkdownDoc("pliczek", "CHF")
    markdown_doc("pliczek", "CHF", 4.345, "AAAA/Aby")

