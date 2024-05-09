import redis from "redis";
const client = redis.createClient();

client.on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on("connect", () => {
    console.log("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    redis.print(`Reply: ${reply}`);
    // redis.print(`Erroe: ${reply}`);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
    // if (err) {
    //     console.error(err);
    // }
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
