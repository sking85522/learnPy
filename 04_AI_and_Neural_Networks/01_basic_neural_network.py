import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# यह एक बहुत ही बेसिक न्यूरल नेटवर्क है जो TensorFlow/Keras का उपयोग करता है।

def create_simple_nn():
    # Sequential मॉडल का मतलब है कि परतें (Layers) एक के बाद एक आ रही हैं
    model = Sequential([
        # पहली छिपी हुई परत (Hidden Layer) 16 न्यूरॉन्स के साथ
        Dense(16, activation='relu', input_shape=(10,)),

        # दूसरी छिपी हुई परत 8 न्यूरॉन्स के साथ
        Dense(8, activation='relu'),

        # आउटपुट परत (Output Layer) 1 न्यूरॉन के साथ (जैसे हाँ या ना का जवाब देने के लिए)
        Dense(1, activation='sigmoid')
    ])

    # मॉडल को संकलित (Compile) करना
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    return model

if __name__ == "__main__":
    print("टेन्सरफ्लो लोड हो रहा है...")
    my_nn = create_simple_nn()

    # मॉडल का ढांचा देखना
    print("\n--- न्यूरल नेटवर्क का ढांचा (Architecture) ---")
    my_nn.summary()
    print("\nइस तरह से न्यूरल नेटवर्क की परतें बनाई जाती हैं!")
