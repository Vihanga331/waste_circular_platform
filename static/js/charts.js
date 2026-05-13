const chartTheme = () => ({
  text: document.documentElement.classList.contains('dark') ? '#cbd5e1' : '#475569',
  grid: document.documentElement.classList.contains('dark') ? 'rgba(255,255,255,.08)' : 'rgba(148,163,184,.22)'
});

function makeChart(id, config) {
  const el = document.getElementById(id);
  if (!el || !window.Chart) return;
  const theme = chartTheme();
  Chart.defaults.color = theme.text;
  Chart.defaults.borderColor = theme.grid;
  new Chart(el, config);
}

document.addEventListener('DOMContentLoaded', () => {
  makeChart('wasteChart', {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [
        { label: 'Organic', data: [42, 51, 48, 61, 70, 76], borderColor: '#16a34a', backgroundColor: 'rgba(22,163,74,.12)', tension: .35, fill: true },
        { label: 'Recyclable', data: [28, 31, 36, 40, 44, 52], borderColor: '#0284c7', backgroundColor: 'rgba(2,132,199,.10)', tension: .35, fill: true }
      ]
    },
    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'bottom' } } }
  });

  makeChart('methaneChart', {
    type: 'bar',
    data: {
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      datasets: [{ label: 'm3 produced', data: [510, 620, 580, 710, 780, 730, 840], backgroundColor: '#0ea5e9' }]
    },
    options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }
  });

  makeChart('donutChart', {
    type: 'doughnut',
    data: {
      labels: ['Recycled', 'Methane', 'Landfill avoided'],
      datasets: [{ data: [44, 31, 25], backgroundColor: ['#16a34a', '#0284c7', '#64748b'], borderWidth: 0 }]
    },
    options: { responsive: true, maintainAspectRatio: false, cutout: '68%', plugins: { legend: { position: 'bottom' } } }
  });

  makeChart('billingChart', {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
      datasets: [{ label: 'Payments', data: [72, 78, 81, 87, 92, 96], borderColor: '#16a34a', tension: .35 }]
    },
    options: { responsive: true, maintainAspectRatio: false }
  });
});
