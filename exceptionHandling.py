try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Execution completed.")