"""
AutoRender AI — Editorial Soft-Minimalist Design System & UI Assets.

Provides the custom Gradio theme, Google Fonts head tags, CSS design tokens,
HTML landing/navigation/loader sections, and interactive JS behaviors while
preserving 100% of the existing Python/Gradio inference backend.
"""

import gradio as gr
from gradio.themes import Soft
from gradio.themes.utils import fonts


def build_autorender_theme() -> Soft:
    """Create a Gradio Soft theme aligned to the AutoRender AI palette."""
    theme = Soft(
        font=(
            fonts.GoogleFont("Outfit", weights=(300, 400, 500, 600, 700)),
            "ui-sans-serif",
            "system-ui",
            "sans-serif",
        ),
    )
    theme.set(
        body_background_fill="#FDFCF8",
        body_background_fill_dark="#FDFCF8",
        background_fill_primary="#FDFCF8",
        background_fill_primary_dark="#FDFCF8",
        background_fill_secondary="#FFFFFF",
        background_fill_secondary_dark="#FFFFFF",
        block_background_fill="#FFFFFF",
        block_background_fill_dark="#FFFFFF",
        block_border_width="1px",
        block_border_color="rgba(41, 37, 36, 0.08)",
        block_border_color_dark="rgba(41, 37, 36, 0.08)",
        block_radius="20px",
        block_label_background_fill="#EFEDF4",
        block_label_background_fill_dark="#EFEDF4",
        block_label_text_color="#292524",
        block_label_text_color_dark="#292524",
        block_label_text_weight="500",
        block_label_radius="9999px",
        block_title_background_fill="#EFEDF4",
        block_title_background_fill_dark="#EFEDF4",
        block_title_text_color="#292524",
        block_title_text_color_dark="#292524",
        block_title_text_weight="500",
        block_title_radius="9999px",
        body_text_color="#292524",
        body_text_color_dark="#292524",
        body_text_color_subdued="#78716C",
        body_text_color_subdued_dark="#78716C",
        input_background_fill="#FDFCF8",
        input_background_fill_dark="#FDFCF8",
        input_border_color="rgba(41, 37, 36, 0.12)",
        input_border_color_dark="rgba(41, 37, 36, 0.12)",
        input_border_color_focus="#FFB7B2",
        input_border_color_focus_dark="#FFB7B2",
        input_radius="16px",
        slider_color="#FFB7B2",
        slider_color_dark="#FFB7B2",
        button_primary_background_fill="#FFB7B2",
        button_primary_background_fill_hover="#FFA39D",
        button_primary_background_fill_dark="#FFB7B2",
        button_primary_background_fill_hover_dark="#FFA39D",
        button_primary_text_color="#292524",
        button_primary_text_color_dark="#292524",
        button_secondary_background_fill="#292524",
        button_secondary_background_fill_hover="#3D3836",
        button_secondary_background_fill_dark="#292524",
        button_secondary_background_fill_hover_dark="#3D3836",
        button_secondary_text_color="#FDFCF8",
        button_secondary_text_color_dark="#FDFCF8",
        shadow_drop="0 8px 28px rgba(41, 37, 36, 0.045)",
        shadow_drop_lg="0 16px 40px rgba(41, 37, 36, 0.06)",
    )
    return theme


HEAD_HTML = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Reenie+Beanie&display=swap" rel="stylesheet">
<meta name="theme-color" content="#FDFCF8">
"""


AMBIENT_HTML = """
<div class="ar-ambient-layer" aria-hidden="true">
  <div class="ar-blob ar-blob-coral"></div>
  <div class="ar-blob ar-blob-lavender"></div>
  <div class="ar-blob ar-blob-sage"></div>
</div>
<div class="ar-grain-overlay" aria-hidden="true"></div>
"""


NAVBAR_HTML = """
<header class="ar-nav-shell">
  <nav class="ar-nav-pill" aria-label="Primary navigation">
    <a href="#ar-hero" class="ar-brand" data-scroll-target="ar-hero">
      <span class="ar-brand-badge" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M3.5 14.5h17l-1.6-4.2a2.5 2.5 0 0 0-2.3-1.6H8.8a3 3 0 0 0-2.4 1.2L3.5 14.5Z"/>
          <circle cx="7.5" cy="15.5" r="1.7"/>
          <circle cx="16.5" cy="15.5" r="1.7"/>
          <path d="M5 6.5h6.5"/>
        </svg>
      </span>
      <span class="ar-brand-text">AutoRender AI</span>
    </a>

    <div class="ar-nav-links" role="menubar">
      <button type="button" class="ar-nav-link" data-scroll-target="ar-hero" role="menuitem">Home</button>
      <button type="button" class="ar-nav-link" data-scroll-target="ar-studio" role="menuitem">Studio</button>
      <button type="button" class="ar-nav-link" data-scroll-target="ar-how-it-works" role="menuitem">How it works</button>
      <button type="button" class="ar-nav-link" data-scroll-target="ar-faq" role="menuitem">About</button>
    </div>

    <div class="ar-nav-actions">
      <button type="button" class="ar-nav-cta" data-scroll-target="ar-studio">
        Start Creating
      </button>
      <button type="button" class="ar-nav-toggle" id="ar-nav-toggle" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="ar-mobile-menu">
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>

  <div class="ar-mobile-menu" id="ar-mobile-menu" hidden>
    <button type="button" class="ar-mobile-link" data-scroll-target="ar-hero">Home</button>
    <button type="button" class="ar-mobile-link" data-scroll-target="ar-studio">Studio</button>
    <button type="button" class="ar-mobile-link" data-scroll-target="ar-how-it-works">How it works</button>
    <button type="button" class="ar-mobile-link" data-scroll-target="ar-features">Features</button>
    <button type="button" class="ar-mobile-link" data-scroll-target="ar-faq">About &amp; FAQ</button>
    <button type="button" class="ar-mobile-cta" data-scroll-target="ar-studio">Start Creating</button>
  </div>
