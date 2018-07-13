package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func wrapCalculatorPartOne(input string) int {
	result := 0
	scanner := bufio.NewScanner(strings.NewReader(input))
	for scanner.Scan() {
		dims := strings.Split(scanner.Text(), "x")
		l, _ := strconv.Atoi(dims[0])
		w, _ := strconv.Atoi(dims[1])
		h, _ := strconv.Atoi(dims[2])

		result += calcSurfaceArea(l, w, h) + calcShortestside(l, w, h)
	}

	return result
}

func calcSurfaceArea(l, w, h int) int {
	return (2 * l * w) + (2 * w * h) + (2 * h * l)
}

func calcCubic(l, w, h int) int {
	return l * w * h
}

func calcShortestside(l, w, h int) int {
	x := []int{
		l * w,
		w * h,
		h * l,
	}

	shortest := x[0]
	for _, v := range x {
		if v < shortest {
			shortest = v
		}
	}

	return shortest
}

func calcShortestDistance(l, w, h int) int {
	return 0
}

func wrapCalculatorPartTwo(input string) int {
	result := 0
	scanner := bufio.NewScanner(strings.NewReader(input))
	for scanner.Scan() {
		dims := strings.Split(scanner.Text(), "x")
		l, _ := strconv.Atoi(dims[0])
		w, _ := strconv.Atoi(dims[1])
		h, _ := strconv.Atoi(dims[2])

		result += calcShortestDistance(l, w, h) + calcCubic(l, w, h)
	}

	return result
}

func main() {
	inputBytes, _ := ioutil.ReadFile("input.txt")
	input := string(inputBytes)

	fmt.Println("Part 1 answer : ", wrapCalculatorPartOne(input))
	fmt.Println("Part 2 answer : ", wrapCalculatorPartTwo(input))
}
