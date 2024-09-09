

class NumericalSystem:
    def convert_character_to_ascii_decimal(self, value: str) -> list[int]:
        """
            Convert the character to ASCII decimal and return a list of these values\n
            :param value as string: The character to be converted
            :return: A list of ASCII decimal values of the character
        """
        ascii_decimal = [ord(char) for char in value]
        return ascii_decimal
    
    def convert_text_to_binary(self, value: str) -> list[str]:
        """
            Convert the text to binary and return a list of these values\n
            :param value as string: The text to be converted
            :return: A list of binary representations of the characters
        """
        binary = ' '.join(format(ord(char), '08b') for char in value)
        return binary

    def convert_decimal_to_binary(self, decimal: int) -> str:
        """
            Convert the decimal value to binary and return it as a string\n
            :param value as string: The decimal value to be converted
            :return: The binary representation of the decimal value as a string
        """
        binary = bin(int(decimal))[2:]
        return binary

    def convert_binary_to_decimal(self, value: str | list[int]) -> int:
        """
            Convert the binary value to ASCII decimal and return it as an integer\n
            :param value as string or list of integer: The binary value(s) to be converted
            :return: The ASCII decimal value(s) as an integer
        """
        if isinstance(value, str):
            value = list(map(int, value))
        decimal = 0
        for digit in value:
            decimal = decimal * 2 + digit
        return decimal

    def convert_binary_to_text(self, value: str):
        """
            Convert binary values to text and return them as a string\n
            :param value as string: The binary values to be converted
            :return: The text representation of the binary values as a string
        """
        ascii_text = ''.join(chr(int(binary, 2))
                             for binary in value.split(' '))
        return ascii_text

    def convert_char_to_decimal(self, value: str) -> int:
        """
            Convert the character to decimal and return it as an integer\n
            :param value as string: The character to be converted
            :return: The decimal representation of the character as an integer
        """
        return ord(value)

    pass


def main():
    test: str = "Cy8er"
    ns = NumericalSystem()
    decimals = ns.convert_character_to_ascii_decimal(value=test)
    for index, decimal in enumerate(decimals):
        binary = ns.convert_decimal_to_binary(decimal=decimal)
        print(f"Character: {test[index]}, Decimal: {decimal}, Binary: {binary}")

    binary_value = "01001111 01010011 01001001 01001110 01010100"
    test = "01000011 01111001 00111000 01100101 01110010"

    print(1, ns.convert_text_to_binary(value="Cy8er"))
    print(2, ns.convert_binary_to_text(value=binary_value))
    print(3, ns.convert_char_to_decimal(value="a"))
    print(4, ns.convert_binary_to_decimal(value="00001000"))
    print(5, ns.convert_decimal_to_binary(199))
    print(6, ns.convert_decimal_to_binary(222))
    print(7, ns.convert_binary_to_decimal(value="00101110"))
    print(8, ns.convert_binary_to_decimal(value="11111111"))
    print(9, ns.convert_char_to_decimal(value="#"))
    print(10, ns.convert_decimal_to_binary(25))
    print(11, ns.convert_binary_to_decimal(value="1010101010"))
    print(12, ns.convert_char_to_decimal(value="%"))
    print(13, ns.convert_binary_to_decimal(value="1101"))
    print(14, ns.convert_char_to_decimal(value=" "))
    print(15, ns.convert_decimal_to_binary(160))
    print(16, ns.convert_decimal_to_binary(100))
    print(17, ns.convert_char_to_decimal(value="0"))
    print(18, ns.convert_char_to_decimal(value="Q"))
    print(19, ns.convert_binary_to_decimal(value="101"))
    print(20, ns.convert_char_to_decimal(value="@"))



    print(ns.convert_decimal_to_binary(27))
    print(ns.convert_decimal_to_binary(89))
    print(ns.convert_decimal_to_binary(53))
    print(ns.convert_binary_to_text("01110011"))
    print(ns.convert_binary_to_text("01010111 01100101 01101100 01101100 00100000 01000100 01101111 01101110 01100101"))
    
    print(ns.convert_decimal_to_binary(55))


    print(ns.convert_binary_to_text("01001011 01101110 01101111 01110111 01101100"))
    print(ns.convert_char_to_decimal("Z"))
    print(ns.convert_binary_to_decimal("10101010"))
    print(ns.convert_decimal_to_binary(157))
    print(ns.convert_decimal_to_binary("64"))
    print(ns.convert_binary_to_decimal("10011010"))
    print(ns.convert_binary_to_decimal("00011100"))
    print(ns.convert_char_to_decimal("!"))
    print(ns.convert_binary_to_text("01010110 01101001 01110011 01101001 01101111"))
    print(ns.convert_char_to_decimal("x"))
    print(ns.convert_binary_to_decimal("01010101"))
    print(ns.convert_decimal_to_binary(76))
    print(ns.convert_decimal_to_binary(51))
    print(ns.convert_binary_to_decimal("00110101"))
    print(ns.convert_binary_to_decimal("11010001"))
    print(ns.convert_char_to_decimal("|"))
    print(ns.convert_text_to_binary("Hello World"))
    print(ns.convert_binary_to_decimal("00000001"))
    print(ns.convert_decimal_to_binary(128))
    print(ns.convert_char_to_decimal("B"))
if __name__ == '__main__':
    main()
