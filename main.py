import threading
import time

def Parallel_MDAS(expression):
    print()
    start_time = time.time()
    result = eval(expression)
    end_time = time.time()
    print("Parallel MDAS result:", result)
    return end_time - start_time

def Sequential_MDAS(expression):
    print()
    start_time = time.time()
    # Split the expression into individual components (numbers and operators)
    components = expression.split()

    # Initialize result with the first number
    result = float(components[0])

    # Iterate over the components starting from index 1
    for i in range(1, len(components), 2):
        operator = components[i]
        operand = float(components[i + 1])

        # Perform the operation based on the operator
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == 'x' or operator == '*':
            result *= operand
        elif operator == '/':
            # Avoid division by zero
            if operand != 0:
                result /= operand
            else:
                print("Error: Division by zero!")
                return None
        else:
            print("Error: Invalid operator!")
            return None

    end_time = time.time()
    print("Sequential MDAS result:", result)
    print("Sequential execution time:", end_time - start_time, "seconds")
    print()
    return end_time - start_time

# Function to run Parallel_MDAS in a separate thread
def run_parallel(expression):
    start_time = time.time()
    t = threading.Thread(target=Parallel_MDAS, args=(expression,))
    t.start()
    t.join()
    end_time = time.time()
    print("Parallel execution time:", end_time - start_time, "seconds")
    return end_time - start_time

# Test the functions
expression = input("Input mathematical expression: ")

# Run Parallel_MDAS in a separate thread
parallel_time = run_parallel(expression)
# Run Sequential_MDAS in the main thread
sequential_time = Sequential_MDAS(expression)
print()

# Results
print("Results:")
print("Execution time for parallel MDAS:", parallel_time, "seconds")
print("Execution time for sequential MDAS:", sequential_time, "seconds")
print()
print()
print("The difference in execution time between parallel and sequential MDAS:", sequential_time - parallel_time, "seconds")
print()
