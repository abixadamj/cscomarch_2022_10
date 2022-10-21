# wczytujemy niezbędne elementy
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from functions.nbp import Nbp_table
from functions.md_create import markdown_doc
from functions.doc_create import md_to_docx


# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Wybierz nr tabeli (A|B|C"), sg.Combo(["A", "B", "C"], default_value="A"), ],
    [sg.Text("Podaj kod Waluty (np.CHF)"), sg.InputText(), ],
    [sg.Text("Podaj  datę początkową (RRRR-MM-DD)"), sg.InputText(), ],
    [sg.Button("NBP"), sg.Exit(), ],
]
window = sg.Window("NBP Tablice", app_layout)
# używamy pętli nieskończonej, która działa aż do słowa kluczowego `break`
# pamiętajmy o PEP-8, wcięciach i bloku kodu - https://www.python.org/dev/peps/pep-0008/#indentation
while True:
    # poniższe wywołanie otwiera okno i wczytuje dane
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        print("Hard EXIT")
        break

    if event == "NBP":
        table, currency, date_from = values[0], values[1], values[2]
        nbp = Nbp_table(table, currency)
        nbp.get_table()
        nbp.show_currency()
        history_y = nbp.history_currency(date_from)
        if history_y is False:
            sg.popup(f"Error - {nbp.error_text}")
            break

        history_x = [x for x in range(len(history_y))]
        title = f"Historia waluty {currency} od dnia {date_from} do dzisiaj."
        plt.plot(history_x, history_y, marker="+", color="red", label=f"Kolejne wartości {currency}.")
        plt.grid()
        plt.legend()
        # tu tworzymy Markdown
        output_file = f"output/{currency}"
        image_file = f"{output_file}.png"
        plt.savefig(image_file)
        markdown_doc(output_file, currency, nbp.kurs, nbp.nbp_table_no, image_file)
        md_to_docx(output_file + ".md")

    # sprawdzamy wartości zwracane przez okno
    # sg.popup("Evnt is:", event, "Returned dict is:", values)


# koniec programu
window.close()
print("End of application")
