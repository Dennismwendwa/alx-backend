import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message);

  done();
});

queue.on('error', (err) => {
  console.error(`Queue error: ${err}`);
});

queue.on('error', () => {
  console.error(`Queue error: ${err}`);
});

queue.on('ready', () => {
  console.log('Queue is ready');
});

queue.on('idle', () => {
  console.log('Queue is idle');
});

queue.on('job complete', (id) => {
  console.log(`Job ${id} completed`);
});

queue.on('job failed', (id, err) => {
  console.error(`Job ${id} failed with error: ${err}`);
});

queue.on('job removed', (id) => {
 console.log(`Job ${id} removed from the queue`);
});
