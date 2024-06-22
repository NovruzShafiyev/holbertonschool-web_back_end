import { createClient } from 'redis';

(async () => {
  const pub = await createClient()
    .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
    .connect(console.log('Redis client connected to the server'));

  function timeout(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }
  async function publishMessage(message, time) {
    await timeout(time);
    console.log('About to send', message);
    await pub.publish('holberton school channel', message);
  }

  publishMessage('Holberton Student #1 starts course', 100);
  publishMessage('Holberton Student #2 starts course', 200);
  publishMessage('KILL_SERVER', 300);
  publishMessage('Holberton Student #3 starts course', 400);
})();
