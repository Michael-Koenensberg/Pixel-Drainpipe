# Pixel-Drainpipe

Simple Python algorithm for texture generation using accumulation with remainder.

## How it works

Counter num adds DPL each step. When num ≥ 1, it places a white pixel and subtracts 1 (remainder carries over). DPL can randomly change each step.

## Parameters

- `r` — base density (DPL = 2/r)
- `min_rand_DPL` — randomness (1 = no randomness)
- `x`, `y` — image size

## Quick start

```bash
pip install pillow numpy
python script.py
