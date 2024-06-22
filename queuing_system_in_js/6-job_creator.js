import kue from 'kue';

const jobData = {
  phoneNumber: '04654654',
  message: 'Hello world',
};
const queue = kue.createQueue();
const job = queue.create('push_notification_code', jobData);

job.on('failed', (() => {
  console.log('Notification job failed');
}));

job.on('complete', (() => {
  console.log('Notification job completed');
}));

job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});
