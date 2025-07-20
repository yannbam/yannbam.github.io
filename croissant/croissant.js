import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/controls/OrbitControls.js';

// Croissant geometry parameters - MATHEMATICALLY IDENTICAL to SVG
const R     = 70;     // major radius of centre-line arc (mm ≈ px here)
const r0    = 20;     // maximum half-thickness at u = 0
const alpha = 1.5;    // taper exponent
const theta = 1.4;    // half-opening angle (radians)
const k     = 0.70;   // flattening factor of cross-section
const SAMPLES = 200;  // resolution of the outline

// Helper: cross-section scale factor f(u) = [cos(πu/2θ)]^α
function f(u) {
    return Math.pow(Math.cos(Math.PI * u / (2 * theta)), alpha);
}

// Create the 2D croissant shape - IDENTICAL MATH TO SVG
function createCroissantShape() {
    const shape = new THREE.Shape();
    
    // Build the outer edge from u = −θ … +θ
    for (let i = 0; i <= SAMPLES; i++) {
        const u = -theta + 2 * theta * i / SAMPLES;
        const a = r0 * f(u);  // local radius added outward
        const x = (R + a) * Math.cos(u);
        const y = (R + a) * Math.sin(u);
        
        if (i === 0) {
            shape.moveTo(x, y);
        } else {
            shape.lineTo(x, y);
        }
    }
    
    // Build the inner edge back from u = +θ … −θ
    for (let i = SAMPLES; i >= 0; i--) {
        const u = -theta + 2 * theta * i / SAMPLES;
        const b = k * r0 * f(u);  // local radius subtracted inward
        const x = (R - b) * Math.cos(u);
        const y = (R - b) * Math.sin(u);
        shape.lineTo(x, y);
    }
    
    shape.closePath();
    return shape;
}

// Scene setup
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xffffff);

// Camera
const camera = new THREE.PerspectiveCamera(
    50,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);
camera.position.set(0, 0, 300);

// Renderer
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
document.body.appendChild(renderer.domElement);

// Create croissant geometry
const croissantShape = createCroissantShape();

// Option 1: 2D flat representation (like SVG)
const geometry2D = new THREE.ShapeGeometry(croissantShape);
const material2D = new THREE.MeshBasicMaterial({
    color: 0xF8D59E,  // warm crumb colour from SVG
    side: THREE.DoubleSide
});
const mesh2D = new THREE.Mesh(geometry2D, material2D);

// Add outline
const outlineGeometry = new THREE.BufferGeometry().setFromPoints(croissantShape.getPoints());
const outlineMaterial = new THREE.LineBasicMaterial({ 
    color: 0xC69A5B,  // crust outline from SVG
    linewidth: 2 
});
const outline = new THREE.Line(outlineGeometry, outlineMaterial);
outline.position.z = 0.1;  // slightly in front

// Group 2D representation
const croissant2D = new THREE.Group();
croissant2D.add(mesh2D);
croissant2D.add(outline);
scene.add(croissant2D);

// Option 2: 3D extruded version (comment out 2D version above to use this)
/*
const extrudeSettings = {
    depth: 15,
    bevelEnabled: true,
    bevelThickness: 2,
    bevelSize: 1,
    bevelSegments: 5
};
const geometry3D = new THREE.ExtrudeGeometry(croissantShape, extrudeSettings);
const material3D = new THREE.MeshPhongMaterial({
    color: 0xF8D59E,
    specular: 0x222222,
    shininess: 25
});
const croissant3D = new THREE.Mesh(geometry3D, material3D);
scene.add(croissant3D);

// Add lights for 3D version
const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
scene.add(ambientLight);
const directionalLight = new THREE.DirectionalLight(0xffffff, 0.4);
directionalLight.position.set(50, 50, 50);
scene.add(directionalLight);
*/

// Controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}

// Handle window resize
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// Start animation
animate();

// Export for debugging/verification
window.croissantParams = { R, r0, alpha, theta, k, SAMPLES, f };