# In the main function I am gathering input from the user and running that input through the question() function to make sure it is an acceptable input to move forward with. 
# This will also decide if the program will be encoding or decoding a message from the users choice.
def main():
    answer = the_question()
    if answer == "encode":
        message = input("What is your message? ").lower()
        offset = int(input("What is the offset of your code? "))
        return print(caesar_encoder(message, offset))
    else:
        message = input("What is your message? ").lower()
        offset = input("What is the offset of your code, (if unknow type unknow)? ")
        if offset == "unknow":
            num_range = int(input("How many times would you like the decoder to run?: "))
            return unknow_offset(message, num_range)
        else:
            offset = int(offset)
            return print(caesar_decode(message, offset))

# This is the function that I am making sure the users input is valid before retuning it back to the main function. 
def the_question():
    while True:
        answer = input("What would you like to do encode or decode? ").lower().strip()
        if answer.isalpha() and answer == "encode":
            return answer
        elif answer.isalpha() and answer == "decode":
            return answer
        elif answer.isalpha() is False or answer != "encode" or answer != "decode":
            print("Please select either encode or decode: ")


# The encoder function takes two arguments, and returns a new string of charters after each charter in the message is offset a certain amount of times that the users decides on. 
# This code also has 2 comendted out lines on how it was created before updating it to accept any special charter. 
def caesar_encoder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # punctuation = """.,?'!" """ (this was the first set of special charters that the if statement would check before either setting a new offset or pushing to the else statement not having this sting in here allows the user to enter any special charter they chose in the message)
    translated_message = ""
    for letter in message:
        # if not letter in punctuation: (this would have confirmed that the letter it was on in the message was not in the punctuation string)
        if letter in alphabet:
            letter_value = alphabet.find(letter)
            translated_message +=  alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message

# This is just like the encoder except the translated_message will add a new offset charter that is be + on the alphabet list 
def caesar_decode(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    translated_message = ""
    for letter in message:
        if letter in alphabet:
            letter_value = alphabet.find(letter)
            translated_message +=  alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message

# The unknow_offset function is like the decoder function but if the offset is unknow from the user and that is stated in the main() function this will run the decoder lines of code a selected amount of times decided by the user with a print out of the number of times or offset number
def unknow_offset(message, num_range):
    def caesar_decode(message, offset):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        translated_message = ""
        for letter in message:
            if letter in alphabet:
                letter_value = alphabet.find(letter)
                translated_message +=  alphabet[(letter_value + offset) % 26]
            else:
                translated_message += letter
        return translated_message
    
    offset = 0

    for number in range(num_range):
        offset += 1
        print(f"{number + 1} " + caesar_decode(message, offset))


main()





