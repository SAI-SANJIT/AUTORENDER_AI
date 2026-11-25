
import torch
from PIL import Image
from src.renderer import load_pipeline
from src.image_processing import detect_edges

print("Loading AutoRender AI...")

pipe = load_pipeline()

# Load the vehicle sketch
sketch = Image.open("uploads/car_sketch.png").convert("RGB")
sketch = sketch.resize((512, 512))

# Extract Canny edges
edge_image = detect_edges(sketch)

# Generate photorealistic vehicle
prompt = (
    "photorealistic professional automotive photography, "
    "sleek modern sports car, realistic metallic paint, "
    "detailed headlights, realistic wheels, studio lighting, "
    "highly detailed, 4k"
)

negative_prompt = (
    "cartoon, illustration, distorted wheels, extra wheels, "
    "deformed car, blurry, low quality, unrealistic proportions"
)

print("Generating vehicle render...")

with torch.inference_mode():
    result = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        image=edge_image,
        num_inference_steps=15,
        guidance_scale=7,
        controlnet_conditioning_scale=0.8,
        height=512,
        width=512
    ).images[0]

result.save("outputs/first_render.png")

print("SUCCESS! Render saved to outputs/first_render.png")
