def totalCalc(billAmt,tipPerc):
    total=billAmt*(1+0.01*tipPerc)
    print("Your bill is",total,"INR.")
    return total

totalCalc(2000,10)