</header>
"""


HERO_HTML = """
<section id="ar-hero" class="ar-hero">
  <div class="ar-hero-inner">
    <div class="ar-hero-kicker ar-reveal">
      <span class="ar-kicker-dot" aria-hidden="true"></span>
      <span>AI Automotive Design Studio</span>
    </div>

    <h1 class="ar-hero-title ar-reveal">
      From simple sketches to
      <span class="ar-hero-accent-wrap">
        <span class="ar-handwritten-word">stunning</span>
        <svg class="ar-underline-svg" viewBox="0 0 220 18" fill="none" aria-hidden="true">
          <path d="M4 13.5C58 4.5 148 3.5 216 11.5" stroke="#FFB7B2" stroke-width="3.6" stroke-linecap="round"/>
        </svg>
      </span>
      realities.
    </h1>

    <p class="ar-hero-subtitle ar-reveal">
      Transform your vehicle sketches into realistic automotive designs using the power of artificial intelligence.
    </p>

    <div class="ar-hero-ctas ar-reveal">
      <button type="button" class="ar-btn ar-btn-coral" data-scroll-target="ar-studio">
        <span>Start Creating</span>
        <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M4.5 10h11M11 5.5 15.5 10 11 14.5"/>
        </svg>
      </button>
      <button type="button" class="ar-btn ar-btn-outline" data-scroll-target="ar-how-it-works">
        <span>Explore the Studio</span>
      </button>
    </div>

    <div class="ar-hero-showcase ar-reveal" aria-label="Sketch to photorealistic render pipeline illustration">
      <div class="ar-showcase-panel ar-showcase-sketch">
        <div class="ar-showcase-tag">
          <span class="ar-tag-dot ar-dot-stone"></span>
          <span>Input sketch</span>
          <span class="ar-handwritten-note">raw linework</span>
        </div>
        <svg class="ar-car-svg" viewBox="0 0 420 175" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Automotive coupe pencil wireframe sketch">
          <line x1="24" y1="142" x2="396" y2="142" stroke="#78716C" stroke-opacity="0.35" stroke-width="1.2" stroke-dasharray="4 4"/>
          <path d="M52 126C48 111 58 94 79 88L142 74C167 52 204 42 246 43C284 44 316 58 346 78L374 87C386 92 391 106 386 125" stroke="#292524" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M84 127H102M158 127H268M326 127H374" stroke="#292524" stroke-width="2" stroke-linecap="round"/>
          <path d="M150 76C174 58 206 51 242 52C269 53 292 62 313 78L150 76Z" stroke="#78716C" stroke-width="1.4" stroke-dasharray="5 3"/>
          <path d="M98 92C146 88 228 87 328 94" stroke="#78716C" stroke-width="1.3" stroke-linecap="round"/>
          <path d="M225 53L219 77M185 92L178 122M279 93L275 122" stroke="#78716C" stroke-width="1.1" stroke-opacity="0.7"/>
          <circle cx="130" cy="126" r="26" stroke="#292524" stroke-width="2"/>
          <circle cx="130" cy="126" r="14" stroke="#78716C" stroke-width="1.3" stroke-dasharray="3 3"/>
          <circle cx="297" cy="126" r="26" stroke="#292524" stroke-width="2"/>
          <circle cx="297" cy="126" r="14" stroke="#78716C" stroke-width="1.3" stroke-dasharray="3 3"/>
          <path d="M62 103L86 99L78 111H57" stroke="#FFB7B2" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>

      <div class="ar-showcase-bridge" aria-hidden="true">
        <div class="ar-bridge-pill">
          <span class="ar-bridge-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14M13 6l6 6-6 6"/>
            </svg>
          </span>
          <span class="ar-bridge-label">Canny + ControlNet</span>
        </div>
      </div>

      <div class="ar-showcase-panel ar-showcase-render">
        <div class="ar-showcase-tag">
          <span class="ar-tag-dot ar-dot-coral"></span>
          <span>Studio render</span>
          <span class="ar-handwritten-note">512 × 512 AI output</span>
        </div>
        <svg class="ar-car-svg" viewBox="0 0 420 175" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Stylized studio-lit automotive coupe silhouette">
          <defs>
            <linearGradient id="arBodyGrad" x1="60" y1="45" x2="365" y2="135" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#292524"/>
              <stop offset="52%" stop-color="#44403C"/>
              <stop offset="100%" stop-color="#292524"/>
            </linearGradient>
            <linearGradient id="arGlassGrad" x1="150" y1="50" x2="310" y2="80" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#EFEDF4" stop-opacity="0.95"/>
              <stop offset="100%" stop-color="#FFB7B2" stop-opacity="0.45"/>
            </linearGradient>
          </defs>
          <ellipse cx="218" cy="150" rx="166" ry="8" fill="#292524" fill-opacity="0.1"/>
          <path d="M52 126C48 111 58 94 79 88L142 74C167 52 204 42 246 43C284 44 316 58 346 78L374 87C386 92 391 106 386 125L372 127H54L52 126Z" fill="url(#arBodyGrad)"/>
          <path d="M150 76C174 58 206 51 242 52C269 53 292 62 313 78L150 76Z" fill="url(#arGlassGrad)"/>
          <path d="M96 93C146 89 235 88 336 95" stroke="#FFB7B2" stroke-width="2" stroke-opacity="0.85" stroke-linecap="round"/>
          <path d="M62 103L88 99L79 111H57Z" fill="#FFB7B2"/>
          <path d="M366 96L385 100L381 109H362Z" fill="#FFB7B2" fill-opacity="0.9"/>
          <circle cx="130" cy="126" r="27" fill="#FDFCF8" stroke="#292524" stroke-width="5"/>
          <circle cx="130" cy="126" r="13" fill="#EFEDF4" stroke="#292524" stroke-width="2"/>
          <circle cx="130" cy="126" r="4.5" fill="#FFB7B2"/>
          <circle cx="297" cy="126" r="27" fill="#FDFCF8" stroke="#292524" stroke-width="5"/>
          <circle cx="297" cy="126" r="13" fill="#EFEDF4" stroke="#292524" stroke-width="2"/>
          <circle cx="297" cy="126" r="4.5" fill="#FFB7B2"/>
        </svg>
      </div>
    </div>
  </div>
</section>
"""


STUDIO_HEADER_HTML = """
<div id="ar-studio" class="ar-section-header ar-reveal">
  <div class="ar-section-kicker-row">
    <span class="ar-pill-tag ar-pill-coral">01 · Interactive Studio</span>
    <span class="ar-handwritten-kicker">sketch in, render out</span>
  </div>
  <h2 class="ar-section-title">Design &amp; rendering workspace</h2>
  <p class="ar-section-desc">
    Upload an automotive sketch, tune your diffusion guidance and ControlNet conditioning, and inspect the extracted Canny edges alongside your photorealistic render.
  </p>
</div>
"""


LEFT_PANEL_INPUT_HEADER_HTML = """
<div class="ar-card-head">
  <div>
    <span class="ar-card-step">Step 01</span>
    <h3 class="ar-card-title">Vehicle sketch &amp; prompt</h3>
  </div>
  <span class="ar-card-badge">512 × 512 RGB</span>
</div>
"""


LEFT_PANEL_PARAMS_HEADER_HTML = """
<div class="ar-card-head">
  <div>
    <span class="ar-card-step">Step 02</span>
    <h3 class="ar-card-title">Diffusion &amp; ControlNet controls</h3>
  </div>
  <span class="ar-handwritten-mini">precision tuning</span>
</div>
"""


RIGHT_PANEL_OUTPUT_HEADER_HTML = """
<div class="ar-card-head">
  <div>
    <span class="ar-card-step">Step 03</span>
    <h3 class="ar-card-title">Photorealistic vehicle render</h3>
  </div>
  <span class="ar-card-badge ar-badge-coral">AI Studio Output</span>
</div>
"""


RIGHT_PANEL_INSPECT_HEADER_HTML = """
<div class="ar-card-head">
  <div>
    <span class="ar-card-step">Pipeline inspection</span>
    <h3 class="ar-card-title">Original sketch &amp; Canny edge map</h3>
  </div>
  <span class="ar-handwritten-mini">structural blueprint</span>
