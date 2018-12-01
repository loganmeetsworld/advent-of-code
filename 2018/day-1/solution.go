package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func part1(input string) string {
	inputList := strings.Split(input, "\n")
	var result int

	for i := range inputList {
		num, _ := strconv.Atoi(inputList[i])
		result += num
	}
	return strconv.Itoa(result)
}

func main() {
	inputBytes, _ := ioutil.ReadFile("input.txt")
	input := string(inputBytes)

	fmt.Println("Part 1 answer : ", part1(input))
}
