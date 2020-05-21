def extract_lower(phrase):
    return(list(filter(lambda n: n.islower(),phrase)))

def extract_upper(phrase):
    return(list(filter(lambda n: n.isupper(),phrase)))

print(f"__name__ value in helpers.py: {__name__}")
