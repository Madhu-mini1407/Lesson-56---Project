def myfunction(n):
    
    print(f"\n--- Complexity Analysis for n = {n} ---")
    
    print("1. First Loop Complexity: O(n) (Linear Time)")
    for i in range(0, n + 1):
        print("First Loop")

    
    print("\n2. Second Loop Complexity: O(log n) (Logarithmic Time)")
    j = 1
    while j <= n + 1:
        print("Second Loop ",j)
        j = j * 2

    
    print("\n3. Third Loop Complexity: O(1) (Constant Time)")
    for i in range(0, 100):
        print("Third loop")

    print("\nTotal Time Complexity: O(n)")

myfunction(10)
print("\n" + "="*50)
myfunction(100)