class StringReverse:

    def __init__(self):
        self.__text = ""

    def getString(self):
        self.__text = input("Enter a String: ")

    def reverseString(self):
        print("Reversed String:", self.__text[::-1])

s = StringReverse()
s.getString()
s.reverseString()