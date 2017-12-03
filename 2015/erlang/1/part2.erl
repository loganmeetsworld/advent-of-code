-module(part2).
-export([solve/0]).

input() ->
  { ok, Binary } = file:read_file("input.txt"),
  binary_to_list(Binary).

position_of_basement(Input) ->
  length(Input) - position_of_basement(Input,0).

position_of_basement(Input, Acc) when Acc < 0 ->
  length(Input);
position_of_basement([ 40 | T ], Acc) ->
  position_of_basement(T, Acc + 1);    
position_of_basement([ 41 | T ], Acc) ->
  position_of_basement(T, Acc - 1).
    
solve() ->
  BasementPosition = position_of_basement(input()),
  { BasementPosition }.