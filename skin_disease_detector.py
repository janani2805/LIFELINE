from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator

# Define directories
base_dir = r'C:\Users\NIVESARA\Downloads\archive (2)\data-2'
train_data_dir = os.path.join(base_dir, 'train')
validation_data_dir = os.path.join(base_dir, 'validation')

# Data generators
train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary'
)

validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary'
)

# Load or define your YOLO model here
# model = ...

# Train the model
history = model.fit(train_generator, validation_data=validation_generator, epochs=10)
