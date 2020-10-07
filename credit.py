def first2(a):
  listcc = list(a)
  first2char =  listcc[0] + listcc[1]
  return first2char
  
def first1(a):
  listcc = list(a)
  return listcc[0]

def falseInput(a):
  if len(a) == 13 or len(a) == 15 or len(a) == 16:
    try:
      int(a)
      return False
    except:
      return True
  else:
    return True

def checkCard(a):
  if int(first2(a)) == 34 or first2(a) == 37:
    print("American Express")
  elif int(first2(a)) >= 51 and first2(a) <= 55:
    print("MasterCard")
  elif int(first1(a)) == 4:
    print("Visa")
  else:
    print("This does not belong to American Express, MasterCard, or Visa")

def validCard(cc):
  cc_str = str(cc)
  index = len(cc_str)
  sum = 0
  for num in cc_str:
    if (index % 2 == 0):
      mult_by_2 = 2*int(num)
      if mult_by_2 > 9:
        dig1 = str(mult_by_2)[0]
        dig2 = str(mult_by_2)[1]
        sum += int(dig1) + int(dig2)
      else:
        sum += mult_by_2
    elif (index % 2 == 1):
      sum += int(num)
    index -= 1
  lastindexsum = len(str(sum)) - 1
  lastdig = (str(sum)[lastindexsum])
  if lastdig == "0":
    return True
  else:
    return False



ccnumber = str(input("Credit card number: "))
check = falseInput(ccnumber)
while check == True:
  ccnumber = str(input("Credit card number: "))
  check = falseInput(ccnumber)
checkCard(ccnumber)
if validCard(ccnumber) == True:
  print("This is a valid credit card number.")
else:
  print("This is not a valid credit card number.")