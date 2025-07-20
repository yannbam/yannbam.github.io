# Three.js Croissant

Mathematically identical implementation of the SVG croissant using Three.js.

## Mathematical Parameters
- `R = 70` - major radius of centre-line arc
- `r0 = 20` - maximum half-thickness at u = 0
- `alpha = 1.5` - taper exponent
- `theta = 1.4` - half-opening angle (radians)
- `k = 0.70` - flattening factor of cross-section
- `f(u) = [cos(πu/2θ)]^α` - cross-section scale factor

## Quick Start

```bash
cd ~/project/croissant
python3 -m http.server 8080
# Open http://localhost:8080 in browser
```

## Features
- 100% mathematically identical to the original SVG implementation
- 2D shape rendering (default) matching SVG output
- Optional 3D extrusion (uncomment in code)
- Interactive camera controls (OrbitControls)

## Implementation Details
The `createCroissantShape()` function generates a `THREE.Shape` using the exact same mathematical formulas as the SVG:
1. Outer edge: `(R + r0*f(u)) * [cos(u), sin(u)]` for u ∈ [-θ, +θ]
2. Inner edge: `(R - k*r0*f(u)) * [cos(u), sin(u)]` for u ∈ [+θ, -θ]

## Verification
Access `window.croissantParams` in browser console to inspect all parameters.

## Interactive Versions

### 1. Basic Interactive (`interactive.html`)
- Real-time sliders for all mathematical parameters
- Visual feedback with live updates
- Reset and randomize functions
- Clean, focused interface

### 2. Advanced Explorer (`advanced.html`)
- All basic features plus:
- 3D extrusion with adjustable depth
- Live f(u) function graph visualization
- Grid and axes toggles
- Wireframe mode
- Auto-rotation option
- 6 shape presets (thin, fat, sharp, round, banana, moon)
- Professional UI with glassmorphism effects

## Mathematical Parameter Ranges

| Parameter | Symbol | Description | Range | Scale |
|-----------|--------|-------------|-------|-------|
| R | R | Major radius of centre-line arc | 20-200 | Linear |
| r₀ | r0 | Maximum half-thickness at u=0 | 5-60 | Linear |
| α | alpha | Taper exponent | 0.1-5.0 | Exponential effect |
| θ | theta | Half-opening angle (radians) | 0.1-π | Angular |
| k | k | Flattening factor | 0.1-1.0 | Linear |
| Samples | - | Curve resolution | 20-500 | Linear |

## Files
- `index.html` - Original ES6 module version (requires web server)
- `standalone.html` - Basic standalone version (works with file://)
- `interactive.html` - Interactive version with parameter sliders
- `advanced.html` - Full-featured mathematical explorer
- `croissant.js` - ES6 module implementation
- `view.sh` - Launcher script for easy viewing