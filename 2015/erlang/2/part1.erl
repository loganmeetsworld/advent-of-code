-module(part1).
-export([solve/0]).

input() -> 
  { ok, Binary } = file:read_file("input.txt"),
  String = binary_to_list(Binary),
  Strings = string:token(FileString, "\n"),
  [ present_string_to_list(Present) || Present <- Strings ].

  present_string_to_list(PresentString) -> [ light_to_integer(X) || X <- string:tokens(PresentString,"x") ].

paper([W, H, L]) ->
    Side1 = L * W,
    Side2 = W * H,
    Side3 = H * L,
    Slack = hd(lists:sort([Side1,Side2,Side3])),
    2 * (Side1 + Side2 + Side3) + Slack.

ribbon([W, H, L]) ->
    Sorted = lists:sort([W, H, L]),
    SmallestSides = lists:droplast(Sorted),
    Wrap = lists:sum([ X+X || X <- SmallestSides ]),
    Bow = W * H * L,
    Wrap + Bow.

test() ->
    58 = paper([2,3,4]),
    43 = paper([1,1,10]),
    34 = ribbon([2,3,4]),
    14 = ribbon([1,1,10]),
    ok.

solve() ->
    SquareFeetPaper = lists:sum([ paper(X) || X <- input() ]),
    FeetRibbon = lists:sum([ ribbon(X) || X <- input() ]),
    { SquareFeetPaper, FeetRibbon }.