</div>
"""


LOADER_OVERLAY_HTML = """
<div id="ar-loader-overlay" class="ar-loader-overlay" role="status" aria-live="polite" aria-hidden="true">
  <div class="ar-loader-card">
    <div class="ar-speed-stage" aria-hidden="true">
      <svg class="ar-speed-svg" viewBox="0 0 320 120" fill="none" xmlns="http://www.w3.org/2000/svg">
        <!-- Animated horizontal speed lines -->
        <line class="ar-speed-line ar-sl-1" x1="230" y1="28" x2="305" y2="28" stroke="#FFB7B2" stroke-width="3" stroke-linecap="round"/>
        <line class="ar-speed-line ar-sl-2" x1="210" y1="44" x2="295" y2="44" stroke="#292524" stroke-opacity="0.28" stroke-width="2.2" stroke-linecap="round"/>
        <line class="ar-speed-line ar-sl-3" x1="240" y1="62" x2="312" y2="62" stroke="#FFB7B2" stroke-width="2.5" stroke-linecap="round"/>
        <line class="ar-speed-line ar-sl-4" x1="195" y1="80" x2="285" y2="80" stroke="#292524" stroke-opacity="0.22" stroke-width="2" stroke-linecap="round"/>
        <line class="ar-speed-line ar-sl-5" x1="40" y1="98" x2="280" y2="98" stroke="#292524" stroke-opacity="0.14" stroke-width="2" stroke-linecap="round"/>

        <!-- Character-like geometric speed pod -->
        <g class="ar-runner-char">
          <!-- Soft ground shadow -->
          <ellipse cx="145" cy="99" rx="54" ry="5" fill="#292524" fill-opacity="0.1"/>
          <!-- Trailing aerodynamic scarf/fin -->
          <path d="M88 54C74 51 64 56 54 62C66 64 78 65 92 63Z" fill="#FFB7B2"/>
          <!-- Main rounded capsule body -->
          <path d="M86 73C86 52 103 36 126 36H168C191 36 212 52 214 73C215 80 209 86 201 86H99C91 86 86 80 86 73Z" fill="#292524"/>
          <!-- Coral roof crest -->
          <path d="M126 36H164C173 36 180 40 185 45H115C119 40 122 36 126 36Z" fill="#FFB7B2"/>
          <!-- Expressive geometric visor -->
          <rect x="150" y="49" width="46" height="18" rx="9" fill="#FDFCF8"/>
          <!-- Minimal character eyes inside visor -->
          <circle class="ar-char-eye" cx="166" cy="58" r="3" fill="#292524"/>
          <circle class="ar-char-eye" cx="182" cy="58" r="3" fill="#292524"/>
          <!-- Front coral accent bumper -->
          <rect x="200" y="71" width="14" height="6" rx="3" fill="#FFB7B2"/>

          <!-- Spinning geometric wheels -->
          <g class="ar-wheel ar-wheel-left">
            <circle cx="114" cy="85" r="13" fill="#FDFCF8" stroke="#292524" stroke-width="3.5"/>
            <line x1="114" y1="76" x2="114" y2="94" stroke="#FFB7B2" stroke-width="2.2" stroke-linecap="round"/>
            <line x1="105" y1="85" x2="123" y2="85" stroke="#292524" stroke-width="2" stroke-linecap="round"/>
          </g>
          <g class="ar-wheel ar-wheel-right">
            <circle cx="184" cy="85" r="13" fill="#FDFCF8" stroke="#292524" stroke-width="3.5"/>
            <line x1="184" y1="76" x2="184" y2="94" stroke="#FFB7B2" stroke-width="2.2" stroke-linecap="round"/>
            <line x1="175" y1="85" x2="193" y2="85" stroke="#292524" stroke-width="2" stroke-linecap="round"/>
          </g>
        </g>
      </svg>
    </div>

    <div class="ar-loader-copy">
      <p class="ar-loader-title">Bringing your design to life...</p>
      <p class="ar-loader-sub">Extracting Canny contours &amp; rendering with Stable Diffusion ControlNet</p>
    </div>

    <div class="ar-progress-track" aria-hidden="true">
      <div class="ar-progress-bar"></div>
    </div>
  </div>
</div>
"""


HOW_IT_WORKS_HTML = """
<section id="ar-how-it-works" class="ar-section">
  <div class="ar-section-header ar-reveal">
    <div class="ar-section-kicker-row">
      <span class="ar-pill-tag ar-pill-sage">02 · Workflow</span>
      <span class="ar-handwritten-kicker">three clean stages</span>
    </div>
    <h2 class="ar-section-title">How AutoRender AI works</h2>
    <p class="ar-section-desc">
      A focused three-stage pipeline connecting your raw sketch directly to local Stable Diffusion ControlNet inference.
    </p>
  </div>

  <div class="ar-steps-grid">
    <article class="ar-info-card ar-card-white ar-reveal">
      <div class="ar-step-top">
        <span class="ar-step-num">01</span>
        <span class="ar-step-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 16V4m0 0-4 4m4-4 4 4"/>
            <path d="M4 17v2a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-2"/>
          </svg>
        </span>
      </div>
      <h3>Upload your sketch</h3>
      <p>
        Drop any vehicle drawing or concept silhouette into the studio. The image is converted to RGB and normalized to 512 × 512.
      </p>
    </article>

    <article class="ar-info-card ar-card-lavender ar-reveal">
      <div class="ar-step-top">
        <span class="ar-step-num">02</span>
        <span class="ar-step-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
            <rect x="4" y="4" width="16" height="16" rx="3"/>
            <path d="M8 15c2-4 5-6 8-6"/>
            <circle cx="8" cy="15" r="1.2" fill="currentColor"/>
            <circle cx="16" cy="9" r="1.2" fill="currentColor"/>
          </svg>
        </span>
      </div>
      <h3>AI processes the sketch</h3>
      <p>
        OpenCV converts the sketch to grayscale, smooths noise with Gaussian blur, and extracts crisp structural contours via Canny edge detection.
      </p>
    </article>

    <article class="ar-info-card ar-card-sage ar-reveal">
      <div class="ar-step-top">
        <span class="ar-step-num">03</span>
        <span class="ar-step-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 3l1.9 5.2L19 10l-5.1 1.8L12 17l-1.9-5.2L5 10l5.1-1.8L12 3z"/>
          </svg>
        </span>
      </div>
      <h3>Generate your realistic vehicle design</h3>
      <p>
        Stable Diffusion and ControlNet Canny synthesize metallic paint, wheels, glass, and studio lighting while respecting your sketch geometry.
      </p>
    </article>
  </div>
</section>
"""


FEATURES_HTML = """
<section id="ar-features" class="ar-section">
  <div class="ar-section-header ar-reveal">
    <div class="ar-section-kicker-row">
      <span class="ar-pill-tag ar-pill-lavender">03 · Capabilities</span>
      <span class="ar-handwritten-kicker">built for automotive ideation</span>
    </div>
    <h2 class="ar-section-title">Studio capabilities</h2>
    <p class="ar-section-desc">
      Every control in the studio maps directly to the underlying computer vision and generative rendering pipeline.
    </p>
  </div>

  <div class="ar-features-grid">
    <article class="ar-feature-card ar-reveal">
      <div class="ar-feature-icon ar-icon-coral" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 18 15 7l2 2L6 20H4v-2Z"/>
          <path d="M13.5 8.5 15.5 6.5a1.4 1.4 0 0 1 2 2l-2 2"/>
        </svg>
      </div>
      <h3>Sketch-to-image generation</h3>
      <p>
        Turn quick perspective or side-profile automotive sketches into 512 × 512 photorealistic vehicle renders ready for immediate PNG download.
      </p>
    </article>

    <article class="ar-feature-card ar-reveal">
      <div class="ar-feature-icon ar-icon-sage" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 15.5c2.5-5.5 6.5-7.5 10.5-7.5 2.4 0 4.2.8 5.5 2"/>
          <path d="M4 18h16"/>
          <circle cx="8" cy="18" r="2"/>
          <circle cx="16.5" cy="18" r="2"/>
        </svg>
      </div>
      <h3>Edge detection using Canny</h3>
      <p>
        Inspect both the resized original sketch and the extracted Canny edge map side by side to verify structural fidelity.
      </p>
    </article>

    <article class="ar-feature-card ar-reveal">
      <div class="ar-feature-icon ar-icon-lavender" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
          <rect x="5" y="5" width="14" height="14" rx="4"/>
          <path d="M9 12h6M12 9v6"/>
        </svg>
      </div>
      <h3>AI-powered vehicle rendering</h3>
      <p>
        Runs Stable Diffusion v1.5 paired with ControlNet Canny FP16 and UniPC multistep scheduling with automatic automotive studio defaults.
      </p>
    </article>

    <article class="ar-feature-card ar-reveal">
      <div class="ar-feature-icon ar-icon-coral" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">
          <line x1="4" y1="7" x2="20" y2="7"/>
          <circle cx="9" cy="7" r="2" fill="#FDFCF8"/>
          <line x1="4" y1="12" x2="20" y2="12"/>
          <circle cx="15" cy="12" r="2" fill="#FDFCF8"/>
          <line x1="4" y1="17" x2="20" y2="17"/>
          <circle cx="11" cy="17" r="2" fill="#FDFCF8"/>
        </svg>
      </div>
      <h3>Adjustable generation parameters</h3>
      <p>
        Dial in Inference Steps (5–30), Guidance Scale (1–15), ControlNet Strength (0.1–1.5), custom prompts, and reproducible Seed values.
      </p>
    </article>
  </div>
