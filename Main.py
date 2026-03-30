import random

# -------------------------------
# Sample Food Menu Dataset
# -------------------------------
menu = [
    {"name": "Paneer Butter Masala", "type": "veg", "spice": "medium", "cuisine": "indian"},
    {"name": "Chicken Biryani", "type": "non-veg", "spice": "high", "cuisine": "indian"},
    {"name": "Veg Fried Rice", "type": "veg", "spice": "low", "cuisine": "chinese"},
    {"name": "Chilli Chicken", "type": "non-veg", "spice": "high", "cuisine": "chinese"},
    {"name": "Margherita Pizza", "type": "veg", "spice": "low", "cuisine": "italian"},
    {"name": "Pepperoni Pizza", "type": "non-veg", "spice": "medium", "cuisine": "italian"},
    {"name": "Masala Dosa", "type": "veg", "spice": "medium", "cuisine": "south indian"},
    {"name": "Butter Chicken", "type": "non-veg", "spice": "medium", "cuisine": "indian"}
]

# -------------------------------
# Utility Functions
# -------------------------------
def normalize_input(user_input):
    """Clean and normalize user input"""
    return user_input.strip().lower()


def get_unique_values(key):
    """Extract unique values from menu (like cuisines)"""
    return sorted(list({item[key] for item in menu}))


# -------------------------------
# Get user preferences safely
# -------------------------------
def get_user_preferences():
    print("Welcome to the Smart Food Recommender\n")

    valid_types = ["veg", "non-veg"]
    valid_spice = ["low", "medium", "high"]
    valid_cuisines = get_unique_values("cuisine")

    # Food type
    while True:
        food_type = normalize_input(input("Veg or Non-Veg: "))
        if food_type in valid_types:
            break
        print("Invalid input. Choose from:", valid_types)

    # Spice level
    while True:
        spice_level = normalize_input(input("Spice level (low/medium/high): "))
        if spice_level in valid_spice:
            break
        print("Invalid input. Choose from:", valid_spice)

    # Cuisine (optional flexibility)
    print("Available cuisines:", ", ".join(valid_cuisines))
    cuisine = normalize_input(input("Enter cuisine (or press Enter to skip): "))

    if cuisine == "":
        cuisine = None
    elif cuisine not in valid_cuisines:
        print("Cuisine not found. Ignoring cuisine preference.")
        cuisine = None

    return food_type, spice_level, cuisine


# -------------------------------
# Recommendation Logic
# -------------------------------
def recommend_food(food_type, spice_level, cuisine):
    recommendations = []

    for item in menu:
        score = 0

        if item["type"] == food_type:
            score += 1
        if item["spice"] == spice_level:
            score += 1
        if cuisine and item["cuisine"] == cuisine:
            score += 1

        if score >= 2:
            recommendations.append((item, score))

    # Sort by best score
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return [item[0] for item in recommendations]


# -------------------------------
# Suggest alternative cuisines
# -------------------------------
def suggest_cuisines(food_type, spice_level):
    cuisine_scores = {}

    for item in menu:
        score = 0

        if item["type"] == food_type:
            score += 1
        if item["spice"] == spice_level:
            score += 1

        cuisine_scores[item["cuisine"]] = cuisine_scores.get(item["cuisine"], 0) + score

    sorted_cuisines = sorted(cuisine_scores.items(), key=lambda x: x[1], reverse=True)

    return [c[0] for c in sorted_cuisines[:3]]


# -------------------------------
# Main Program
# -------------------------------
def main():
    if not menu:
        print("Menu is empty. Cannot generate recommendations.")
        return

    try:
        food_type, spice_level, cuisine = get_user_preferences()

        results = recommend_food(food_type, spice_level, cuisine)

        print("\nRecommended Dishes:\n")

        if results:
            for item in results:
                print("-", item["name"], "(" + item["cuisine"] + ")")
        else:
            print("No strong matches found.")

            suggestions = suggest_cuisines(food_type, spice_level)

            if suggestions:
                print("\nSuggested cuisines:")
                for c in suggestions:
                    print("-", c)

            print("\nRandom suggestion:")
            random_item = random.choice(menu)
            print("-", random_item["name"], "(" + random_item["cuisine"] + ")")

    except Exception as e:
        print("An unexpected error occurred:", str(e))


# Run the program
if __name__ == "__main__":
    main()
