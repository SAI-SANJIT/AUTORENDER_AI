
import gradio as gr
import os
import torch

from PIL import Image
from src.image_processing import detect_edges
from src.renderer import load_pipeline
from design import (
    AMBIENT_HTML,
    APP_CSS,
    APP_JS,
    FAQ_HTML,
    FEATURES_HTML,
    FOOTER_HTML,
    HEAD_HTML,
    HERO_HTML,
    HOW_IT_WORKS_HTML,
    LEFT_PANEL_INPUT_HEADER_HTML,
    LEFT_PANEL_PARAMS_HEADER_HTML,
    LOADER_OVERLAY_HTML,
    NAVBAR_HTML,
    RIGHT_PANEL_INSPECT_HEADER_HTML,
    RIGHT_PANEL_OUTPUT_HEADER_HTML,
    STUDIO_HEADER_HTML,
    build_autorender_theme,
)

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# Load the AI pipeline only once
pipe = None


def get_pipeline():
    global pipe

    if pipe is None:
        print("Loading AutoRender AI models...")
        pipe = load_pipeline()

    return pipe


def process_sketch(image, prompt, steps, guidance, control_strength, seed):

    if image is None:
        raise gr.Error("Please upload a vehicle sketch!")

    if not prompt or not prompt.strip():
        prompt = (
            "photorealistic modern sports car, realistic metallic paint, "
            "detailed headlights, realistic wheels, studio lighting, "
            "professional automotive photography, highly detailed"
        )

    try:
        # Resize sketch for Stable Diffusion
        sketch = image.convert("RGB").resize((512, 512))

        # Extract Canny edges
        edge_image = detect_edges(sketch)

        # Load AI models
        model = get_pipeline()

        # Negative prompt
        negative_prompt = (
            "cartoon, illustration, blurry, low quality, "
            "distorted wheels, extra wheels, deformed vehicle"
        )

        print("Generating photorealistic vehicle...")

        # Generate image
        with torch.inference_mode():
            generator = torch.Generator(device="cpu").manual_seed(int(seed))
            result = model(
                prompt=prompt,
                generator=generator,
                negative_prompt=negative_prompt,
                image=edge_image,
                num_inference_steps=int(steps),
                guidance_scale=guidance,
                controlnet_conditioning_scale=control_strength,
                height=512,
                width=512
            ).images[0]

        # Save generated render
        output_path = "outputs/latest_render.png"
        result.save(output_path)

        print("Vehicle rendering completed!")

        return (
            sketch,
            edge_image,
            result,
            "Vehicle generated successfully!",
            output_path
        )

    except Exception as e:
        raise gr.Error(f"Generation failed: {str(e)}")


autorender_theme = build_autorender_theme()

