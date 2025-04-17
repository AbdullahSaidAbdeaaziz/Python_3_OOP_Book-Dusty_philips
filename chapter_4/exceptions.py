class EvenOnly(list):
    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('Value should be integer.')
        
        if value % 2:
            raise ValueError('Value should be even integer.')
        
        super().append(value)


def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"



def check_even(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError('Value is not Integer.')
    
    if value % 2:
        raise ValueError('Value is odd.')
    
    return True


def main():
    # auto = "1"
    # try:
    #     result = check_even(auto)
    #     print("Even" if result else "UNdefiend")
    # except (TypeError, ValueError):
    #     print('Occured has happened')
    pass



if __name__ == '__main__':
    # even = EvenOnly()
    # # even.append('string')
    # # even.append(1)
    # even.append(2)
    
    # print(even)
    # no_return()
    main()