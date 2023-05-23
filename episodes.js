const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
// using the readline module to allow us to get an input from the user using the question method
rl.question("Enter the show and episode name: ", function(ep_name) {
  const pattern = /^.*\sS\d{2}E\d{2}: .*/;
  const match = ep_name.match(pattern);
//after the user adds an input we evaluate it using a regular expression and the use the if statement to decide
  if (match) {
    console.log(`${ep_name} is an episode and is available.`);
  } else {
    console.log(`${ep_name} is not an episode.`);
  }

  rl.close();
});