</section>
"""


FAQ_HTML = """
<section id="ar-faq" class="ar-section ar-faq-section">
  <div class="ar-section-header ar-reveal">
    <div class="ar-section-kicker-row">
      <span class="ar-pill-tag ar-pill-coral">04 · About &amp; FAQ</span>
      <span class="ar-handwritten-kicker">workflow guide</span>
    </div>
    <h2 class="ar-section-title">Questions about the studio</h2>
    <p class="ar-section-desc">
      Clear answers on how AutoRender AI processes your sketches and what each parameter controls.
    </p>
  </div>

  <div class="ar-faq-list ar-reveal">
    <div class="ar-faq-item">
      <button type="button" class="ar-faq-trigger" aria-expanded="false">
        <span>How does AutoRender AI prepare my uploaded sketch?</span>
        <span class="ar-faq-plus" aria-hidden="true">+</span>
      </button>
      <div class="ar-faq-panel" hidden>
        <p>
          Your uploaded sketch is converted to RGB and resized to 512 × 512 pixels. OpenCV then converts it to grayscale, applies a 5 × 5 Gaussian blur to reduce noise, and runs Canny edge detection (thresholds 50 and 150) to produce the structural edge map shown in the inspection panel.
        </p>
      </div>
    </div>

    <div class="ar-faq-item">
      <button type="button" class="ar-faq-trigger" aria-expanded="false">
        <span>What happens if I leave the rendering prompt blank?</span>
        <span class="ar-faq-plus" aria-hidden="true">+</span>
      </button>
      <div class="ar-faq-panel" hidden>
        <p>
          If the prompt field is empty, the studio automatically uses a built-in automotive prompt describing a photorealistic modern sports car with metallic paint, detailed headlights, realistic wheels, and studio lighting, paired with negative prompts that avoid cartoon artifacts or deformed wheels.
        </p>
      </div>
    </div>

    <div class="ar-faq-item">
      <button type="button" class="ar-faq-trigger" aria-expanded="false">
        <span>How do ControlNet Strength, Guidance Scale, and Inference Steps work?</span>
        <span class="ar-faq-plus" aria-hidden="true">+</span>
      </button>
      <div class="ar-faq-panel" hidden>
        <p>
          <strong>ControlNet Strength (0.1–1.5)</strong> controls how closely the render adheres to your Canny edge lines. <strong>Guidance Scale (1–15)</strong> adjusts how strongly the model follows your text prompt. <strong>Inference Steps (5–30)</strong> sets the number of UniPC denoising steps used to refine surface detail.
        </p>
      </div>
    </div>

    <div class="ar-faq-item">
      <button type="button" class="ar-faq-trigger" aria-expanded="false">
        <span>How do I reproduce or download a generated vehicle render?</span>
        <span class="ar-faq-plus" aria-hidden="true">+</span>
      </button>
      <div class="ar-faq-panel" hidden>
        <p>
          Keep the same <strong>Generation Seed</strong> value to reproduce consistent renders while iterating on prompts or slider values, or change the seed for a fresh variation. Once generation completes, click <strong>Download Generated Vehicle</strong> to save the rendered PNG directly.
        </p>
      </div>
    </div>
  </div>
</section>
"""


FOOTER_HTML = """
<footer class="ar-footer">
  <div class="ar-footer-inner">
    <div class="ar-footer-brand">
      <span class="ar-brand-badge ar-brand-badge-sm" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M3.5 14.5h17l-1.6-4.2a2.5 2.5 0 0 0-2.3-1.6H8.8a3 3 0 0 0-2.4 1.2L3.5 14.5Z"/>
          <circle cx="7.5" cy="15.5" r="1.7"/>
          <circle cx="16.5" cy="15.5" r="1.7"/>
        </svg>
      </span>
      <div>
        <strong class="ar-footer-title">AutoRender AI</strong>
        <p class="ar-footer-note">Sketch-to-photorealistic automotive rendering studio powered by Stable Diffusion &amp; ControlNet.</p>
      </div>
    </div>
    <div class="ar-footer-links">
      <button type="button" class="ar-footer-link" data-scroll-target="ar-hero">Back to top</button>
      <button type="button" class="ar-footer-link" data-scroll-target="ar-studio">Open studio</button>
      <button type="button" class="ar-footer-link" data-scroll-target="ar-how-it-works">Workflow</button>
    </div>
  </div>
</footer>
"""


APP_CSS = """
:root,
.dark,
body,
.gradio-container {
  --ar-bg: #FDFCF8;
  --ar-coral: #FFB7B2;
  --ar-coral-hover: #FFA39D;
  --ar-coral-soft: rgba(255, 183, 178, 0.24);
  --ar-sage: #E8EFE8;
  --ar-lavender: #EFEDF4;
  --ar-ink: #292524;
  --ar-muted: #78716C;
  --ar-white: #FFFFFF;
  --ar-border: rgba(41, 37, 36, 0.085);
  --ar-border-strong: rgba(41, 37, 36, 0.15);
  color-scheme: light !important;
  --body-background-fill: #FDFCF8 !important;
  --background-fill-primary: #FDFCF8 !important;
  --background-fill-secondary: #FFFFFF !important;
  --block-background-fill: #FFFFFF !important;
  --body-text-color: #292524 !important;
  --body-text-color-subdued: #78716C !important;
  --color-accent: #FFB7B2 !important;
}

html {
  scroll-behavior: smooth;
  background-color: #FDFCF8 !important;
}

body {
  background-color: #FDFCF8 !important;
  color: #292524 !important;
  font-family: 'Outfit', ui-sans-serif, system-ui, -apple-system, sans-serif !important;
  overflow-x: hidden !important;
}

.gradio-container {
  background: transparent !important;
  max-width: 1280px !important;
  margin: 0 auto !important;
  padding: 0 20px 48px 20px !important;
  position: relative;
  z-index: 1;
}

.gradio-container .main,
.gradio-container .wrap {
  max-width: 100% !important;
}

/* Remove extra padding on pure HTML wrapper hosts */
#ar-ambient-host,
#ar-nav-host,
#ar-hero-host,
#ar-loader-host,
#ar-how-host,
#ar-features-host,
#ar-faq-host,
#ar-footer-host,
#ar-studio-header-host {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

/* Grain texture overlay */
.ar-grain-overlay {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9998;
  opacity: 0.032;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.82' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 220px 220px;
}

/* Soft ambient floating shapes */
.ar-ambient-layer {
  position: fixed;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}

