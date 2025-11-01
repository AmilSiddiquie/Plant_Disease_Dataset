import tensorflow as tf

print("TensorFlow version:", tf.__version__)
print("GPUs available:", tf.config.list_physical_devices('GPU'))  # Should show []
print("Running a quick computation on CPU:", tf.reduce_sum(tf.random.normal([1000, 1000])))
print("Computation successful!")