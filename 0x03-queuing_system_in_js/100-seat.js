import express from 'express';
import kue from 'kue';
import Redic from 'redic';

const app = express();
const port = 1245;

// Initialize Redic client and Kue queue
const redic = new Redic();
const queue = kue.createQueue();

// Set initial number of available seats
redic.call('set', 'available_seats', 50);

// Initialize reservationEnabled
let reservationEnabled = true;

// Function to reserve a seat
const reserveSeat = (number) => {
  redic.call('set', 'available_seats', number);
};

// Function to get the current number of available seats
const getCurrentAvailableSeats = async () => {
  const availableSeats = await redic.call('get', 'available_seats');
  return parseInt(availableSeats, 10);
};

// Express route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

// Express route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  // Create and queue a job
  const job = queue.create('reserve_seat').save((err) => {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });

  // Job completion handler
  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  // Job failure handler
  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Express route to process the queue and decrease available seats
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  // Process the queue
  queue.process('reserve_seat', async (job, done) => {
    try {
      const currentSeats = await getCurrentAvailableSeats();
      if (currentSeats <= 0) {
        reservationEnabled = false;
        return done(new Error('Not enough seats available'));
      }

      // Decrease available seats
      reserveSeat(currentSeats - 1);

      if (currentSeats - 1 === 0) {
        reservationEnabled = false;
      }

      done();
    } catch (error) {
      done(error.message);
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
