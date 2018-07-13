package main

import (
	"fmt"
	"io/ioutil"
)

func floorCounterPartOne(input string) int {
	result := 0
	for _, r := range input {
		if r == '(' {
			result++
		} else if r == ')' {
			result--
		}
	}
	return result
}

func floorCounterPartTwo(input string) int {
	result := 0
	for i, r := range input {
		i++
		if r == '(' {
			result++
		} else if r == ')' {
			result--
		}

		if result < 0 {
			return i
		}
	}
	return result
}

func main() {
	inputBytes, _ := ioutil.ReadFile("input.txt")
	input := string(inputBytes)

	fmt.Println("Part 1 answer : ", floorCounterPartOne(input))
	fmt.Println("Part 2 answer : ", floorCounterPartTwo(input))
}
