def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return total / 5

def calculate_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "F"