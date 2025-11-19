# 2D to 3D  README

[![Model Card](https://img.shields.io/badge/%F0%9F%A4%97%20Model_Card-Huggingface-orange)](https://huggingface.co/stabilityai/TripoSR) [![Gradio Demo](https://img.shields.io/badge/%F0%9F%A4%97%20Gradio%20Demo-Huggingface-orange)](https://huggingface.co/spaces/stabilityai/TripoSR) [![Paper](https://img.shields.io/badge/%F0%9F%A4%97%20Paper-Huggingface-orange)](https://huggingface.co/papers/2403.02151) [![ArXiv](https://img.shields.io/badge/Arxiv-2403.02151-B31B1B.svg)](https://arxiv.org/abs/2403.02151)


Overview
--------

This repository implements the 2D3D single-image reconstruction model (research by Tripo AI + Stability AI). It focuses on fast feedforward reconstruction that produces a mesh (OBJ) and either per-vertex colors or a baked texture map from a single input image.

What you'll find here
- `run.py`: command-line inference for one or more images
- `gradio_app.py` / `gradio_single.py`: small local web demos for quick interactive testing
- `models/`: model code, renderers, tokenizers, and supporting modules
- `tsr/`: texture-baking and rendering utilities (`bake_texture.py`, `system.py`)
- `examples/`: sample input images (e.g., `examples/chair.png`)
- `figures/`: assets used in this README

Quick Start
-----------

Requirements
- Python 3.8+
- PyTorch (install the wheel matching your CUDA version): https://pytorch.org/get-started/locally/
- Optional: CUDA for GPU acceleration

Install dependencies

```powershell
pip install --upgrade setuptools
pip install -r requirements.txt
```

Run inference (single image)

```powershell
python run.py examples/chair.png --output-dir output/
```

Notes
- You can pass multiple image paths to `run.py` separated by spaces.
- VRAM usage depends on options; default runs typically require ~6GB (varies by GPU).
- See `python run.py --help` for all available flags.

Texture baking
- Add `--bake-texture` to bake a texture map instead of using per-vertex colors.
- Use `--texture-resolution <N>` to set the baked texture size (e.g., `--texture-resolution 1024`).

Local demo

```powershell
python gradio_app.py
```

Example outputs
---------------
When inference completes, expected files in `--output-dir` include:
- `<basename>_mesh.obj`  reconstructed mesh (OBJ)
- `<basename>_preview.png`  a rendered preview image
- `<basename>_texture.png`  baked texture (if `--bake-texture` used)
- additional metadata files depending on flags

Repository Layout (short)
- `run.py`  CLI inference
- `gradio_app.py`, `gradio_single.py`  demo apps
- `models/`  model implementation and rendering utilities
- `tsr/`  texture baking / helper scripts
- `examples/`  sample inputs
- `figures/`  README/demo images
- `output_test/`  developer/test outputs

Troubleshooting
---------------

Problem: `AttributeError: module 'torchmcubes_module' has no attribute 'mcubes_cuda'` or a message that `torchmcubes` was compiled without CUDA.

Cause: `torchmcubes` was installed/built without CUDA support or PyTorch wheel/CUDA major versions are mismatched.

Quick fix

```powershell
pip install --upgrade setuptools
pip uninstall torchmcubes
pip install git+https://github.com/tatsy/torchmcubes.git
```

Ensure the PyTorch CUDA major version (e.g., CUDA 11.x) matches your installed CUDA and the wheel you installed. If you don't have CUDA, install the CPU-only builds.

Citation
--------

If you use this code or model in your research, please cite:

```bibtex
@article{TripoSR2024,
  title={2D to 3D: Fast 3D Object Reconstruction from a Single Image},
  author={Tochilkin, Dmitry and Pankratz, David and Liu, Zexiang and Huang, Zixuan and Letts, Adam and Li, Yangguang and Liang, Ding and Laforte, Christian and Jampani, Varun and Cao, Yan-Pei},
  journal={arXiv preprint arXiv:2403.02151},
  year={2024}
}
```

License
-------
This project is provided under the MIT license.

