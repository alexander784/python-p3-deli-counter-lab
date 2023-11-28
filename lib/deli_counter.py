
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    return f"Welcome, {name}. Ypu are number {len(katz_deli)} in line."

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving = katz_deli.pop(0)
        print(f"Currently serving {serving}.")