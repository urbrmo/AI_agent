from functions.get_file_content import get_file_content

def run_tests():
    #print("Test 1: get_file_content ('calculator', 'lorem.txt')")
    #print(get_file_content("calculator", "lorem.txt"), end="\n\n")

    print("Test 1: get_file_content ('calculator', 'main.py')")
    print(get_file_content("calculator", "main.py"), end="\n\n")

    print("Test 2: get_file_content ('calculator', 'pkg/calculator.py')")
    print(get_file_content("calculator", "pkg/calculator.py"), end="\n\n")

    print("Test 3: get_file_content ('calculator', '/bin/cat')")
    print(get_file_content("calculator", "/bin/cat"), end="\n\n")

    #print("Test 2: get_files_info('calculator', 'pkg')")
    #print(get_files_info("calculator", "pkg"), end="\n\n")

    #print("Test 3: get_files_info('calculator', '/bin')")
    #print(get_files_info("calculator", "/bin"), end="\n\n")

    #print("Test 4: get_files_info('calculator', '../')")
    #print(get_files_info("calculator", "../"), end="\n\n")

if __name__ == "__main__":
    run_tests()