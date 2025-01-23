def to_roman(number):
    # Validações mais abrangentes
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    if number <= 0:
        raise ValueError("Input must be between 1 and 3999")

    roman_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    result = ''
    for value, symbol in roman_map:
        while number >= value:
            result += symbol
            number -= value
    
    return result