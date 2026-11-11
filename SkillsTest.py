# Periodic Table Information Finder

from pyscript import document

non_metals = {
    "H": ["Hydrogen", 1, 1.008],
    "He": ["Helium", 2, 4.0026],
    "C": ["Carbon", 6, 12.011],
    "N": ["Nitrogen", 7, 14.007],
    "O": ["Oxygen", 8, 15.999],
    "F": ["Fluorine", 9, 18.998],
    "Ne": ["Neon", 10, 20.180],
    "P": ["Phosphorus", 15, 30.974],
    "S": ["Sulfur", 16, 32.06],
    "Cl": ["Chlorine", 17, 35.45],
    "Ar": ["Argon", 18, 39.948],
    "Se": ["Selenium", 34, 78.971],
    "Br": ["Bromine", 35, 79.904],
    "Kr": ["Krypton", 36, 83.798],
    "I": ["Iodine", 53, 126.904],
    "Xe": ["Xenon", 54, 131.293],
    "Rn": ["Radon", 86, 222]
}


def search_element(e):
    symbol = document.getElementById("symbol").value.strip().capitalize()

    element = non_metals.get(
        symbol, ["Element does not exist in the non-metals list.", "N/A", "N/A"]
    )

    document.getElementById("output").innerHTML = f"""
    <p><b>Symbol:</b> {symbol}</p>
    <p><b>Element:</b> {element[0]}</p>
    <p><b>Atomic Number:</b> {element[1]}</p>
    <p><b>Atomic Mass:</b> {element[2]}</p>
    """