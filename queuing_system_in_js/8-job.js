export default function createPushNotificationJobs(jobs, queue) {
  if (Array.isArray(jobs) === false) {
    throw new Error('Jobs is not an array');
  }

  for (const job of jobs) {
    const newJob = queue.create('push_notification_code_3', {
      phoneNumber: job.phoneNumber,
      message: job.message,
    });

    newJob.on('failed', ((errMessage) => {
      console.log(`Notification job ${newJob.id} failed: ${errMessage}`);
    }));

    newJob.on('progress', ((progress) => {
      console.log(`Notification job ${newJob.id} ${progress}% complete`);
    }));

    newJob.on('complete', (() => {
      console.log(`Notification job ${newJob.id} completed`);
    }));

    newJob.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${newJob.id}`);
      }
    });
  }
}
