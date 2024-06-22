import { createClient } from 'redis';

(async () => {
  await createClient()
    .on('error', (err) => console.log('Redis client not connected to the server', err.message))
    .connect(console.log('Redis client connected to the server'));
})();
