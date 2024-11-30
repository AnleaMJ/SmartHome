document.addEventListener('DOMContentLoaded', () => {
    fetchEnergyConsumption();
    fetchRecommendations();
    fetchPredictedUsage();
});

async function fetchEnergyConsumption() {
    const response = await fetch('/api/energy-consumption');
    const data = await response.json();
    document.getElementById('energy-consumption').textContent = `${data.consumption} kWh`;
}

async function fetchRecommendations() {
    const response = await fetch('/api/recommendations');
    const data = await response.json();
    document.getElementById('recommendations').textContent = data.recommendations;
}

async function fetchPredictedUsage() {
    const response = await fetch('/api/predicted-usage');
    const data = await response.json();
    document.getElementById('predicted-usage').textContent = `${data.usage} kWh`;
}
