from name_function import get_formatted_name
while True:
    first=input("\nPlease give me a first name:")
    if first=='q':
        break
    last=input("Please give me a last name")
    if last=="q":
        break
    formated_name=get_formatted_name(first,last)
    print("\tNeatly formatted name: " + formated_name)

