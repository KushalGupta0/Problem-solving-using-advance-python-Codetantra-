class Numbers:

    def __init__(self):
        pass

    def insert_elements(self):
        L = []
        num = int(input("Enter no. of elements:"))
        for i in range(num):
            a = int(input())
            L.append(a)
        self.value = L

    def find_max(self):
        return max(self.value)

n1 = Numbers()
n1.insert_elements()
print("The largest number is:", n1.find_max())
