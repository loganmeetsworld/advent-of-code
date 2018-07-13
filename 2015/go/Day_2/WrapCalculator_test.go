package main

import (
	"testing"
)

func TestWrapCalculatorPartOne(t *testing.T) {
	tables := []struct {
		x string
		y int
	}{
		{"2x3x4", 58},
		{"1x1x10", 43},
	}
	for _, table := range tables {
		result := wrapCalculatorPartOne(table.x)
		if result != table.y {
			t.Errorf("wrapCalculatorPartOne(%s) was incorrect, got: %d, want: %d.", table.x, table.y, result)
		}
	}
}

func TestWrapCalculatorPartTwo(t *testing.T) {
	tables := []struct {
		x string
		y int
	}{
		{"2x3x4", 34},
		{"1x1x10", 14},
	}
	for _, table := range tables {
		result := wrapCalculatorPartTwo(table.x)
		if result != table.y {
			t.Errorf("wrapCalculatorPartTwo(%s) was incorrect, got: %d, want: %d.", table.x, table.y, result)
		}
	}
}
