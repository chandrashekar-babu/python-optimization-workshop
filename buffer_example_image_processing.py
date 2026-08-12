import numpy as np
from PIL import Image
import time

# Load an image
img = Image.open('large_image.jpg')

# Time the traditional approach (with copying)
start = time.time()
# Convert to NumPy array (makes a copy)
np_img = np.array(img)
# Apply a simple operation (brighten the image)
brightened = np_img * 1.5
# Clip values to valid range
brightened = np.clip(brightened, 0, 255).astype(np.uint8)
# Convert back to PIL Image (another copy)
result_img = Image.fromarray(brightened)
traditional_time = time.time() - start

# Time the buffer protocol approach
start = time.time()
# Get a memory view directly
buffer = memoryview(img.tobytes())
# Create NumPy array from the buffer without copying
np_img = np.frombuffer(buffer, dtype=np.uint8)
np_img = np_img.reshape(img.height, img.width,
len(img.getbands()))
# Process in-place when possible
np.multiply(np_img, 1.5, out=np_img)
np.clip(np_img, 0, 255, out=np_img)
# Create new image sharing the same buffer
result_img = Image.frombuffer(img.mode, img.size, np_img, 'raw', img.mode, 0, 1)
buffer_time = time.time() - start

print(f"Traditional approach: {traditional_time:.4f} seconds")
print(f"Buffer protocol approach: {buffer_time:.4f} seconds")
print(f"Speedup: {traditional_time / buffer_time:.2f}x")