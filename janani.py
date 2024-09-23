import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Define data path
data_path ='E:/medical/data-2'

# Check if data path exists
if not os.path.exists(data_path):
    print(f"Error: Data path '{data_path}' does not exist.")
    exit()

# Load and preprocess data
train_datagen = ImageDataGenerator(rescale=1./255)

try:
    train_generator = train_datagen.flow_from_directory(
        os.path.join(data_path, 'train'),
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary'
    )
    
    validation_generator = train_datagen.flow_from_directory(
        os.path.join(data_path, 'validation'),
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary'
    )
    
    test_generator = train_datagen.flow_from_directory(
        os.path.join(data_path, 'test'),
        target_size=(150, 150),
        batch_size=32,
        class_mode='binary'
    )
    
    print("Data loaded successfully.")
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# Build a simple CNN
from tensorflow.keras.layers import Input
model = tf.keras.Sequential([
    Input(shape=(150, 150, 3)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
try:
    model.fit(train_generator, validation_data=validation_generator, epochs=10)
except Exception as e:
    print(f"Error training model: {e}")

# Evaluate the model
try:
    loss, accuracy = model.evaluate(test_generator)
    print(f"Test accuracy: {accuracy:.2f}")
except Exception as e:
    print(f"Error evaluating model: {e}")
