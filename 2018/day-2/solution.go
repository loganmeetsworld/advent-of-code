package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func partOne(input string) string {
	inputList := strings.Split(input, "\n")
	var twos int
	var threes int

	for i := range inputList {
		var freqHash = make(map[string]int)
		box := strings.Split(inputList[i], "")
		for j := range box {
			freqHash[box[j]]++
		}
		twoFound := false
		threeFound := false

		for _, v := range freqHash {
			if v == 2 && !twoFound {
				twoFound = true
				twos++
			}
			if v == 3 && !threeFound {
				threeFound = true
				threes++
			}
		}
	}

	return strconv.Itoa(twos * threes)
}

func partTwo(input string) string {
	// inputList := strings.Split(input, "\n")

	return input
}

func main() {
	inputBytes, _ := ioutil.ReadFile("input.txt")
	input := string(inputBytes)

	fmt.Println("Part 1 answer : ", partOne(input))
	// fmt.Println("Part 1 answer : ", partTwo(input))
}
