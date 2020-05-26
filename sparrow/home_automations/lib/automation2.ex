defmodule Automation2 do
  use Sparrow.Actor

  pattern turn_off as not {:motion, id, :on, :bathroom}[window: {2, :mins}] and {:light, idl, :on, :bathroom}, options: [last]  # green blue

  ## Generic version to turn on lights of each room
  # pattern turn_off as not {:motion, id, :on, :bathroom}[window: {2, :mins}] and {:light, idl, :on, :bathroom}, options: [last] 

end
