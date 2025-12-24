def myfunction(n):
    print(f"--- Complexity Analysis for n = {n} ---")

    for i in range(0, n + 1):
        x = i

    j = 1
    while j <= n + 1:
        j = j * 2

    for i in range(0, 100):
        y = i

    print("Execution Finished.")

myfunction(10)
print("="*30)
myfunction(100)