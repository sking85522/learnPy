# यह फ़ाइल कंट्रोल फ्लो (if-else, loops) सिखाती है।

print("--- If-Else Statements ---")
marks = 85

if marks >= 90:
    print("ग्रेड: A")
elif marks >= 80:
    print("ग्रेड: B")
else:
    print("ग्रेड: C")


print("\n--- For Loop ---")
# 1 से 5 तक गिनती
for i in range(1, 6):
    print("गिनती:", i)

animals = ["कुत्ता", "बिल्ली", "शेर"]
for animal in animals:
    print("जानवर:", animal)


print("\n--- While Loop ---")
count = 3
while count > 0:
    print("उलटी गिनती:", count)
    count -= 1
print("शुरू!")
