def filter_words(st):
    return " ".join(st.capitalize().split())

st1 = input("Input the string with CAPS: ")
print (filter_words(st1))
