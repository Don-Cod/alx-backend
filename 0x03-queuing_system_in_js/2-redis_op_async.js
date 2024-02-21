import redis from "redis";
const { promisify } = require("util");

// this creates a new client
const client = redis.createClient();
// By default redis.createClient and port 6379

const asyncGet = promisify(client.get).bind(client);

// listen for the connect event
// client.on("connect", () => console.log("Redis client connected to the server"));

// listen for the error event 
client.on("error", (err) =>
  console.error(`Redis client not connected to the server: ${err.message}`)
);

function setNewSchool(schoolName, value) {
  // redis.print prints “Reply: OK” to the console
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  console.log(await asyncGet(schoolName));
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
