// Minimal floating lines background using Canvas
// Keeps animation subtle to avoid distracting from content

(function () {
  const canvas = document.createElement("canvas");
  canvas.id = "network-bg";
  document.addEventListener("DOMContentLoaded", () => {
    document.body.prepend(canvas);
    init();
  });

  let ctx;
  let width;
  let height;
  let points = [];
  const POINT_COUNT = 80;
  const MAX_DISTANCE = 150;

  function init() {
    ctx = canvas.getContext("2d");
    onResize();
    window.addEventListener("resize", onResize);
    createPoints();
    requestAnimationFrame(tick);
  }

  function onResize() {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
  }

  function createPoints() {
    points = [];
    for (let i = 0; i < POINT_COUNT; i++) {
      points.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.4,
        vy: (Math.random() - 0.5) * 0.4,
      });
    }
  }

  function tick() {
    ctx.clearRect(0, 0, width, height);
    ctx.fillStyle = "#050608";
    ctx.fillRect(0, 0, width, height);

    // Move points
    for (const p of points) {
      p.x += p.vx;
      p.y += p.vy;

      if (p.x < 0 || p.x > width) p.vx *= -1;
      if (p.y < 0 || p.y > height) p.vy *= -1;
    }

    // Draw connections
    ctx.lineWidth = 0.5;
    for (let i = 0; i < points.length; i++) {
      for (let j = i + 1; j < points.length; j++) {
        const p1 = points[i];
        const p2 = points[j];
        const dx = p1.x - p2.x;
        const dy = p1.y - p2.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < MAX_DISTANCE) {
          const alpha = 1 - dist / MAX_DISTANCE;
          ctx.strokeStyle = "rgba(200, 200, 200," + alpha * 0.4 + ")";
          ctx.beginPath();
          ctx.moveTo(p1.x, p1.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.stroke();
        }
      }
    }

    // Draw points
    ctx.fillStyle = "#d0d0d0";
    for (const p of points) {
      ctx.beginPath();
      ctx.arc(p.x, p.y, 1.3, 0, Math.PI * 2);
      ctx.fill();
    }

    requestAnimationFrame(tick);
  }
})();


