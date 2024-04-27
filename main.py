import time 
import threading
import re
    
# Function to parse and compute mathematical expressions
def compute(expression):
    # Evaluate the expression
    result = eval(expression)
    return result

# Function to parse expressions from a string
def parse_expressions(expression_string):
    # Define pattern to match expressions
    expression_pattern = r"([0-9]+(?:\.[0-9]+)?(?:\s*[\+\-\*\/]\s*[0-9]+(?:\.[0-9]+)?)+)"
    
    # Find all matches of expressions in the input string
    expressions = re.findall(expression_pattern, expression_string)
    return expressions

# Sequential execution without threading
def sequential_execution(expressions):
    start_time = time.time()
    for expression in expressions:
        compute(expression)
    end_time = time.time()
    print("Sequential execution time:", end_time - start_time)

# Parallel execution with threading
def parallel_execution(expressions):
    start_time = time.time()
    threads = []
    for expression in expressions:
        t = threading.Thread(target=compute, args=(expression,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print("Parallel execution time:", end_time - start_time)

if __name__ == "__main__":
    expression_string = input("Enter mathematical expressions (separated by spaces): ")
    expressions = parse_expressions(expression_string)
    print()
    print()
    
    # Compute and print the result of each expression
    for expression in expressions:
        result = compute(expression)
        print(f"{expression} = {result}")
    
    print()
    # Sequential execution
    sequential_execution(expressions)
    
    # Parallel execution
    parallel_execution(expressions)
    
    time.sleep(5)

