%% beginning we always declare the module which is also the file name
-module(part1).
%% we export the relevant functions
-export([solve/0]).
-compile(debug_info).

%% we prepare the input string as binary
input() ->
  { ok, Binary } = file:read_file("input.txt"),
  binary_to_list(Binary).

%% setting up the floor checker that takes an input, this is the recursive base case
%% Input is a local variable without assignment yet
floor_on(Input) ->
  floor_on(Input, 0).

%% if the head is on 40/41 the ascii for '(' and ')' then add one to the count
floor_on([], Count) -> Count;
floor_on([ 40 | T], Count) -> floor_on(T, Count + 1);
floor_on([ 41 | T], Count) -> floor_on(T, Count - 1).


%% solve method to be exported that takes in the input
solve() ->
  NumberOfFLoors = floor_on(input()),
  { NumberOfFLoors }.