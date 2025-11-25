# Skincare-Haircare-Advisor
Skincare-Haircare advisor is wholely  a python based program , simply coded and easy to use . This program helps you find some best skincare and haircare fits for yourself with or without having a knowledge in this field . It also provides a quick guide to enter the world of Skincare and haircare .

# OVERVIEW 
SKincare - Haircare advisor is a program that is wholely coded in python , thus designed for python enthusiasts ; aslo its central theme which includes skincare and haircare element makes it a topic of interest for people of almost every age group in present day . Nowadays, either everone has a specific skin care routine or looks for a perfect routine , one which is appropriate for their skin , fits in their budget and has long lasting impacts on their skin . This brings in the role of this program that would actively help users find the skincare routine best suited for them and also give quick and meaningful suggestions to those who already are into skincare from a long time .
BY selecting a skintype and confirming your budget , the program lets you know:-
(i) The necessary active ingredients that your products should contain according to your skin type 
(ii) The products best suited for your skin , within your budget 
(iii) Home remedies that could be beneficial for your skin 
(iv) Some good diet tips accordingly 
Everything is stored in simple dictionaries (ingredients_db, product_db, home_remedies_db), making it easy to update or expand.


# FEATURES 
(1).Lets you discover your skintype 
   It asks simple and basic questions regarding your skin 
   With the help of these questions , it determines your skintype which most people are confused about initially 

(2).Gives you personalised suggestions for skincare and haircare 
    When the user selects their skin type, the app recommends:
    Actives like Salicylic Acid, 
                 Niacinamide 
                 Hyaluronic Acid 
                 Vitamin C 
                 Ceramides, etc.
                 Products from trusted brands (Dermatouch, Minimalist, Dot & Key, The Derma Co., Cetaphil, Hyphen, etc.)
                 Product suggestions that fit in the budget of the user 

(3).Has an efficient Product Database
     It hasa structured Python dictionary storing the Product names, price , Categorization by skin type
     This database is quite efficient and customizable at the same time , therefore can be updated frequently 

(4). Has an Ingredient Knowledge Base
       It Explains which actives are suitable for different skin types
       This helps users understand why products are recommended and gives them a knowledge of active ingredients and their roles for different skin type 

(5). Provides Home Remedies
      It gives Simple, safe DIY suggestions for each skin type using ingredients like:
        Aloe vera
        Honey
        Multani mitti
        Cucumber etc. 

(6). Has a Beginner-Friendly Code
        No external libraries, therefore easy to read, easy to modify.


# Project Strcucture 
  skincare-haircare-advisor/
│
│── database/
│     ├── product_db.py
│     ├── ingredients_db.py
│     ├── remedies_db.py
│
│── main.py
│── README.md

  Explanation:
database/ →  It contains all datasets (products, ingredients, remedies)
main.py →It contaisn the  main program that imports the database and runs the advisor
README.md → It conatins the project documentation



# Tech Stack
   Python 3.x
   No additional dependencies required

# Prerequisites
   Python should be  installed on your system (3.8+ recommended)
   A code editor like VS Code would make things easier 

# How to run the Project 
  1. Install Python
     Ensure Python 3 is installed.
     Check version :  python --version

  2. Download the project
     Clone from github : https://github.com/aditi60801/Skincare-Haircare-Advisor.git
  3. Navigate into the folder
     cd skincare-haircare-advisor
  4. Run the program
     
   
# How It Works
    User selects age , gender , experience and  skin type i.e."oily", "dry", "combination", "normal"
    Program displays  the corresponding List of actives → from ingredients_db 
                                        List of Products + prices → from product_db
                                        List of Home remedies → from home_remedies_db
   Finally the Output is neatly displayed.   

# Example Output
For Eg. You selected:-
         Female (gender)
         Adult (age group )
         Beginner (EXperience)
         Oily (Skintype)
        
        The program recommends Active Ingredients such as :-
          - Salicylic Acid (BHA)
          - Niacinamide
          - Retinoids

       The program now Recommends Products:
          1. Dermatouch Salicylic Acid Face Wash — ₹150
          2. The Derma Co. 1% Salicylic Acid Oil Free Moisturizer — ₹300
          3. Minimalist Oily Skincare Kit — ₹1067
          4. Dot & Key Anti Acne Routine Kit (Cica + Salicylic) — ₹1788

       For users who go for Home Remedies it gives home remedies :
         - Use aloe vera gel daily.
         - Apply multani mitti once or twice a week.   

# Contributing
   Any Contributions are more than welcome!
      You can add more Ingredient
                       Products
                       Skin types
                       Features  in the program and thus help us serve a larger no. of users      

        
# Acknowledgements
 An extended Thanks to the open skincare community that provided the knowledge of active ingredients , home remedies and appropriate diet tips . 
















        












     
