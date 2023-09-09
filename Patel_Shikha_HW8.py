#Author: Shikha Patel 
#Homework Number & Name: Homework 8 Return on Investment
#Due Date: Thursday by 11:59pm
#Program Description: The application  helps determine the return on investment (ROI) for several projects. 
 
#import both classes
import validation 
import calculation 

def main(): 
    
    #request the input in your main, the validation class will be used to validate if the input received is valid.
    validate = validation.ValidationClass()
    initial = input("What is the initial value? ")
    checkInitial = validate.checkFloat(initial)
    while checkInitial == False:
        print("Invalid initial value, please enter a float.")
        initial = input("What is the initial value? ")
        checkInitial = validate.checkFloat(initial)
        
    current = input("What is the current value? ")
    checkCurrent = validate.checkFloat(current)
    while checkCurrent == False:
        print("Invalid current value, please enter a float.")
        current = input("What is the current value? ")
        checkCurrent = validate.checkFloat(current)
        
        
    
    #Use the CalculationClass to display the ROI to the user as a percentage, with 2 decimal places
    ROIcalc = calculation.CalculationClass(float(initial), float(current))
    ROIvalue = ROIcalc.calcROI()
    print("The ROI for this investment is ", format(ROIvalue, ".2f"), "%", sep = "")
    
main()

