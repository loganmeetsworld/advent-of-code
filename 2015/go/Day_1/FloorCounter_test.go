package main

import (
	"testing"
)

func TestFloorCounterPartOne(t *testing.T) {
	tables := []struct {
		x string
		y int
	}{
		{"(())", 0},
		{"()()", 0},
		{"(((", 3},
		{"(()(()(", 3},
		{"))(((((", 3},
		{"())", -1},
		{")))", -3},
		{")())())", -3},
	}
	for _, table := range tables {
		result := floorCounterPartOne(table.x)
		if result != table.y {
			t.Errorf("floorCounterPartOne(%s) was incorrect, got: %d, want: %d.", table.x, table.y, result)
		}
	}
}

func TestFloorCounterPartTwo(t *testing.T) {
	tables := []struct {
		x string
		y int
	}{
		{")", 1},
		{"()())", 5},
	}
	for _, table := range tables {
		result := floorCounterPartTwo(table.x)
		if result != table.y {
			t.Errorf("floorCounterPartTwo(%s) was incorrect, got: %d, want: %d.", table.x, table.y, result)
		}
	}
}
