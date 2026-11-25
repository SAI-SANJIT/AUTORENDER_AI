# 🚗 AutoRender AI
### Transform Vehicle Sketches into Photorealistic Images Using Artificial Intelligence

AutoRender AI is an AI-powered vehicle rendering application that transforms simple vehicle sketches into realistic, high-quality vehicle images using Deep Learning and image processing techniques.

The application uses Stable Diffusion 1.5 combined with ControlNet Canny Edge Detection to preserve the structure and shape of the original sketch while generating realistic vehicle designs.

---

## ✨ Features

- **Sketch-to-Image Generation:** Convert hand-drawn vehicle sketches into realistic images.
- **AI-Powered Rendering:** Uses Stable Diffusion 1.5 for photorealistic image generation.
- **ControlNet Integration:** Uses Canny edge detection to maintain the original sketch structure.
- **Custom Prompts:** Describe the desired vehicle appearance using text prompts.
- **Adjustable Parameters:** Customize inference steps, guidance scale, ControlNet strength, and random seed.
- **Edge Detection Preview:** View the extracted edges of the uploaded sketch.
- **Image Download:** Download the generated vehicle image.
- **Interactive Web Interface:** User-friendly interface built using Gradio with a custom-designed UI.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Gradio | Web application interface |
| Stable Diffusion 1.5 | AI image generation |
| ControlNet Canny | Sketch structure preservation |
| OpenCV | Image processing and edge detection |
| PyTorch | Deep learning framework |
| Diffusers | Stable Diffusion pipeline |
| NumPy | Image array processing |
| Pillow | Image handling |

---

## 📁 Project Structure

```text
AutoRenderAI/
│
├── app.py
├── design.py
├── test_model.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── image_processing.py
│   └── renderer.py
│
├── models/
│   ├── stable-diffusion/
│   └── controlnet-canny/
│
├── assets/
├── uploads/
├── outputs/
└── venv/
```

**Note:** The `models/`, `uploads/`, `outputs/`, and `venv/` folders are excluded from the GitHub repository where appropriate. The folder structure above represents the local project setup.

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/SAI-SANJIT/AUTORENDER_AI.git
```

### 2. Navigate to the Project Directory

```bash
cd AUTORENDER_AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

For GPU acceleration, install a PyTorch build compatible with your NVIDIA GPU and CUDA environment if the installed version is not suitable.

---

## 🤖 Model Setup

AutoRender AI uses two locally stored AI models:

1. **Stable Diffusion 1.5**
2. **ControlNet Canny**

Place the downloaded model files in the following directories, matching the paths expected by `src/renderer.py`:

```text
models/
├── stable-diffusion/
└── controlnet-canny/
```

The model weights are not included in this GitHub repository because of their large file sizes.

You must download and configure the required model files before running the application.

---

## ▶️ Running the Application

After installing dependencies and configuring the models, run:

```bash
python app.py
```

Open your browser and visit:

```text
http://localhost:7860
```

The application interface will open.

---

## 🖥️ How It Works

The application follows this workflow:

1. **Upload Sketch:** The user uploads a vehicle sketch.
2. **Image Processing:** OpenCV processes the uploaded image.
3. **Edge Detection:** Canny edge detection extracts the important structural outlines.
4. **AI Rendering:** Stable Diffusion and ControlNet generate a realistic vehicle image.
5. **Display Result:** The generated image is displayed in the application.
6. **Download:** The user can download the generated image.

### System Workflow

```text
Vehicle Sketch
      |
      v
Image Processing
      |
      v
Canny Edge Detection
      |
      v
ControlNet + Stable Diffusion
      |
      v
AI Image Generation
      |
      v
Photorealistic Vehicle Image
      |
      v
Download Generated Image
```

---

## 🎛️ Generation Parameters

The application provides adjustable controls:

| Parameter | Description |
|---|---|
| Inference Steps | Controls the number of image generation steps |
| Guidance Scale | Controls how closely the output follows the text prompt |
| ControlNet Strength | Controls how strongly the generated image follows the sketch |
| Seed | Controls reproducibility of image generation |

---

## 💻 System Requirements

- Python
- NVIDIA GPU recommended for faster generation
- Compatible PyTorch and CUDA environment for GPU acceleration
- Sufficient RAM and GPU memory
- Stable Diffusion and ControlNet model files

Performance depends on the hardware configuration and generation settings.

---

## 👨‍💻 Developer

**Project Name:** AutoRender AI

**GitHub Repository:**  
https://github.com/SAI-SANJIT/AUTORENDER_AI

---

## 📌 Project Objective

The main objective of AutoRender AI is to simplify vehicle visualization by converting basic sketches into realistic vehicle designs using artificial intelligence.

It demonstrates the practical application of Deep Learning, Computer Vision, Image Processing, and Generative AI in automotive design.

---

*AutoRender AI — From Sketch to Reality.* 🚗
