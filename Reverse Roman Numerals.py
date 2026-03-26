def from_roman_numeral(roman_numeral):
    values = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    total = 0
    for i in range(len(roman_numeral)):
        # If current < next → subtract
        if i < len(roman_numeral) - 1 and values[roman_numeral[i]] < values[roman_numeral[i + 1]]:
            total -= values[roman_numeral[i]]
        else:
            total += values[roman_numeral[i]]
    return total