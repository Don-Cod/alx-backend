import redis from "redis";

// this creates a new client
const client = redis.createClient();
// By default redis.createClient()

// listen for the connect event
client.on("connect", () => console.log("Redis client connected to the server"));

// listen for the error event
client.on("error", (err) =>
  console.error(`Redis client not connected to the server: ${err.message}`)
);

function setNewSchool(schoolName, value) {
  // redis.print prints “Reply: OK” to the console
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, result) => {
    if (err) {
      console.log(err);
      throw err;
    }
    console.log(result);
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
