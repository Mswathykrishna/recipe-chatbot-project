


recipes = {
    "poha": [
        "Ingredients: Poha, onion, mustard seeds, curry leaves, turmeric, lemon.",
        "Steps: Rinse poha, sauté onion with spices, add poha, mix, add lemon."
    ],
    "banana smoothie": [
        "Ingredients: Bananas, milk, honey, cinnamon.",
        "Steps: Blend everything and serve chilled."
    ],
    "chicken curry": [
        "Ingredients: Chicken, onion, tomato, ginger garlic paste, curry powder.",
        "Steps: Sauté onion, add tomato & spices, cook chicken for 25 mins."
    ]
}
 
def recipe_chat():
    print("👩‍🍳 Hi! I'm your Recipe Bot.")
    while True:
        ask = input("Type a recipe name (or 'exit'): ").lower()
        if ask == "exit":
            print("Bye! 👋")
            break
        elif ask in recipes:
            print("\n📝 " + recipes[ask][0])
            print("👨‍🍳 " + recipes[ask][1])
        else:
            print("Recipe not found. Try another.")
 
recipe_chat()






