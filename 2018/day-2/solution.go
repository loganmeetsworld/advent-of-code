package main

import (
	"fmt"
	"io/ioutil"
)

func partOne(input string) string {
	// inputList := strings.Split(input, "\n")

	return input
}

func partTwo(input string) string {
	// inputList := strings.Split(input, "\n")

	return input
}

func main() {
	inputBytes, _ := ioutil.ReadFile("input.txt")
	input := string(inputBytes)

	fmt.Println("Part 1 answer : ", partOne(input))
	fmt.Println("Part 1 answer : ", partTwo(input))
}
