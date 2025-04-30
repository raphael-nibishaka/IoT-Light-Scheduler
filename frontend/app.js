const statusText = document.getElementById('statusText');
const simulateOn = document.getElementById('simulateOn');
const simulateOff = document.getElementById('simulateOff');

// Connect to WebSocket
const socket = new WebSocket('ws://localhost:8765');

socket.onopen = () => {
  console.log('Connected to WebSocket server');
};

socket.onmessage = (event) => {
  statusText.textContent = `Server: ${event.data}`;
};

socket.onerror = (err) => {
  console.error('WebSocket error:', err);
  statusText.textContent = 'WebSocket error. Please retry later.';
};

document.getElementById('scheduleForm').addEventListener('submit', (e) => {
  e.preventDefault();
  const onTime = document.getElementById('onTime').value;
  const offTime = document.getElementById('offTime').value;
  const message = `${onTime},${offTime}`;
  socket.send(message);
  statusText.textContent = `Schedule sent: ON @ ${onTime}, OFF @ ${offTime}`;
});

simulateOn.onclick = () => {
  statusText.textContent = 'Simulated: Light is ON 💡';
};

simulateOff.onclick = () => {
  statusText.textContent = 'Simulated: Light is OFF 🕯️';
};