.ar-blob {
  position: absolute;
  border-radius: 9999px;
  filter: blur(80px);
  opacity: 0.55;
  will-change: transform;
}

.ar-blob-coral {
  width: 420px;
  height: 420px;
  top: -80px;
  right: -90px;
  background: #FFB7B2;
  opacity: 0.34;
  animation: arFloatSlow 18s ease-in-out infinite;
}

.ar-blob-lavender {
  width: 460px;
  height: 460px;
  top: 260px;
  left: -140px;
  background: #EFEDF4;
  opacity: 0.9;
  animation: arFloatSlow 22s ease-in-out infinite reverse;
}

.ar-blob-sage {
  width: 360px;
  height: 360px;
  bottom: 40px;
  right: 8%;
  background: #E8EFE8;
  opacity: 0.72;
  animation: arFloatSlow 25s ease-in-out infinite;
}

@keyframes arFloatSlow {
  0%, 100% { transform: translate3d(0, 0, 0) scale(1); }
  50% { transform: translate3d(18px, -24px, 0) scale(1.05); }
}

/* Floating pill navigation */
.ar-nav-shell {
  position: fixed;
  top: 18px;
  left: 50%;
  transform: translateX(-50%);
  width: calc(100% - 32px);
  max-width: 960px;
  z-index: 9000;
}

.ar-nav-pill {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 10px 12px 10px 16px;
  background: rgba(255, 255, 255, 0.78);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border: 1px solid rgba(41, 37, 36, 0.08);
  border-radius: 9999px;
  box-shadow: 0 10px 32px rgba(41, 37, 36, 0.06);
}

.ar-brand {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: #292524;
  font-weight: 600;
  font-size: 1rem;
  letter-spacing: -0.02em;
  flex-shrink: 0;
}

.ar-brand-badge {
  width: 34px;
  height: 34px;
  border-radius: 9999px;
  background: #FFB7B2;
  color: #292524;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.45);
  transition: transform 0.3s ease;
}

.ar-brand-badge svg {
  width: 18px;
  height: 18px;
}

.ar-brand:hover .ar-brand-badge {
  transform: scale(1.05);
}

.ar-nav-links {
  display: flex;
  align-items: center;
  gap: 6px;
}

.ar-nav-link {
  background: transparent;
  border: none;
  color: #78716C;
  font-family: 'Outfit', sans-serif;
  font-size: 0.93rem;
  font-weight: 500;
  padding: 8px 14px;
  border-radius: 9999px;
  cursor: pointer;
  transition: color 0.25s ease, background-color 0.25s ease;
}

.ar-nav-link:hover {
  color: #292524;
  background: rgba(239, 237, 244, 0.8);
}

.ar-nav-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.ar-nav-cta {
  background: #292524;
  color: #FDFCF8;
  border: none;
  border-radius: 9999px;
  padding: 10px 20px;
  font-family: 'Outfit', sans-serif;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: transform 0.25s ease, background-color 0.25s ease;
}

.ar-nav-cta:hover {
  background: #3B3634;
  transform: scale(1.02);
}

.ar-nav-toggle {
  display: none;
  width: 38px;
  height: 38px;
  border-radius: 9999px;
  border: 1px solid rgba(41, 37, 36, 0.12);
  background: #FFFFFF;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 5px;
  cursor: pointer;
  padding: 0;
}

.ar-nav-toggle span {
  display: block;
  width: 16px;
  height: 1.6px;
  background: #292524;
  border-radius: 2px;
  transition: transform 0.25s ease;
}

.ar-mobile-menu {
  margin-top: 10px;
  padding: 14px;
  background: rgba(255, 255, 255, 0.94);
  backdrop-filter: blur(18px);
  border: 1px solid rgba(41, 37, 36, 0.08);
  border-radius: 24px;
  box-shadow: 0 18px 40px rgba(41, 37, 36, 0.1);
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.ar-mobile-menu[hidden] {
  display: none !important;
}

.ar-mobile-link,
.ar-mobile-cta {
  width: 100%;
  text-align: left;
  font-family: 'Outfit', sans-serif;
  font-size: 0.98rem;
  font-weight: 500;
  padding: 11px 16px;
  border-radius: 14px;
  border: none;
  cursor: pointer;
}

.ar-mobile-link {
  background: transparent;
  color: #292524;
}

.ar-mobile-link:hover {
  background: #EFEDF4;
}

.ar-mobile-cta {
  margin-top: 4px;
  text-align: center;
  background: #292524;
  color: #FDFCF8;
  border-radius: 9999px;
}

/* Hero Section */
.ar-hero {
  padding: 124px 0 56px 0;
  position: relative;
}

.ar-hero-inner {
  max-width: 960px;
  margin: 0 auto;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.ar-hero-kicker {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 7px 16px;
  border-radius: 9999px;
  background: #E8EFE8;
  color: #292524;
  font-size: 0.86rem;
  font-weight: 500;
  border: 1px solid rgba(41, 37, 36, 0.06);
  margin-bottom: 24px;
}

.ar-kicker-dot {
  width: 8px;
  height: 8px;
  border-radius: 9999px;
  background: #FFB7B2;
}

.ar-hero-title {
  font-family: 'Outfit', sans-serif;
  font-size: clamp(2.65rem, 6vw, 4.7rem);
  font-weight: 600;
  line-height: 1.06;
  letter-spacing: -0.035em;
  color: #292524;
  margin: 0 0 22px 0;
  max-width: 820px;
}

.ar-hero-accent-wrap {
  position: relative;
  display: inline-block;
  padding: 0 4px;
}

.ar-handwritten-word {
  font-family: 'Reenie Beanie', cursive;
  font-weight: 500;
  font-size: 1.24em;
  letter-spacing: 0;
  color: #292524;
  display: inline-block;
  transform: rotate(-1.5deg);
}

.ar-underline-svg {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0.04em;
  width: 100%;
  height: 14px;
  pointer-events: none;
}

.ar-hero-subtitle {
  font-size: clamp(1.05rem, 2vw, 1.24rem);
  line-height: 1.65;
  color: #78716C;
  max-width: 620px;
  margin: 0 0 34px 0;
  font-weight: 400;
}

.ar-hero-ctas {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 14px;
  margin-bottom: 52px;
}

.ar-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  border-radius: 9999px;
  padding: 14px 28px;
  font-family: 'Outfit', sans-serif;
  font-size: 0.98rem;
  font-weight: 500;
  cursor: pointer;
  transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1), background-color 0.25s ease, box-shadow 0.25s ease;
}

.ar-btn svg {
  width: 17px;
  height: 17px;
}

.ar-btn-coral {
  background: #FFB7B2;
  color: #292524;
  border: 1px solid rgba(41, 37, 36, 0.06);
  box-shadow: 0 10px 24px rgba(255, 183, 178, 0.38);
}

.ar-btn-coral:hover {
  background: #FFA39D;
  transform: scale(1.02) translateY(-1px);
  box-shadow: 0 14px 30px rgba(255, 183, 178, 0.48);
}

.ar-btn-outline {
  background: #FFFFFF;
  color: #292524;
  border: 1px solid rgba(41, 37, 36, 0.14);
}

.ar-btn-outline:hover {
  background: #EFEDF4;
  transform: scale(1.02) translateY(-1px);
}

/* Hero Automotive Showcase */
.ar-hero-showcase {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 16px;
  background: #FFFFFF;
  border: 1px solid rgba(41, 37, 36, 0.08);
  border-radius: 30px;
  padding: 20px;
  box-shadow: 0 20px 55px rgba(41, 37, 36, 0.055);
}

