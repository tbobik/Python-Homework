#################################################################
# CS 21A Programming in Python Lab #3
#
# Constants, Float, Input, Print statements, Formated Output
# If Elif statements.
# Reveieve cost of groceries as input, check to see the
# coupon anount. Output the price of groceries and coupon amount
# 
#################################################################
# Read total amount for groceries.
COST_OF_GROCERIES = float(input("Please enter your total cost of groceries: "))

# Initialize constant variables for coupon levels and amounts.
NO_COUPON = "Sorry, you did not spend enought to recieve a coupon"
COUPON_LEVEL_1 = 8.00
COUPON_LEVEL_2 = 10.00
COUPON_LEVEL_3 = 12.00
COUPON_LEVEL_4 = 14.00
CONVERT_TO_PERCENT = 100.00

# Determine the coupon rate.
if COST_OF_GROCERIES >= 210 :
  couponLevel = COUPON_LEVEL_4
elif COST_OF_GROCERIES < 210 and COST_OF_GROCERIES >= 150 :
  couponLevel = COUPON_LEVEL_3
elif COST_OF_GROCERIES < 150 and COST_OF_GROCERIES >= 60 :
  couponLevel = COUPON_LEVEL_2
elif COST_OF_GROCERIES < 60 and COST_OF_GROCERIES >= 10 :
  couponLevel = COUPON_LEVEL_1
else :
  couponLevel = NO_COUPON

# Compute and print the coupon amount.
if couponLevel == NO_COUPON :
  print (NO_COUPON)
else: 
  couponAmount = (COST_OF_GROCERIES * (couponLevel / CONVERT_TO_PERCENT))
  print ("You win a discount coupon of $%.2f. (%d%% of your purchase)" % \
      (couponAmount, couponLevel))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Please enter your total cost of groceries: 320.21
# You win a discount coupon of $44.83 (14% of your purchase)
#
# Please enter your total cost of groceries: 160.45
# You win a discount coupon of $19.25. (12% of your purchase)
#
# Please enter your total cost of groceries: 101.32
# You win a discount coupon of $10.13. (10% of your purchase)
#
# Please enter your total cost of groceries: 50.25
# You win a discount coupon of $4.02. (8% of your purchase)
#
# Please enter your total cost of groceries: 5
# Sorry, you did not spend enought to recieve a coupon
##################################################################
