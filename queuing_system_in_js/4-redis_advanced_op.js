import { createClient } from 'redis';

(async () => {
  const client = await createClient()
    .on('error', (err) => console.log('Redis client not connected to the server', err.message))
    .connect(console.log('Redis client connected to the server'));

  async function setNewLocation(locationName, value) {
    const reply = await client.hSet('HolbertonSchools', locationName, value);
    console.log(`Reply: ${reply}`);
  }

  async function displayAllLocations() {
    const locations = await client.hGetAll('HolbertonSchools');
    console.log(locations);
  }

  setNewLocation('Portland', 50);
  setNewLocation('Seattle', 80);
  setNewLocation('New York', 20);
  setNewLocation('Bogota', 20);
  setNewLocation('Cali', 40);
  setNewLocation('Paris', 2);
  displayAllLocations();
})();
