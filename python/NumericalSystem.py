

class NumericalSystem:
    def convert_character_to_decimal(self, value: str) -> list[int]:
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

    def convert_decimal_to_hexadecimal(self, value: int):
        """
            Convert the decimal value to hexadecimal and return it as a string\n
            :param value as integer: The decimal value to be converted
            :return: The hexadecimal representation of the decimal value as a string
        """
        hexadecimal = hex(int(value))[2:]
        return hexadecimal

    def convert_hexadecimal_to_decimal(self, value: str | int) -> int:
        """
            Convert the hexadecimal value to decimal and return it as an integer\n
            :param value as string or integer: The hexadecimal value to be converted
            :return: The decimal representation of the hexadecimal value as an integer
        """
        return int(str(value), 16)

    def convert_binary_to_hexadecimal(self, value: str) -> str:
        """
            Convert binary values to hexadecimal and return them as a string\n
            :param value as string: The binary values to be converted
            :return: The hexadecimal representation of the binary values as a string
        """
        hexadecimal = hex(int(value, 2))[2:]
        return hexadecimal

    def convert_hexadecimal_to_binary(self, value: str) -> str:
        """
            Convert hexadecimal values to binary and return them as a string\n
            :param value as string: The hexadecimal values to be converted
            :return: The binary representation of the hexadecimal values as a string
        """
        binary = bin(int(value, 16))[2:]
        return binary

    def convert_hexadecimal_to_text(self, value: str) -> str:
        """
        Convert hexadecimal values to text and return them as a string.
        
        :param value: The hexadecimal values to be converted, with each byte separated by spaces.
        :return: The text representation of the hexadecimal values as a string.
        """
        # Remove any spaces from the input
        value = value.replace(' ', '')

        # Initialize an empty string to hold the ASCII text
        ascii_text = ''

        # Iterate through the hex string in byte-sized chunks
        for i in range(0, len(value), 2):
            # Extract the hex pair
            hex_pair = value[i:i+2]
            # Convert the hex pair to an integer
            decimal_value = int(hex_pair, 16)
            # Convert the decimal value to a character and append to the result string
            ascii_text += chr(decimal_value)

        return ascii_text
    def convert_text_to_hexadecimal(self, text: str) -> str:
        """
        Convert text to hexadecimal values and return them as a string.
        
        :param text: The text to be converted.
        :return: The hexadecimal representation of the text as a string, with each byte separated by spaces.
        """
        # Convert each character to its ASCII value, then to a two-digit hexadecimal string
        hex_string = ' '.join(f'{ord(char):02X}' for char in text)
        
        return hex_string

def main():
    print("Staring up...")
    numerical_system = NumericalSystem()
    print(numerical_system.convert_decimal_to_hexadecimal(220))
    print(numerical_system.convert_binary_to_text(
        "01000111 01101111 01101111 01100100 00100000 01001010 01101111 01100010"))
    print(numerical_system.convert_binary_to_text(
        "01000111 01101111 01101111 01100100 00100000 01001010 01101111 01100010"))
    print(len("ceafc89b3ce24fd225b04a655c42c772"))
    print(numerical_system.convert_hexadecimal_to_text("48 6F 6C 61 21"))
    print(numerical_system.convert_text_to_hexadecimal("Hola!"))
    print(numerical_system.convert_text_to_hexadecimal("Nice Work :)"))
    print(numerical_system.convert_hexadecimal_to_binary("DA"))
    print(numerical_system.convert_binary_to_decimal("11011010"))
    print(numerical_system.convert_hexadecimal_to_text("57 65 6C 6C 20 44 6F 6E 65"))
    print(numerical_system.convert_binary_to_text("01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01110100 01101001 01101110 01111001 01110101 01110010 01101100 00101110 01100011 01101111 01101101 00101111 01110011 01101000 01101111 01110010 01110100 01101101 01100101 01101001 01100011"))
    pass


if __name__ == "__main__":
    main()
