const redis = require('redis');

// Create our Redis Connection
const client = redis.createClient(6379, 'localhost');


// Define a callback when a message is recieved
client.on('message', (channel, message) => {
    console.log(`Recieved ${message}`);
});

// Subscribe to the numberStream
client.subscribe("numberStream");
