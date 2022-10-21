# Gosia

def markdown_doc(filename: str, code: str, mid: float, table_no: str, image_file: str):
    import snakemd
    doc = snakemd.new_doc(filename)
    doc.add_header("Kurs Waluty z dnia.")
    doc.add_horizontal_rule()
    doc.add_paragraph(f"Tablica nr: {table_no}")
    doc.add_horizontal_rule()
    doc.add_code(f"Wartość kursu: {mid}")
    doc.add_horizontal_rule()
    doc.add_element(snakemd.Paragraph([snakemd.InlineText("Wykres", url=image_file, image=True)]))
    doc.output_page()

