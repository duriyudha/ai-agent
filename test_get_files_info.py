from functions.get_files_info import get_files_info

def main():
    test_cases = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../"),
    ]
    
    for test in test_cases:
        result = get_files_info(*test)
        print(result)
        print("-" * 50)

if __name__ == "__main__":
    main()