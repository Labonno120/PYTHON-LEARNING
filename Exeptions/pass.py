#user ke inform korbo na je kono error hoise. just abar input nibo.
def main():
    x = get_int("Whats X?")
    print(x)
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()