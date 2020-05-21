#!/usr/local/bin/python3.7
from helpers import extract_upper, extract_lower

name="Jagadish Uddandam"
print(f"__name__ value in mynew_script.py: {__name__}")

print(f"uppercase letters are: {extract_upper(name)}")
print(f"lowercase letters are: {extract_lower(name)}")
