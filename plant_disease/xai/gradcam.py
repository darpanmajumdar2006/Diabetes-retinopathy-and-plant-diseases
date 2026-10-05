# Plant disease Grad-CAM utilities

import cv2
import numpy as np


def generate_gradcam_heatmap(model, image_tensor, target_layer):
    """Placeholder function for Grad-CAM generation.

    Replace this with your actual model-specific Grad-CAM implementation.
    """
    heatmap = np.zeros((224, 224), dtype=np.float32)
    return heatmap


def overlay_heatmap(image, heatmap, alpha=0.5):
    """Overlay a heatmap on an input image."""
    heatmap = cv2.resize(heatmap, (image.shape[1], image.shape[0]))
    heatmap = np.uint8(255 * heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    overlay = cv2.addWeighted(image, 1 - alpha, heatmap, alpha, 0)
    return overlay
