from sklearn.linear_model import LinearRegression
import numpy as np

# मान लीजिए कि हम घरों के आकार (Square feet) के आधार पर उनकी कीमत (Lakhs) की भविष्यवाणी करना चाहते हैं।

# X: घर का आकार (Features - 2D array होना चाहिए)
X = np.array([[500], [1000], [1500], [2000], [2500]])

# y: घर की कीमत लाखों में (Target/Labels)
y = np.array([20, 40, 60, 80, 100])

# मशीन लर्निंग मॉडल बनाना (Linear Regression)
model = LinearRegression()

# मॉडल को डेटा पर ट्रेन करना (सीखना)
model.fit(X, y)
print("मॉडल ट्रेनिंग पूरी हो गई है!")

# अब नए डेटा पर भविष्यवाणी करना
new_house_size = np.array([[1800]])
predicted_price = model.predict(new_house_size)

print(f"\n1800 वर्ग फुट के घर की अनुमानित कीमत: {predicted_price[0]} लाख रुपये होगी।")
