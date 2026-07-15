# यह फ़ाइल वेरिएबल्स (Variables) और डेटा प्रकारों (Data Types) के बारे में सिखाती है।

# 1. Numbers (संख्याएँ)
age = 25          # Integer (पूर्णांक)
height = 5.9      # Float (दशमलव)

# 2. Strings (टेक्स्ट)
name = "पायथन लर्नर"
message = 'कोडिंग मजेदार है!'

# 3. Lists (सूचियाँ) - इन्हें बदला जा सकता है (Mutable)
fruits = ["सेब", "केला", "संतरा"]
fruits.append("आम") # सूची में नया आइटम जोड़ना

# 4. Tuples - इन्हें बदला नहीं जा सकता (Immutable)
coordinates = (10.0, 20.0)

# 5. Dictionaries - की-वैल्यू पेयर (Key-Value pairs)
person = {
    "नाम": "राहुल",
    "उम्र": 30,
    "शहर": "दिल्ली"
}

# 6. Boolean (सत्य/असत्य)
is_learning = True
is_tired = False

print("मेरा नाम", name, "है और मेरी उम्र", age, "है।")
print("मुझे", fruits[0], "पसंद है।")
print("व्यक्ति की जानकारी:", person["शहर"])
