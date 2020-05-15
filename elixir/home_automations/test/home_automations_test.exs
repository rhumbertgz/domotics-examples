defmodule HomeAutomationsTest do
  use ExUnit.Case
  doctest HomeAutomations

  test "greets the world" do
    assert HomeAutomations.hello() == :world
  end
end
