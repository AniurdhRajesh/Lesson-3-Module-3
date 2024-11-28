frequency_dict = {'Codingal': 2, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

def check_frequency(value, freq_dict):
    count = list(freq_dict.values()).count(value)
    return count

value_to_check = 2
frequency_count = check_frequency(value_to_check, frequency_dict)

print(f"The frequency of the value '{value_to_check}' in the dictionary is: {frequency_count}")
