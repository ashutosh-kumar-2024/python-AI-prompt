from my_package import C

def main():
    print("Using artifact package:")
    c_instance = C()
    result = c_instance.function_c()
    print(result)

if __name__ == "__main__":
    main()
