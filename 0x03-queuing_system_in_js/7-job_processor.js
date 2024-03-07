import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
 job.progress(0);

   if (blacklistedNumbers.includes(phoneNumber)) {
    job.progress(100);
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50); // Track progress 50 out of 100
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  job.progress(100); // Set progress to 100
  done();
};

const queue = kue.createQueue();

// Process jobs of the queue 'push_notification_code_2' with two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
