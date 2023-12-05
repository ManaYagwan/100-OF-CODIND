print("welcome to tip calculator ")
bill = int(input("what is ur total bill "))
tip = int(input("what percent of tip u giving "))
ppl = int(input("spliting  d bill between ? "))
bill_tip = tip / 100 * bill + bill
print(bill_tip)