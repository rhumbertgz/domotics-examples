defmodule Automation1 do
  use Sparrow.Actor

  pattern turn_on as {:motion, id, :on, :bathroom} and {:ambient_light, idal, value, :bathroom} # green
                  and {:light, idl, :off, :bathroom} when value > 40, options: [last]       # green

  ## Generic version to turn on lights of each room
  # pattern turn_on as {:motion, :on, room} and {:ambient_light,  value, room}
  #                 and {:light, :off, room} when value > 40, options: [last]

end

