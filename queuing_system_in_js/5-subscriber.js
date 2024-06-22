import { createClient } from 'redis';

(async () => {
  const sub = await createClient()
    .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
    .connect(console.log('Redis client connected to the server'));

  await sub.subscribe('holberton school channel', (message) => {
    if (message === 'KILL_SERVER') {
      sub.unsubscribe('holberton school channel');
      sub.quit();
    }
    console.log(message);
  });
})();
