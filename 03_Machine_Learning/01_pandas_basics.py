import pandas as pd

# 1. डेटा बनाना (Creating Data)
data = {
    'नाम': ['राहुल', 'प्रिया', 'अमित', 'सुनीता'],
    'उम्र': [25, 22, 28, 24],
    'शहर': ['दिल्ली', 'मुंबई', 'पुणे', 'बैंगलोर'],
    'वेतन': [50000, 60000, 45000, 70000]
}

# डिक्शनरी को Pandas DataFrame में बदलना
df = pd.DataFrame(data)

print("--- हमारा पूरा डेटा ---")
print(df)
print("\n")

# 2. डेटा विश्लेषण (Data Analysis)
print("--- केवल 25 साल से अधिक उम्र के लोग ---")
older_than_25 = df[df['उम्र'] > 25]
print(older_than_25)
print("\n")

# 3. औसत वेतन निकालना
average_salary = df['वेतन'].mean()
print(f"--- सभी का औसत वेतन: {average_salary} ---")
