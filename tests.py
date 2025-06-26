from functions.run_python_file import run_python_file

def run_tests():
    #print("Test 1: get_file_content ('calculator', 'lorem.txt')")
    #print(get_file_content("calculator", "lorem.txt"), end="\n\n")

    #print("Test 1: get_file_content ('calculator', 'main.py')")
    #print(get_file_content("calculator", "main.py"), end="\n\n")

    #print("Test 2: get_file_content ('calculator', 'pkg/calculator.py')")
    #print(get_file_content("calculator", "pkg/calculator.py"), end="\n\n")

    #print("Test 3: get_file_content ('calculator', '/bin/cat')")
    #print(get_file_content("calculator", "/bin/cat"), end="\n\n")

    #print("Test 2: get_files_info('calculator', 'pkg')")
    #print(get_files_info("calculator", "pkg"), end="\n\n")

    #print("Test 3: get_files_info('calculator', '/bin')")
    #print(get_files_info("calculator", "/bin"), end="\n\n")

    #print("Test 4: get_files_info('calculator', '../')")
    #print(get_files_info("calculator", "../"), end="\n\n")

    #print("Test 1: write_file('calculator', 'lorem.txt', 'wait, this isn't lorem ipsum')")
    #print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    #print("Test 2: write_file('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')")
    #print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    #print("Test 3: write_file('calculator', '/tmp/temp.txt', 'this should not be allowed')")
    #print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

    print("Test 1: run_python_file('calculator', 'main.py')")
    print(run_python_file("calculator", "main.py"))
    
    print('Test 2: run_python_file("calculator", "tests.py")')
    print(run_python_file("calculator", "tests.py"))

    print('Test 3: run_python_file("calculator", "../main.py")')
    print(run_python_file("calculator", "../main.py")) #(this should return an error)
    
    print('Test 4: run_python_file("calculator", "nonexistent.py")')
    print(run_python_file("calculator", "nonexistent.py")) #(this should return an error)

if __name__ == "__main__":
    run_tests()