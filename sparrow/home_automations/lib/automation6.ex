defmodule Automation6 do
  use Sparrow.Actor

  pattern electicity_alert as {:consumption, meter_id, @value}[window: {3, :weeks}] # green blue
                           |> fold(0, fn({_,_,v}, acc)-> acc+v end)                 # green
                           |> bind(total)                                           # green
                           |> total > 200                                           # green

end
