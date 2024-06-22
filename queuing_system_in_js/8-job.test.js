import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationJobs from './8-job';

const queue = kue.createQueue();

describe('createPushNotificationJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should throw an Error when argument jobs is not an array', () => {
    const jobs = {};
    expect(() => createPushNotificationJobs(jobs, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should add new job when being passed an array', () => {
    const jobs = [
      {
        phoneNumber: '654654654',
        message: 'This is the code 6544 to verify your account',
      },
      {
        phoneNumber: '3241685476',
        message: 'This is the code 4654 to verify your account',
      },
    ];

    createPushNotificationJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
