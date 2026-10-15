s1 = int(input("Sub 1: "))
s2 = int(input("Sub 2: "))
s3 = int(input("Sub 3: "))
s4 = int(input("Sub 4: "))
s5 = int(input("Sub 5: "))

pct = (s1 + s2 + s3 + s4 + s5) // 5

if pct >= 75: grade = "Distinction"
elif pct >= 65: grade = "First Class"
elif pct >= 40: grade = "Second Class"
else: grade = "Fail"

print("Percentage:", pct, "% | Grade:", grade)
