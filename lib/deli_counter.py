katz_deli =[]

def line(katz_deli):
    length = len(katz_deli)
    string = "The line is currently:"
    if length > 0:
        for n in range(0,length):
            string += f" {n+1}. {katz_deli[n]}"
    else:
        string = "The line is currently empty."
    print(string)

def take_a_number(katz_deli, new_name):
    katz_deli.append(new_name)
    print(f"Welcome, {new_name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del(katz_deli[0])
    