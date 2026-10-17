def main():
    my_dict = [{
        "Name" : "Bristy",
        "City" : "Hyderabad",
        "Marital Status" : "Single"
    },
    {
        "Name" : "Trishna",
        "City" : "Dhaka",
        "Marital Status" : "Married"
    },
    {
        "Name" : "Tonmoy",
        "City" : "Feni",
        "Marital Status" : "Married"
    },]
    for person in my_dict:
        for key, value in person.items():
            print(key, ":", value)
    for person in my_dict:
        print(person["Name"], person["City"], person["Marital Status"], sep = ", ")
main()