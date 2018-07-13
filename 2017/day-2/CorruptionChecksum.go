package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func readInputFile(file *os.File) [][]int {
	result := make([][]int, 0, 0)

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		numbers := strings.Split(line, "\t")
		row := make([]int, 0, len(numbers))
		for _, v := range numbers {
			value, _ := strconv.Atoi(v)
			row = append(row, value)
		}

		result = append(result, row)
	}

	return result
}

func partOne(input [][]int) int {
	result := 0
	for _, v := range input {
		result += mod(v)
	}
	return result
}

func diff(input []int) int {
	min, max := math.MaxInt32, math.MinInt32

	for _, v := range input {
		if v < min {
			min = v
		}

		if v > max {
			max = v
		}
	}

	return max - min
}

func mod(input []int) int {
	for i, v := range input {
		for _, v2 := range input[i+1:] {
			if v%v2 == 0 {
				return v / v2
			}

			if v2%v == 0 {
				return v2 / v
			}
		}
	}

	return 0
}

func main() {
	inputFile, _ := os.Open(os.Args[1])
	defer inputFile.Close()

	input := readInputFile(inputFile)

	fmt.Println("Part 1 answer : ", partOne(input))
	// fmt.Println("Part 2 answer : ", partTwo(input))
}
