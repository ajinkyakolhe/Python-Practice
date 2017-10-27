# First you define a class which might or might not have an object as an argument
class Restaurant(object):

    # Take some variable which defines the behavior of the output and assign it a default binary value
    bankrupt = False
    # For modularity, define a method within the class
    def open_branch(self):
        # Check conditional statements.
        # In this case, self is used to refer to some variable which is part of the class.
        ## The below code will not work without the self keyword.
        if not self.bankrupt:
            print("branch opened")

# Define the main function
def main():
    # Instantiate the class here using some variable
    r = Restaurant()
    # Call the methods defined within the class with the help of the variables defined.
    r.open_branch()

# Call the main function.
if __name__ == '__main__':
    main()

'''
Things which are necessarily to be done in any program containing the class, in that order:
Declare a class name
Declare a method within the class
Define a main method
Instantiate the class and call methods from inside it
Call the main method
'''