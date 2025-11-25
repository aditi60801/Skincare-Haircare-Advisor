# An Advisor for Skincare/Haircare/Makeup 

# Below is a small , rather a very basic database for the Program
#  this databse can be extended further 

ingredients_db = {
    "For OILY Skintype,any of these active ingredients maybe useful": ["1. Salicylic Acid (BHA)", "2. Niacinamide (Vitamin B3)" ," 3. Clay (Kaolin / Bentonite / Multani Mitti)" ," 4. Zinc" ,"5. Green Tea Extract"],
    "For DRY skintype any of these active ingredients maybe useful ": [" 1. Hyaluronic Acid", " 2. Ceramides", "3. Glycerin", "4. Shea Butter / Squalane" ,"5. Lactic Acid (Mild AHA)"],
    "For COMBINATION skintype these active  ingredients maybe useful": [" 1. Vitamin C", "2. Niacinamide","3. Hyaluronic Acid", "4. Green Tea","5. Salicylic Acid (2 percent or lower)"],
    "For NORMAL skintype these active ingredients maybe useful": ["1. Aloe Vera", " 2.Vitamin E", "3. Hyaluronic Acid" , "4. Panthenol (Vitamin B5)" , "5. Mild Exfoliants (Lactic / Mandelic Acid)"]
}

product_db = {"For oily skintype":  
              [
     
        {"name": "Dermatouch Salicylic Acid Face Wash" , "Price": 150},
        {"name": "The Derma Co. 1% Salicylic Acid Oil Free Moisturizer", "Price": 300},
        {"name":"Minimalist Oily Skincare Kit" , "Price": 1067},
        {"name":"Dot & Key Anti Acne Routine Kit (Cica + Salicylic)" , "Price":1788 } 
    ],
       

       "For dry skintype": [
        {"name":"Hyphen Lightweight Face Cream (Dry)", "price": 417},
        {"name":"Cetaphil Daily Advance Ultra Hydrating Lotion", "price": 229}
    ]

}

home_remedies = {
    "For oily Skintype ": "Use aloe vera gel. Apply multani mitti once a week.",
    "For dry Skintype ": "Use raw milk with honey added to it . Apply coconut oil lightly.",
    "For combination skintype ": "Use rose water , it acts as a toner. Apply aloe vera gel on areas which you feel oily .",
    "For normal skintype ": " Apply aloe vera gel and drink plenty of water to keep skin hydrated "
}

diet_tips = {
    "For oily skintype ": "Avoid fried food. Drink lemon water.",
    "For dry skintype ": "Drink more water. Eat nuts and seeds.",
    "For combination skintype ": "Eat fruits like oranges, berries.",
    "For normal skintype ": "Maintain balanced diet with vegetables."
}

# Below is the Code for the Program 

while True:
    print("\n--- Welcome to the Skin-Hair-Makeup Advisor. A solution to all your unheard QUERIES  ---")

    gender = input("Please select your gender (Male/Female/others): ")
    age = input("Please identify your age group (Teen/Adult/Senior): ")

    print("\n Where do you need our advice :")
    print("1. Skincare\n2. Haircare\n3. Makeup\n4. In all the above ")
    category = input("Select your concern (1/2/3/4): ")

    # Now we input if the user is at an early stage (ie. a beginner ) or just wants to find something better (ie. Somewhat experienced )
    "Exp" == input("\nAre you a Entering the world of skincare(ie. Beginner) or are an Experienced user ? ").lower()


    # If the user is a beginner 
    
    if "Exp" == "beginner":
        aware = input("\nAre you aware of your skin type? (yes/no): ").lower()

        if aware == "yes":
            skin_type = input("Please let us know your skin type (oily/dry/combination/normal): ").lower()

        else:
            print("\nAnswer these to help identify your skin type.")
            q1 = input("Do you feel your face gets oily in a short span of time after washing? (yes/no): ").lower()
            q2 = input("Does your skin have dry or flaky patches? (yes/no): ").lower()

            if q1 == "yes" and q2 == "no":
                skin_type = "oily"
            elif q1 == "no" and q2 == "yes":
                skin_type = "dry"
            else:
                skin_type = "combination"

        print("\nYour skin type is:", skin_type)

        # After recognising the skintype of the user , we suggest some active ingredients that their products must include
        print("\nSome Recommended Ingredients:")
        for ing in ingredients_db.get(skin_type, []):
            print("-", ing)

        # After suggesting ingredients we ask about the preferrd choice of the user for skincare (i.e. Products/Hone remedies etc.)
        print("\nHow do you want us to suggest you cures :")
        print("1. BY suggesting some good Products\n2. BY suggesting some Home Remedies\n3. BY Giving you Diet Tips")
        sol = input("Enter choice (1/2/3): ")

        # NOw we give Suggestion of some good products from our database 
        if sol == "1":
            budget = int(input("\nHow much money are you willing to spend ( What is your budget) (e.g. 200-500): "))
            print("\nThese products might work for your skintype and fit in your budget as well:")
            for p in product_db.get(skin_type, []):
                if p["price"] <= budget:
                    print("-", p["name"], "₹", p["price"])

        # Now we suggest some Home remedies for the users 
        elif sol == "2":
            allergy = input("Do you have any allergies (yes/no): ")
            print("\nYou can try these GHARELU NUSKHAS ( Home Remedies ) for your skintype :")
            print(home_remedies.get(skin_type, "No data."))

        # Below is the code for suggesting diet tips to the user 
        elif sol == "3":
            print("\nThese diet tips maybe beneficial for your skintype:")
            print(diet_tips.get(skin_type, "No data."))

    
    # If the user is an experienced user and is already into skincare 
    
    else:
        current = input("\nWhich product do you currently use or want to change ?: ")
        reason = input("Why do you want to change it? ")
        budget = int(input("What is your Budget : "))

        print("\nBased on your skintype and budget, here are some better suggestions for you:")
        for p in product_db.get("oily", []):  
            if p["price"] <= budget:
                print("-", p["name"], "₹", p["price"])

        print("\nYou may try these home remedies for better results:", home_remedies["normal"])
        print("These diet tips might work for your skintype :", diet_tips["normal"])

    # We give a final personalised plan to the user including all the product suggestions / home remdies he/she has been looking for 
    
    print("\n--- Your Final Personalised Routine ---")
    print("Cleanse -> Treat -> Moisturize")
    print("Follow the recommended remedies and products to see better results .")

    # Restart?
    again = input("\nDo you want to start again? (yes/no): ").lower()
    if again != "yes":
        print("\nThank you for using the advisor, we hope we were able to help you !")
        break
