def prints(n):
    if (n <= 1):
        return
    print("Codingal", end="\r")
    prints(n/2)
    prints(n/2)

def myfunction(n):
    print(f"--- Complexity Analysis for n = {n} ---")

    for i in range(0, n + 1):
        x = i

    j = 1
    while j <= n + 1:
        j = j * 2

    for i in range(0, 100):
        y = i

    print("Executing Recursive Calls...")
    prints(n)

    print("\nExecution Finished.")

myfunction(10)
print("="*30)
myfunction(100)