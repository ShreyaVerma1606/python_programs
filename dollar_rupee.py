r=84.03
amt=float(input("Enter the amount:"))
type=input("Enter the type you want to convert in- dollars_to_rupees or rupees_to_dollars:")
if type == 'dollars_to_rupees':
  conv=amt*r
  print("Converted amount:",conv)
elif type == 'rupees_to_dollars':
   conv=amt/r
   print("Converted amount:",conv)
else:
   print("Invalid type entered")


    


