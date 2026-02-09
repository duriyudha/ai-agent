from functions.get_file_content import get_file_content

def main():
    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py"),
    ]
    
    for test in test_cases:
        result = get_file_content(*test)
        print(result)
        print("-" * 50)

if __name__ == "__main__":
    main()