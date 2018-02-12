#!/usr/bin/env node

// Read from stdin and output to stdout with Node - the following is
// provided by HackerRank and it seems to work well enough
process.stdin.resume()
process.stdin.setEncoding('ascii')

var input_stdin = ''
var input_stdin_array = ''
var input_currentline = 0

process.stdin.on('data', function (data) {
  input_stdin += data
})

process.stdin.on('end', function () {
  input_stdin_array = input_stdin.split('\n')
  main()
})

function readLine () {
  return input_stdin_array[input_currentline++]
}

// Now here's my code
function main () {
  // Get number of acids
  let n = parseInt(readLine())

  // Go through each acid
  for (let a = 0; a < n; a++) {
    let acidName = readLine()
    let result = ''

    // Classify the acid
    if (acidName.search(/^hydro.*ic$/) !== -1) {
      result = 'non-metal acid\n'
    } else if (acidName.search(/ic$/) !== -1) {
      result = 'polyatomic acid\n'
    } else {
      result = 'not an acid\n'
    }

    process.stdout.write(result)
  }
}
