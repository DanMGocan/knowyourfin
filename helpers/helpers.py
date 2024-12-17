def calculate_calories(age, gender):
    """
    Estimate daily calorie needs based on age and gender.

    Args:
    age (float): Age in years.
    gender (str): Gender ('male' or 'female').

    Returns:
    float: Estimated daily calorie requirement.
    """
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120 years.")
    if gender not in ['male', 'female']:
        raise ValueError("Gender must be 'male' or 'female'.")

    # Calorie estimation for infants and children (gender-neutral)
    if age <= 1:
        return 800 + (age * 400)  # Infancy: ~800–1200 kcal
    elif age <= 9:
        return 1200 + (age - 1) * 100  # Childhood: ~1200–2000 kcal

    # Calorie estimation for adolescents (gender-specific)
    if 9 < age <= 18:
        if gender == 'male':
            return 2000 + (age - 9) * 120  # Boys: ~2000–3080 kcal
        elif gender == 'female':
            return 1900 + (age - 9) * 100  # Girls: ~1900–2800 kcal

    # Calorie estimation for adults
    if age > 18:
        if gender == 'male':
            return 2500  # Standard for adult males
        elif gender == 'female':
            return 2000  # Standard for adult females

