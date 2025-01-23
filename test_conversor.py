import pytest
from conversor import to_roman

def test_to_roman_valores_unicos():
    casos = [
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M")
    ]
    for numero, romano in casos:
        assert to_roman(numero) == romano

def test_to_roman_combinacoes():
    casos = [
        (4, "IV"),
        (9, "IX"),
        (14, "XIV"),
        (23, "XXIII"),
        (40, "XL"),
        (49, "XLIX"),
        (90, "XC"),
        (99, "XCIX"),
        (400, "CD"),
        (444, "CDXLIV"),
        (900, "CM"),
        (999, "CMXCIX"),
        (1987, "MCMLXXXVII"),
        (2023, "MMXXIII"),
        (3549, "MMMDXLIX"),
        (3999, "MMMCMXCIX")
    ]
    for numero, romano in casos:
        assert to_roman(numero) == romano

def test_to_roman_invalid_input():
    casos_invalidos = [
        0,      # Zero
        -1,     # Negativo
        3.14,   # Ponto flutuante
        "texto" # Não inteiro
    ]
    for entrada in casos_invalidos:
        with pytest.raises(ValueError):
            to_roman(entrada)

def test_to_roman_limites():
    assert to_roman(1) == "I"
    assert to_roman(3999) == "MMMCMXCIX"
