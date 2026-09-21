document.getElementById('year').textContent = new Date().getFullYear();

const lb = document.getElementById('lightbox');
const lbImg = lb.querySelector('img');
const lbCap = lb.querySelector('.lb-cap');

document.getElementById('grid').addEventListener('click', (e) => {
  const shot = e.target.closest('.shot');
  if (!shot) return;
  const img = shot.querySelector('img');
  lbImg.src = img.src;
  lbImg.alt = img.alt;
  lbCap.textContent = shot.dataset.caption || img.alt;
  if (typeof lb.showModal === 'function') lb.showModal();
});

lb.querySelector('.lb-close').addEventListener('click', () => lb.close());
lb.addEventListener('click', (e) => { if (e.target === lb) lb.close(); });

// Pause the marquee when the tab is hidden; nobody needs it burning cycles in the background.
const track = document.querySelector('.marquee-track');
document.addEventListener('visibilitychange', () => {
  if (track) track.style.animationPlayState = document.hidden ? 'paused' : 'running';
});
