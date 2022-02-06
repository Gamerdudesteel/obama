answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

print("""
It's time to order a oizza!

You are hungry for pizza! Gather the courage to pick up the phone and do it!

Are you ready to order the pizza? (Yes / No)
""")

ans1 = input(">>")

if ans1 in answer_yes:
    print("\n You pick up the phone and dial the number to the pizza place. Jimmy's Pizza. This is Jimmy speaking. Would you like to place an order? (Yes / No)\n")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("\nYou order a pizza and it is delivered to your house. You Won!")

    elif ans2 in answer_no:
        print("\nThen why did you call? I dont have time for pranks *click. GAME OVER")

    else:
        print("\n Can you repeat that? I don't understand.*start over")

elif ans1 in answer_no:
    print("\nDon't be such a wimp. Are you hungry or not? (Yes / No)\n")

    ans3 = input(">>")

    if ans3 in answer_yes:
        print("\nWell in that case, you'll have to start over!")

    elif ans3 in answer_no:
        print("\nLooks like you don't need to order a pizza after all. GAME OVER")

    else:
        print("\nMommy, make the bad typing go away!")

else:
    print("\nError! Invalid command!")