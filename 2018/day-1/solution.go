package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func partOne(input string) string {
	inputList := strings.Split(input, "\n")
	var result int

	for i := range inputList {
		num, _ := strconv.Atoi(inputList[i])
		result += num
	}
	return strconv.Itoa(result)
}

func partTwo(input string) string {
	inputList := strings.Split(input, "\n")
	var currentFreq int
	var tracker = make(map[int]bool)

	for {
		for i := range inputList {
			num, _ := strconv.Atoi(inputList[i])
			currentFreq += num
			if tracker[currentFreq] {
				return strconv.Itoa(currentFreq)
			}
			tracker[currentFreq] = true
		}
	}
}

func main() {
	inputBytes, _ := ioutil.ReadFile("input.txt")
	input := string(inputBytes)

	fmt.Println("Part 1 answer : ", partOne(input))
	fmt.Println("Part 1 answer : ", partTwo(input))
}