with gr.Blocks(title="AutoRender AI") as demo:

    gr.HTML(AMBIENT_HTML, elem_id="ar-ambient-host", apply_default_css=False)
    gr.HTML(NAVBAR_HTML, elem_id="ar-nav-host", apply_default_css=False)
    gr.HTML(LOADER_OVERLAY_HTML, elem_id="ar-loader-host", apply_default_css=False)
    gr.HTML(HERO_HTML, elem_id="ar-hero-host", apply_default_css=False)

    gr.HTML(STUDIO_HEADER_HTML, elem_id="ar-studio-header-host", apply_default_css=False)

    with gr.Row(elem_id="ar-studio-row", equal_height=False):

        with gr.Column(scale=5, min_width=340, elem_id="ar-studio-left"):
            with gr.Column(elem_classes=["ar-studio-card"]):
                gr.HTML(
                    LEFT_PANEL_INPUT_HEADER_HTML,
                    elem_classes=["ar-card-head-html"],
                    apply_default_css=False,
                )

                sketch = gr.Image(
                    label="Upload Sketch",
                    type="pil",
                    height=320,
                    elem_id="ar-sketch-upload",
                )

                prompt = gr.Textbox(
                    label="Rendering Prompt",
                    placeholder="Describe your desired vehicle appearance...",
                    lines=2,
                    elem_id="ar-prompt-input",
                )

            with gr.Column(elem_classes=["ar-studio-card", "ar-studio-card-lavender"]):
                gr.HTML(
                    LEFT_PANEL_PARAMS_HEADER_HTML,
                    elem_classes=["ar-card-head-html"],
                    apply_default_css=False,
                )

                steps = gr.Slider(
                    minimum=5,
                    maximum=30,
                    value=15,
                    step=1,
                    label="Inference Steps",
                    elem_id="ar-steps-slider",
                )

                guidance = gr.Slider(
                    minimum=1,
                    maximum=15,
                    value=7,
                    step=0.5,
                    label="Guidance Scale",
                    elem_id="ar-guidance-slider",
                )

                control_strength = gr.Slider(
                    minimum=0.1,
                    maximum=1.5,
                    value=0.8,
                    step=0.1,
                    label="ControlNet Strength",
                    elem_id="ar-control-slider",
                )

                seed = gr.Number(
                    label="Generation Seed",
                    value=42,
                    precision=0,
                    elem_id="ar-seed-input",
                )

                generate = gr.Button(
                    "Generate Vehicle Render",
                    variant="primary",
                    elem_id="ar-generate-btn",
                )

        with gr.Column(scale=7, min_width=380, elem_id="ar-studio-right"):
            with gr.Column(elem_classes=["ar-studio-card", "ar-studio-card-featured"]):
                gr.HTML(
                    RIGHT_PANEL_OUTPUT_HEADER_HTML,
                    elem_classes=["ar-card-head-html"],
                    apply_default_css=False,
                )

                generated = gr.Image(
                    label="Photorealistic Vehicle Render",
                    height=460,
                    interactive=False,
                    elem_id="ar-generated-output",
                )

                with gr.Row(elem_id="ar-action-row", equal_height=True):
                    status = gr.Textbox(
                        label="Processing Status",
                        interactive=False,
                        placeholder="Ready to render your vehicle sketch...",
                        elem_id="ar-status-box",
                        scale=3,
                    )

                    download = gr.DownloadButton(
                        label="Download Generated Vehicle",
                        value=None,
                        elem_id="ar-download-btn",
                        scale=2,
                    )

            with gr.Column(elem_classes=["ar-studio-card", "ar-studio-card-sage"]):
                gr.HTML(
                    RIGHT_PANEL_INSPECT_HEADER_HTML,
                    elem_classes=["ar-card-head-html"],
                    apply_default_css=False,
                )

                with gr.Row(elem_id="ar-inspect-row"):
                    original = gr.Image(
                        label="Original Sketch",
                        height=220,
                        interactive=False,
                        elem_id="ar-original-preview",
                    )

                    edges = gr.Image(
                        label="Canny Edge Map",
                        height=220,
                        interactive=False,
                        elem_id="ar-edges-preview",
                    )

    gr.HTML(HOW_IT_WORKS_HTML, elem_id="ar-how-host", apply_default_css=False)
    gr.HTML(FEATURES_HTML, elem_id="ar-features-host", apply_default_css=False)
    gr.HTML(FAQ_HTML, elem_id="ar-faq-host", apply_default_css=False)
    gr.HTML(FOOTER_HTML, elem_id="ar-footer-host", apply_default_css=False)

    gen_event = generate.click(
        fn=process_sketch,
        inputs=[sketch, prompt, steps, guidance, control_strength, seed],
        outputs=[original, edges, generated, status, download],
        show_progress="hidden",
        js="""(sketchVal, promptVal, stepsVal, guidanceVal, controlVal, seedVal) => {
            if (sketchVal && window.arShowLoader) {
                window.arShowLoader();
            }
            return [sketchVal, promptVal, stepsVal, guidanceVal, controlVal, seedVal];
        }""",
    )
    gen_event.then(
        fn=None,
        inputs=None,
        outputs=None,
        js="() => { if (window.arHideLoader) window.arHideLoader(); }",
    )

demo.launch(
    server_name="0.0.0.0",
    server_port=7860,
    # Public access is provided separately through the Cloudflare Quick Tunnel.
    theme=autorender_theme,
    css=APP_CSS,
    js=APP_JS,
    head=HEAD_HTML,
    footer_links=["api"],
)

