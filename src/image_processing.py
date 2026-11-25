
import cv2
import numpy as np
from PIL import Image


def detect_edges(image):
    """
    Extract structural edges from an automotive sketch.
    """

    # Convert PIL image to NumPy array
    image = np.array(image.convert("RGB"))

    # Convert RGB to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Reduce unwanted noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(
        blurred,
        threshold1=50,
        threshold2=150
    )

    # Convert edge map into RGB image
    edge_image = Image.fromarray(edges).convert("RGB")

    return edge_image
