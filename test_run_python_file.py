from functions.run_python_file import run_python_file

def main():
    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py"),
        ("calculator", "lorem.txt"),
    ]
    
    for test in test_cases:
        result = run_python_file(*test)  # *test unpacks the tuple
        print(result)
        print("-" * 50)  # separator

if __name__ == "__main__":
    main()