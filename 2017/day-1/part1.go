package main

import (
	"fmt"
	"io/ioutil"
)

func part1(input string, match int) int {
	result := 0

	for i, v := range input {
		if input[i] == input[(i+match)%len(input)] {
			result += int(v - '0')
		}
	}

	return result
}

func main() {
	inputBytes, _ := ioutil.ReadFile("input.txt")
	input := string(inputBytes)

	fmt.Println("Part 1 answer : ", part1(input, 1))
	fmt.Println("Part 2 answer : ", part1(input, len(input)/2))
}
