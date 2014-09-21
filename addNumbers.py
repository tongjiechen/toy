#!/usr/bin/env python

def add(numbers, delimiter=","):
    if numbers == "":
       return 0
    else :
       return sum(map(lambda x: int(x), numbers.split(",")))

if __name__ == "__main__":
    
    print add("")
    print add("1")
    print add("1,2")
    print add("1,2,3,4")


