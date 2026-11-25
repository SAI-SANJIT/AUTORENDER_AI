
import torch
from diffusers import (
    ControlNetModel,
    StableDiffusionControlNetPipeline,
    UniPCMultistepScheduler
)

BASE_DIR = "models/stable-diffusion"
CONTROLNET_DIR = "models/controlnet-canny"


def load_pipeline():

    print("Checking GPU...")

    if not torch.cuda.is_available():
        raise RuntimeError("NVIDIA GPU is not available!")

    print("GPU:", torch.cuda.get_device_name(0))

    dtype = torch.float16

    print("Loading ControlNet FP16...")

    controlnet = ControlNetModel.from_pretrained(
        CONTROLNET_DIR,
        torch_dtype=dtype,
        variant="fp16",
        use_safetensors=True,
        local_files_only=True
    )

    print("Loading Stable Diffusion FP16...")

    pipe = StableDiffusionControlNetPipeline.from_pretrained(
        BASE_DIR,
        controlnet=controlnet,
        torch_dtype=dtype,
        variant="fp16",
        use_safetensors=True,
        safety_checker=None,
        local_files_only=True
    )

    pipe.scheduler = UniPCMultistepScheduler.from_config(
        pipe.scheduler.config
    )

    pipe.enable_model_cpu_offload()

    print("AutoRender AI pipeline loaded successfully!")

    return pipe
