import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    // Enter test mode without processing the jobs
    queue.testMode.enter();
  });

  after(() => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', () => {
    const invalidCall = () => createPushNotificationsJobs('invalid', queue);
    expect(invalidCall).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobsInQueue = queue.testMode.jobs;

    expect(jobsInQueue.length).to.equal(2);

  });
});