.ar-showcase-panel {
  border-radius: 22px;
  padding: 18px 18px 14px 18px;
  text-align: left;
  transition: transform 0.35s ease;
}

.ar-showcase-panel:hover {
  transform: translateY(-2px);
}

.ar-showcase-sketch {
  background: #EFEDF4;
}

.ar-showcase-render {
  background: #E8EFE8;
}

.ar-showcase-tag {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  font-weight: 500;
  color: #292524;
  margin-bottom: 6px;
}

.ar-tag-dot {
  width: 8px;
  height: 8px;
  border-radius: 9999px;
}

.ar-dot-stone { background: #292524; }
.ar-dot-coral { background: #FFB7B2; }

.ar-handwritten-note {
  margin-left: auto;
  font-family: 'Reenie Beanie', cursive;
  font-size: 1.35rem;
  color: #78716C;
  line-height: 1;
}

.ar-car-svg {
  width: 100%;
  height: auto;
  display: block;
}

.ar-showcase-bridge {
  display: flex;
  align-items: center;
  justify-content: center;
}

.ar-bridge-pill {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 14px 12px;
  border-radius: 20px;
  background: #FDFCF8;
  border: 1px solid rgba(41, 37, 36, 0.08);
}

.ar-bridge-icon {
  width: 36px;
  height: 36px;
  border-radius: 9999px;
  background: #FFB7B2;
  color: #292524;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ar-bridge-icon svg {
  width: 18px;
  height: 18px;
}

.ar-bridge-label {
  font-size: 0.78rem;
  font-weight: 500;
  color: #78716C;
  white-space: nowrap;
}

/* Section Headers */
.ar-section {
  padding: 72px 0 18px 0;
}

.ar-section-header {
  max-width: 680px;
  margin: 0 auto 36px auto;
  text-align: center;
}

#ar-studio-header-host .ar-section-header {
  margin-top: 32px;
  margin-bottom: 28px;
}

.ar-section-kicker-row {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 14px;
}

.ar-pill-tag {
  display: inline-flex;
  align-items: center;
  padding: 6px 14px;
  border-radius: 9999px;
  font-size: 0.82rem;
  font-weight: 500;
  color: #292524;
}

.ar-pill-coral { background: #FFB7B2; }
.ar-pill-sage { background: #E8EFE8; }
.ar-pill-lavender { background: #EFEDF4; }

.ar-handwritten-kicker {
  font-family: 'Reenie Beanie', cursive;
  font-size: 1.55rem;
  color: #78716C;
  line-height: 1;
}

.ar-section-title {
  font-family: 'Outfit', sans-serif;
  font-size: clamp(1.9rem, 3.6vw, 2.75rem);
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1.12;
  color: #292524;
  margin: 0 0 12px 0;
}

.ar-section-desc {
  font-size: 1.03rem;
  line-height: 1.65;
  color: #78716C;
  margin: 0;
}

/* Studio Layout Cards */
#ar-studio-row {
  gap: 24px !important;
  align-items: stretch !important;
}

#ar-studio-left,
#ar-studio-right {
  display: flex !important;
  flex-direction: column !important;
  gap: 20px !important;
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  box-shadow: none !important;
}

.ar-studio-card {
  background: #FFFFFF !important;
  border: 1px solid rgba(41, 37, 36, 0.085) !important;
  border-radius: 26px !important;
  padding: 22px !important;
  box-shadow: 0 12px 36px rgba(41, 37, 36, 0.045) !important;
  transition: box-shadow 0.3s ease, transform 0.3s ease !important;
  gap: 14px !important;
}

.ar-studio-card-lavender {
  background: #EFEDF4 !important;
  border-color: rgba(41, 37, 36, 0.06) !important;
}

.ar-studio-card-sage {
  background: #E8EFE8 !important;
  border-color: rgba(41, 37, 36, 0.06) !important;
}

.ar-studio-card-featured {
  background: #FFFFFF !important;
  border: 1px solid rgba(41, 37, 36, 0.1) !important;
  box-shadow: 0 20px 52px rgba(41, 37, 36, 0.065) !important;
}

.ar-card-head-html {
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
  margin: 0 !important;
}

.ar-card-head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid rgba(41, 37, 36, 0.08);
}

.ar-card-step {
  display: block;
  font-size: 0.78rem;
  font-weight: 500;
  color: #78716C;
  margin-bottom: 2px;
}

.ar-card-title {
  font-family: 'Outfit', sans-serif;
  font-size: 1.2rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: #292524;
  margin: 0;
}

.ar-card-badge {
  font-size: 0.78rem;
  font-weight: 500;
  color: #292524;
  background: #FDFCF8;
  border: 1px solid rgba(41, 37, 36, 0.09);
  padding: 5px 12px;
  border-radius: 9999px;
  white-space: nowrap;
}

.ar-badge-coral {
  background: #FFB7B2;
  border-color: transparent;
}

.ar-handwritten-mini {
  font-family: 'Reenie Beanie', cursive;
  font-size: 1.45rem;
  color: #78716C;
  line-height: 1;
}

/* Native Gradio Component Refinement inside Studio */
.ar-studio-card .block {
  background: #FFFFFF !important;
  border: 1px solid rgba(41, 37, 36, 0.08) !important;
  border-radius: 18px !important;
  box-shadow: none !important;
}

.ar-studio-card-lavender .block {
  background: rgba(255, 255, 255, 0.86) !important;
}

.ar-studio-card-sage .block {
  background: rgba(255, 255, 255, 0.9) !important;
}

.ar-studio-card label,
.ar-studio-card .label-wrap span,
.ar-studio-card [data-testid="block-label"] {
  font-family: 'Outfit', sans-serif !important;
  font-weight: 500 !important;
  color: #292524 !important;
  font-size: 0.88rem !important;
}

.ar-studio-card textarea,
.ar-studio-card input[type="text"],
.ar-studio-card input[type="number"] {
  font-family: 'Outfit', sans-serif !important;
  background: #FDFCF8 !important;
  color: #292524 !important;
  border-radius: 14px !important;
  border: 1px solid rgba(41, 37, 36, 0.12) !important;
  font-size: 0.95rem !important;
}

.ar-studio-card textarea:focus,
.ar-studio-card input[type="text"]:focus,
.ar-studio-card input[type="number"]:focus {
  border-color: #FFB7B2 !important;
  box-shadow: 0 0 0 3px rgba(255, 183, 178, 0.25) !important;
}

/* Sliders */
.ar-studio-card input[type="range"] {
  accent-color: #FFB7B2 !important;
}

/* Image upload & preview containers */
#ar-sketch-upload,
#ar-generated-output,
#ar-original-preview,
#ar-edges-preview {
  border-radius: 20px !important;
  overflow: hidden !important;
}

#ar-generated-output {
  background: #FDFCF8 !important;
  border: 1px solid rgba(41, 37, 36, 0.1) !important;
}

/* Primary Generate Button */
#ar-generate-btn {
  background: #FFB7B2 !important;
  color: #292524 !important;
  border: 1px solid rgba(41, 37, 36, 0.08) !important;
  border-radius: 9999px !important;
  padding: 14px 24px !important;
  min-height: 52px !important;
  font-family: 'Outfit', sans-serif !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
  letter-spacing: -0.01em !important;
  box-shadow: 0 10px 24px rgba(255, 183, 178, 0.4) !important;
  transition: transform 0.25s ease, background-color 0.25s ease, box-shadow 0.25s ease !important;
}

#ar-generate-btn:hover {
  background: #FFA39D !important;
  transform: scale(1.015) translateY(-1px) !important;
  box-shadow: 0 14px 28px rgba(255, 183, 178, 0.5) !important;
}

