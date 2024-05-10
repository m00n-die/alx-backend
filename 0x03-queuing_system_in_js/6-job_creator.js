import { createQueue } from 'kue';

const queue = createQueue();

const jobNotification = {
  'phoneNumber': '+233268171889', //random number
  'message': 'This is your OTP: 526478'
}

const job = queue.create('push_notification_code', jobNotification).save((error) => {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
