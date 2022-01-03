import os;

# Chinese Remainder Algorithm
def chinese_remainder():
    clear();
    

def clear():
    os.system("cls");

def get_algorithm_type():
    valid_inputs = ["1", "2", "3", "4", "5"];
    algorithm_type = input("Which algorithm you want to use from the following algorithms:\n"
                          "(1) sieve of Eratosthenes algorithm.\n"
                          "(2) Trial Division algorithm for integer factorization.\n"
                          "(3) Euclidean algorithm.\n"
                          "(4) Chinese remainder algorithm.\n"
                          "(5) Miller’s test algorithm.\n"
                          "Enter the number of the algorithm(ex: 3): ").strip();
    if algorithm_type not in valid_inputs:
        print("Invalid Input\n");
        return get_algorithm_type();
    return algorithm_type


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if (get_algorithm_type() == "4"):
        chinese_remainder()
