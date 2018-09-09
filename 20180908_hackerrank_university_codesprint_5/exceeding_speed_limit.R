#!/usr/bin/env Rscript


# Read from stdin
lines <- readLines(file("stdin"))

# Parse input
speed <- as.numeric(lines[1])

# Determine fine and punishment
if (speed <= 90) {
  fine <- 0
  ticket <- "No punishment"
} else if (speed <= 110) {
  fine <- (speed - 90) * 300
  ticket <- "Warning"
} else {
  fine <- (speed - 90) * 500
  ticket <- "License removed"
}

# Print the fine and punishment
cat(fine, ticket, sep=" ", end="\n")
