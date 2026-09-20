document.getElementById('y').textContent = new Date().getFullYear();
const io = new IntersectionObserver((es)=>{
  es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} });
},{threshold:.15});
document.querySelectorAll('.reveal:not(.in)').forEach(el=>io.observe(el));
