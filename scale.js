const fs = require('fs');

let css = fs.readFileSync('css/style.css', 'utf8');

// 1. Make colors pop more
css = css.replace(/--bg: #0a0a0a;/, '--bg: #000000;');
css = css.replace(/--surface: #141414;/, '--surface: #111111;');
css = css.replace(/--border: rgba\(255,255,255,0.08\);/, '--border: rgba(255,255,255,0.15);');
css = css.replace(/--border-hover: rgba\(255,255,255,0.18\);/, '--border-hover: rgba(255,255,255,0.35);');
css = css.replace(/--text-dim: #888;/, '--text-dim: #aaaaaa;');
css = css.replace(/--accent: #f59e0b;/, '--accent: #ff9d00;');
css = css.replace(/--accent-light: #fbbf24;/, '--accent-light: #ffba33;');
css = css.replace(/--accent-glow: rgba\(245,158,11,0.15\);/, '--accent-glow: rgba(255,157,0,0.3);');

css = css.replace(/--bg: #f3ece0;/, '--bg: #f8f9fa;');
css = css.replace(/--border: rgba\(0,0,0,0.08\);/, '--border: rgba(0,0,0,0.15);');
css = css.replace(/--border-hover: rgba\(0,0,0,0.18\);/, '--border-hover: rgba(0,0,0,0.35);');
css = css.replace(/--text: #111;/, '--text: #000000;');
css = css.replace(/--text-dim: #666;/, '--text-dim: #555555;');
css = css.replace(/--accent: #d97706;/, '--accent: #e65c00;');
css = css.replace(/--accent-light: #f59e0b;/, '--accent-light: #ff7700;');
css = css.replace(/--accent-glow: rgba\(217,119,6,0.12\);/, '--accent-glow: rgba(230,92,0,0.25);');

// 2. Scale font-sizes
css = css.replace(/font-size:\s*clamp\(([^,]+),\s*([^,]+),\s*([^)]+)\)/g, (match, min, vw, max) => {
    const scaleVal = (val) => {
        let num = parseFloat(val);
        let unit = val.replace(/[0-9\.]/g, '');
        return (num * 1.5).toFixed(2).replace(/\.00$/, '') + unit;
    };
    return `font-size: clamp(${scaleVal(min)}, ${scaleVal(vw)}, ${scaleVal(max)})`;
});

css = css.replace(/font-size:\s*([0-9\.]+)(rem|px)/g, (match, val, unit) => {
    let num = parseFloat(val);
    return `font-size: ${(num * 1.5).toFixed(2).replace(/\.00$/, '')}${unit}`;
});

// 3. Scale paddings, margins, gaps, widths, heights (excluding max-width, min-height: 100vh)
const propsToScale = ['padding', 'margin', 'margin-bottom', 'margin-top', 'gap', 'grid-auto-rows', 'width', 'height', 'border-radius'];

propsToScale.forEach(prop => {
    // scale px
    let regexPx = new RegExp(`${prop}:\\s*([0-9\\spx]+);`, 'g');
    css = css.replace(regexPx, (match, vals) => {
        if (vals.includes('vw') || vals.includes('vh') || vals.includes('%')) return match;
        let newVals = vals.split(' ').map(v => {
            if (v.endsWith('px')) {
                let num = parseFloat(v);
                if (num > 2) return (num * 1.5) + 'px'; // don't scale 1px borders
                return v;
            }
            return v;
        }).join(' ');
        return `${prop}: ${newVals};`;
    });
});

// manually fix a few things
css = css.replace(/max-width: 800px;/, 'max-width: 1200px;');
css = css.replace(/max-width: 1300px;/, 'max-width: 1950px;'); // user wants 50% larger
css = css.replace(/--radius: 20px;/, '--radius: 30px;');

fs.writeFileSync('css/style.css', css);
console.log('Scaled CSS applied');
