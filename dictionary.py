def main():
    my_dict = {
        "Bristy" : "Hyderabad",
        "Trishna" : "Dhaka",
        "Tonmoy" : "Feni"
    }
    for( key, value) in my_dict.items():
        print(key, ":", value)
    for key in my_dict:
        print(my_dict[key])
main()