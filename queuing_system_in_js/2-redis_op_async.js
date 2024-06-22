import { createClient } from 'redis';

(async () => {
  const client = await createClient()
    .on('error', (err) => console.log('Redis client not connected to the server', err.message))
    .connect(console.log('Redis client connected to the server'));

  async function setNewSchool(schoolName, value) {
    const reply = await client.set(schoolName, value);
    console.log(`Reply: ${reply}`);
  }

  async function displaySchoolValue(schoolName) {
    const reply = await client.get(schoolName);
    console.log(reply);
  }

  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})();
