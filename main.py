import threading
import time

def evaluate_expression(expression):
    expression = expression.replace(" ", "")
    return eval(expression)

def evaluate_expression_concurrently(expression):
    expression = expression.replace(" ", "")
    result = [None]

    def evaluate():
        result[0] = eval(expression)

    thread = threading.Thread(target=evaluate)
    thread.start()
    thread.join()

    return result[0]

def test():
    expressions = ["1 + 2 * 3 / 4 - 5", "6 * (7 + 8) / 9 - 10", "11 / 12 + 13 - 14 * 15"]
    print("Enter expression: ")
    
    
    print("Testing Parallel MDAS Calculator:")
    for exp in expressions:
        start_time = time.time()
        result = evaluate_expression_concurrently(exp)
        end_time = time.time()
        print(f"Expression: {exp}, \nResult: {result}, \nTime: {end_time - start_time:.4f} seconds")

    print("\nTesting Sequential MDAS Calculator:")
    for exp in expressions:
        start_time = time.time()
        result = evaluate_expression(exp)
        end_time = time.time()
        print(f"Expression: {exp},\nResult: {result}, \nTime: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    test()
