import tensorflow as tf
import numpy as np

# Example training data
train_data = np.array([10, 12, 11, 14, 9, 12, 13, 11, 10, 15])
train_labels = np.array([11, 13, 12, 15, 10, 13, 14, 12, 11, 16])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(train_data, train_labels, epochs=50)

model.save('energy_model.h5')
