defmodule Automation4 do
  use Sparrow.Actor

  pattern door_bell as {:door_bell, id}[debounce: {30, :secs}] # green blue

end
