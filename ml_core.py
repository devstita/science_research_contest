import tensorflow as tf

# TODO: ML Model Accuracy
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=[1]),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1), loss='mse', metrics=['accuracy'])


def train(x_train, y_train):
    model.fit(x_train, y_train, epochs=700)


def query(x_test):
    return model.predict(x_test).flatten()