/* Action Bar: Status & Download Button */
#ar-action-row {
  gap: 14px !important;
  align-items: stretch !important;
}

#ar-status-box {
  background: #FDFCF8 !important;
}

#ar-download-btn,
#ar-download-btn button,
#ar-download-btn a {
  background: #292524 !important;
  color: #FDFCF8 !important;
  border-radius: 9999px !important;
  border: none !important;
  font-family: 'Outfit', sans-serif !important;
  font-weight: 500 !important;
  min-height: 48px !important;
  transition: transform 0.25s ease, background-color 0.25s ease !important;
}

#ar-download-btn:hover,
#ar-download-btn button:hover,
#ar-download-btn a:hover {
  background: #3D3836 !important;
  transform: scale(1.02) !important;
}

#ar-inspect-row {
  gap: 14px !important;
}

/* Custom Character Speed Loader Overlay */
.ar-loader-overlay {
  position: fixed;
  inset: 0;
  z-index: 9995;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  background: rgba(253, 252, 248, 0.88);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.35s ease, visibility 0.35s ease;
}

.ar-loader-overlay.is-active {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.ar-loader-card {
  width: 100%;
  max-width: 440px;
  background: #FFFFFF;
  border: 1px solid rgba(41, 37, 36, 0.09);
  border-radius: 32px;
  padding: 32px 28px 28px 28px;
  box-shadow: 0 28px 70px rgba(41, 37, 36, 0.12);
  text-align: center;
  transform: translateY(10px) scale(0.98);
  transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1);
}

.ar-loader-overlay.is-active .ar-loader-card {
  transform: translateY(0) scale(1);
}

.ar-speed-stage {
  background: #FDFCF8;
  border: 1px solid rgba(41, 37, 36, 0.06);
  border-radius: 22px;
  padding: 16px 12px 10px 12px;
  margin-bottom: 20px;
  overflow: hidden;
}

.ar-speed-svg {
  width: 100%;
  max-width: 300px;
  height: auto;
  display: block;
  margin: 0 auto;
}

.ar-runner-char {
  transform-origin: 150px 75px;
  animation: arCharMotion 1.15s ease-in-out infinite;
}

.ar-wheel {
  animation: arWheelSpin 0.75s linear infinite;
}

.ar-wheel-left { transform-origin: 114px 85px; }
.ar-wheel-right { transform-origin: 184px 85px; }

.ar-speed-line {
  animation: arSpeedStreak 0.9s linear infinite;
}
.ar-sl-1 { animation-delay: 0s; animation-duration: 0.78s; }
.ar-sl-2 { animation-delay: -0.25s; animation-duration: 0.95s; }
.ar-sl-3 { animation-delay: -0.5s; animation-duration: 0.72s; }
.ar-sl-4 { animation-delay: -0.15s; animation-duration: 1.05s; }
.ar-sl-5 { animation-duration: 1.2s; }

@keyframes arCharMotion {
  0%, 100% { transform: translate3d(-4px, 0px, 0) rotate(-1.2deg); }
  50% { transform: translate3d(5px, -3px, 0) rotate(1.2deg); }
}

@keyframes arWheelSpin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes arSpeedStreak {
  0% { transform: translateX(35px); opacity: 0; }
  25% { opacity: 0.95; }
  80% { opacity: 0.85; }
  100% { transform: translateX(-160px); opacity: 0; }
}

.ar-loader-title {
  font-family: 'Outfit', sans-serif;
  font-size: 1.32rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: #292524;
  margin: 0 0 6px 0;
}

.ar-loader-sub {
  font-size: 0.92rem;
  line-height: 1.5;
  color: #78716C;
  margin: 0 0 20px 0;
}

.ar-progress-track {
  width: 100%;
  height: 7px;
  border-radius: 9999px;
  background: #EFEDF4;
  overflow: hidden;
  position: relative;
}

.ar-progress-bar {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 38%;
  border-radius: 9999px;
  background: linear-gradient(90deg, #FFB7B2 0%, #292524 100%);
  animation: arIndeterminate 1.5s cubic-bezier(0.45, 0.05, 0.55, 0.95) infinite;
}

@keyframes arIndeterminate {
  0% { left: -40%; }
  100% { left: 105%; }
}

/* How It Works & Features Cards */
.ar-steps-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 20px;
}

.ar-features-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 20px;
}

.ar-info-card,
.ar-feature-card {
  border-radius: 26px;
  padding: 28px;
  border: 1px solid rgba(41, 37, 36, 0.08);
  transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.35s ease;
}

.ar-info-card:hover,
.ar-feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 42px rgba(41, 37, 36, 0.06);
}

