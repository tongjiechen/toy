#!/usr/bin/env python

def add(numbers, delimiter=","):
    if numbers == "":
        return 0
    else :
        if (numbers.startswith("//")):
            (delimiterline,numbers)=numbers.split("\n",2)
            delimiter = delimiterline.replace("/","")
        numbers = numbers.replace("\n",",")
        numbers_list = numbers.split(delimiter)
        negative_numbers = filter(lambda x: int(x)<0, numbers_list)
        if len(negative_numbers) > 0:
            raise RuntimeError("negatives not allowed",negative_numbers)
        return sum(map(lambda x: int(x), numbers_list))

if __name__ == "__main__":
    
    print add("")
    print add("1")
    print add("1,2")
    print add("1,2,3,4")
    print add("1\n2,3")
    print add("//;\n1;2")
    print add("-1,2,-3,4")

