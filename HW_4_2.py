def enough(cap, on, wait):
    return(on + wait - cap if on + wait >= cap else 0)

#print(enough(100, 60, 50))
#print(enough(10, 5, 5))
