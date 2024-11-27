print("""
Molimo, odradite i sljedeće korake:
    - Analizirajte datoteke unutar docs direktorija i potražite TODO oznake.
    - Ispunite docs/development.md datoteku""")

if '%{{cookiecutter.database}}%' == "Y":
    print("""    - Naveli ste potrebu za bazama podataka. Popunite koje vrste su vam potrebne u poglavlju "Zahtjevi za resurse".
    """)