.ar-card-white { background: #FFFFFF; }
.ar-card-lavender { background: #EFEDF4; }
.ar-card-sage { background: #E8EFE8; }
.ar-feature-card { background: #FFFFFF; }

.ar-step-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 22px;
}

.ar-step-num {
  font-family: 'Reenie Beanie', cursive;
  font-size: 2.1rem;
  color: #292524;
  line-height: 1;
}

.ar-step-icon,
.ar-feature-icon {
  width: 44px;
  height: 44px;
  border-radius: 15px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: #292524;
}

.ar-step-icon {
  background: rgba(255, 255, 255, 0.82);
  border: 1px solid rgba(41, 37, 36, 0.07);
}

.ar-icon-coral { background: #FFB7B2; }
.ar-icon-sage { background: #E8EFE8; }
.ar-icon-lavender { background: #EFEDF4; }

.ar-step-icon svg,
.ar-feature-icon svg {
  width: 21px;
  height: 21px;
}

.ar-feature-icon {
  margin-bottom: 18px;
}

.ar-info-card h3,
.ar-feature-card h3 {
  font-family: 'Outfit', sans-serif;
  font-size: 1.22rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: #292524;
  margin: 0 0 10px 0;
}

.ar-info-card p,
.ar-feature-card p {
  font-size: 0.96rem;
  line-height: 1.65;
  color: #78716C;
  margin: 0;
}

/* FAQ Accordion */
.ar-faq-list {
  max-width: 820px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.ar-faq-item {
  background: #FFFFFF;
  border: 1px solid rgba(41, 37, 36, 0.085);
  border-radius: 22px;
  overflow: hidden;
  transition: background-color 0.25s ease, border-color 0.25s ease;
}

.ar-faq-item.is-open {
  background: #EFEDF4;
  border-color: rgba(41, 37, 36, 0.12);
}

.ar-faq-trigger {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 20px 24px;
  background: transparent;
  border: none;
  text-align: left;
  font-family: 'Outfit', sans-serif;
  font-size: 1.04rem;
  font-weight: 500;
  color: #292524;
  cursor: pointer;
}

.ar-faq-plus {
  width: 30px;
  height: 30px;
  border-radius: 9999px;
  background: #FDFCF8;
  border: 1px solid rgba(41, 37, 36, 0.1);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.15rem;
  line-height: 1;
  flex-shrink: 0;
  transition: transform 0.3s ease, background-color 0.25s ease;
}

.ar-faq-item.is-open .ar-faq-plus {
  transform: rotate(45deg);
  background: #FFB7B2;
  border-color: transparent;
}

.ar-faq-panel {
  padding: 0 24px 22px 24px;
}

.ar-faq-panel[hidden] {
  display: none !important;
}

.ar-faq-panel p {
  margin: 0;
  font-size: 0.96rem;
  line-height: 1.65;
  color: #78716C;
}

.ar-faq-panel strong {
  color: #292524;
  font-weight: 600;
}

/* Footer */
.ar-footer {
  margin-top: 64px;
  padding-top: 12px;
}

.ar-footer-inner {
  background: #FFFFFF;
  border: 1px solid rgba(41, 37, 36, 0.08);
  border-radius: 26px;
  padding: 24px 28px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
}

.ar-footer-brand {
  display: flex;
  align-items: center;
  gap: 14px;
}

.ar-brand-badge-sm {
  width: 36px;
  height: 36px;
  flex-shrink: 0;
}

.ar-footer-title {
  display: block;
  font-size: 1rem;
  font-weight: 600;
  color: #292524;
}

.ar-footer-note {
  margin: 2px 0 0 0;
  font-size: 0.88rem;
  color: #78716C;
}

.ar-footer-links {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.ar-footer-link {
  background: #FDFCF8;
  border: 1px solid rgba(41, 37, 36, 0.1);
  border-radius: 9999px;
  padding: 8px 16px;
  font-family: 'Outfit', sans-serif;
  font-size: 0.86rem;
  font-weight: 500;
  color: #292524;
  cursor: pointer;
  transition: background-color 0.25s ease;
}

.ar-footer-link:hover {
  background: #FFB7B2;
  border-color: transparent;
}

/* Scroll Reveal Animations */
.ar-reveal {
  opacity: 0;
  transform: translateY(26px);
  transition: opacity 0.8s cubic-bezier(0.22, 1, 0.36, 1), transform 0.8s cubic-bezier(0.22, 1, 0.36, 1);
}

.ar-reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
}

/* Gradio footer subtle blending */
footer.svelte-1rjryqp,
.gradio-container > footer {
  margin-top: 16px !important;
  opacity: 0.72;
  font-family: 'Outfit', sans-serif !important;
}

/* Responsive Breakpoints */
@media (max-width: 960px) {
  .ar-hero-showcase {
    grid-template-columns: 1fr;
    gap: 14px;
  }

  .ar-bridge-pill {
    flex-direction: row;
    padding: 8px 16px;
  }

  .ar-bridge-icon svg {
    transform: rotate(90deg);
  }

  .ar-steps-grid {
    grid-template-columns: 1fr;
  }

  .ar-features-grid {
    grid-template-columns: 1fr;
  }

  #ar-studio-row {
    flex-direction: column !important;
  }
}

@media (max-width: 768px) {
  .gradio-container {
    padding: 0 14px 36px 14px !important;
  }

  .ar-nav-links,
  .ar-nav-cta {
    display: none;
  }

  .ar-nav-toggle {
    display: inline-flex;
  }

  .ar-hero {
    padding: 108px 0 36px 0;
  }

  .ar-studio-card {
    padding: 16px !important;
    border-radius: 22px !important;
  }

  #ar-inspect-row,
  #ar-action-row {
    flex-direction: column !important;
  }

  .ar-card-head {
    flex-direction: column;
    align-items: flex-start;
  }
}

/* Respect reduced motion preferences */
@media (prefers-reduced-motion: reduce) {
  html {
    scroll-behavior: auto;
  }

  .ar-blob,
  .ar-runner-char,
  .ar-wheel,
  .ar-speed-line,
  .ar-progress-bar {
    animation: none !important;
  }

  .ar-reveal {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }

  .ar-btn,
  .ar-info-card,
  .ar-feature-card,
  .ar-loader-overlay,
  .ar-loader-card {
    transition: none !important;
  }
}
"""


APP_JS = """
function initAutoRenderUI() {
  if (window.__arInitialized) return;
  window.__arInitialized = true;

  // Smooth scrolling for nav pills, hero CTAs, and footer buttons
  document.addEventListener('click', (event) => {
    const scrollEl = event.target.closest('[data-scroll-target]');
    if (scrollEl) {
      event.preventDefault();
      const targetId = scrollEl.getAttribute('data-scroll-target');
      const target = document.getElementById(targetId);
      if (target) {
        const yOffset = -88;
        const y = target.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({
          top: Math.max(0, y),
          behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'
        });
      }
      const mobileMenu = document.getElementById('ar-mobile-menu');
      const toggleBtn = document.getElementById('ar-nav-toggle');
      if (mobileMenu && !mobileMenu.hasAttribute('hidden')) {
        mobileMenu.setAttribute('hidden', '');
        if (toggleBtn) toggleBtn.setAttribute('aria-expanded', 'false');
      }
      return;
    }

    // Mobile navbar toggle
    const toggle = event.target.closest('#ar-nav-toggle');
    if (toggle) {
      const mobileMenu = document.getElementById('ar-mobile-menu');
      if (mobileMenu) {
        const isHidden = mobileMenu.hasAttribute('hidden');
        if (isHidden) {
          mobileMenu.removeAttribute('hidden');
          toggle.setAttribute('aria-expanded', 'true');
        } else {
          mobileMenu.setAttribute('hidden', '');
          toggle.setAttribute('aria-expanded', 'false');
        }
      }
      return;
    }

    // Minimal FAQ accordion
    const faqTrigger = event.target.closest('.ar-faq-trigger');
    if (faqTrigger) {
      const item = faqTrigger.closest('.ar-faq-item');
      const panel = item ? item.querySelector('.ar-faq-panel') : null;
      if (!item || !panel) return;
      const isOpen = faqTrigger.getAttribute('aria-expanded') === 'true';

      document.querySelectorAll('.ar-faq-item.is-open').forEach((openItem) => {
        if (openItem !== item) {
          openItem.classList.remove('is-open');
          const btn = openItem.querySelector('.ar-faq-trigger');
          const pnl = openItem.querySelector('.ar-faq-panel');
          if (btn) btn.setAttribute('aria-expanded', 'false');
          if (pnl) pnl.setAttribute('hidden', '');
        }
      });

      if (isOpen) {
        item.classList.remove('is-open');
        faqTrigger.setAttribute('aria-expanded', 'false');
        panel.setAttribute('hidden', '');
      } else {
        item.classList.add('is-open');
        faqTrigger.setAttribute('aria-expanded', 'true');
        panel.removeAttribute('hidden');
      }
    }
  });

  // Scroll-reveal observer (0.8s translateY + opacity)
  const revealEls = () => document.querySelectorAll('.ar-reveal:not(.is-visible)');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (reducedMotion || !('IntersectionObserver' in window)) {
    revealEls().forEach((el) => el.classList.add('is-visible'));
  } else {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -30px 0px' }
    );

    const observeAll = () => revealEls().forEach((el) => observer.observe(el));
    observeAll();
    // Re-check briefly after Gradio hydrates any async blocks
    setTimeout(observeAll, 250);
    setTimeout(observeAll, 800);
  }

  // Custom Processing Loader controls (shown only during active generation)
  window.arShowLoader = function () {
    const overlay = document.getElementById('ar-loader-overlay');
    if (overlay) {
      overlay.classList.add('is-active');
      overlay.setAttribute('aria-hidden', 'false');
    }
  };

  window.arHideLoader = function () {
    const overlay = document.getElementById('ar-loader-overlay');
    if (overlay) {
      overlay.classList.remove('is-active');
      overlay.setAttribute('aria-hidden', 'true');
    }
  };

  // Safeguard: hide loader automatically if a Gradio error toast appears
  const toastObserver = new MutationObserver(() => {
    const hasErrorToast = document.querySelector('.toast-wrap .error, .toast-body.error');
    if (hasErrorToast) {
      window.arHideLoader();
    }
  });
  toastObserver.observe(document.body, { childList: true, subtree: true });
}
"""
