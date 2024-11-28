dict={"number":2,"Age":12,"Name":"Anirudh","num1":2,"num2":42}
def check_frequency(value,dict):
    count = list(dict.values()).count(value)
    print(count)
check_frequency(2,dict)