def is_palindrome(str):
    str_to_list = list(str)
    for i in range(len(str_to_list) // 2):
        if str_to_list[i] != str_to_list[len(str_to_list) - i - 1]:
            return False
    return True


if __name__ == "__main__":
    print(is_palindrome("stars"))
