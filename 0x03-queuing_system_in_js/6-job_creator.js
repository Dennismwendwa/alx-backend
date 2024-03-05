import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'Application translation to french was completed',
};

const notificationJob = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${notificationJob.id}`);
    } else {
      console.error(`Error creating notification job: ${err}`);
    }

    queue.shutdown(5000, (err) => {
      if (err) {
        console.error(`Error shutting down queue: ${err}`);
      } else {
        console.log('Queue shutdown');
      }
    });
    });

notificationJob.on('complete', () => {
  console.log('Notification job completed');
});

notificationJob.on('failed', (err) => {
  console.error(`Notification job failed: ${err}`);
});
