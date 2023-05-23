const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter the show and episode name: ", function(ep_name) {
  const pattern = /^.*\sS\d{2}E\d{2}: .*/;
  const match = ep_name.match(pattern);

  if (match) {
    console.log(`${ep_name} is an episode and is available.`);
  } else {
    console.log(`${ep_name} is not an episode.`);
  }

  rl.close();
});
