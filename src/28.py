def calculate_expression(expression):
    try:
        result = eval(expression)
        print("The result is:", result)
    except Exception as e:
        print("An error occurred:", e)

expression = "3 + 5 * 2"
calculate_expression(expression)
