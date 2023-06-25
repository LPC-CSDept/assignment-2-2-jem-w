def main():

    celsius = int(input('Enter temperature in Celsius: '))
    fahrenheit = (9/5) * (celsius) + 32

    print (f'Fahrenheit: \t {fahrenheit:.2f}')
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
