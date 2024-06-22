import { createClient } from 'redis';

/* Using legacy mode to use callback-based interface for this exercise */
(async () => {
  const client = await createClient({ legacyMode: true })
    .on('error', (err) => console.log('Redis client not connected to the server', err.message))
    .connect(console.log('Redis client connected to the server'));

  function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
      console.log(`Reply: ${reply}`);
    });
  }

  function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
      console.log(reply);
    });
  }

  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})();
