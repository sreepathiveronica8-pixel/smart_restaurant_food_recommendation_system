# Smart Restaurant Food Recommendation System

## Overview

This project is a simple Smart Restaurant Food Recommendation System developed using Python. The system suggests food items to users based on their preferences such as food type (veg/non-veg), spice level, and cuisine.

It is designed to simulate how modern food apps recommend dishes, using a basic scoring and filtering approach.

---

## Features

* Takes user input for:

  * Food type (Veg / Non-Veg)
  * Spice level (Low / Medium / High)
  * Preferred cuisine
* Recommends dishes based on matching preferences
* Suggests alternative cuisines if no exact match is found
* Provides a random suggestion as a fallback
* Handles invalid inputs and errors gracefully

---

## How It Works

The system uses a simple scoring mechanism:

* Each food item is compared with user preferences
* Points are assigned for each match (type, spice level, cuisine)
* Items with higher scores are recommended

If no strong matches are found:

* The system suggests the most relevant cuisines
* A random dish is recommended to ensure output is always generated

---

## Technologies Used

* Python (Core Programming)
* Basic Data Structures (Lists, Dictionaries)
* Control Flow (Loops, Conditions)
* Exception Handling

---

## Project Structure

* `menu` → Contains food dataset
* `get_user_preferences()` → Takes and validates input
* `recommend_food()` → Core recommendation logic
* `suggest_cuisines()` → Suggests alternative cuisines
* `main()` → Runs the application

---

## How to Run

1. Make sure Python is installed on your system
2. Save the code in a file (e.g., `food_recommender.py`)
3. Open terminal or command prompt
4. Run the program:

```
python food_recommender.py
```

---

## Example Input

```
Veg or Non-Veg: veg
Spice level: medium
Cuisine: indian
```

## Example Output

```
Recommended Dishes:
- Paneer Butter Masala (indian)
- Masala Dosa (south indian)
```

---

## Future Improvements

* Add graphical user interface (GUI)
* Integrate with a database (MySQL/SQLite)
* Use machine learning algorithms for better recommendations
* Add user ratings and feedback system
* Convert into a web application using Flask or Django

---

## Conclusion

This project demonstrates how a simple recommendation system can be built using basic Python concepts. It can be further enhanced into a real-world application with advanced technologies.

---

## Author

Your Name
(You can add your college name and course here)
