defmodule Automation4 do
  require Timex

  def start do
    last_ring = Timex.shift(Timex.now(), hours: -24)
    pid = spawn(Automation4, :loop, [last_ring])
    IO.puts "Waiting for new messages ..."

    # Test messages
    Task.start_link(fn ->
      Process.sleep(5000)
      send(pid, {:doorbell, 1, :pressed, :front_door})
      Process.sleep(5000)
      send(pid, {:doorbell, 1, :pressed, :front_door})
      Process.sleep(35000)
      send(pid, {:doorbell, 1, :pressed, :front_door})
    end)
  end


  def loop(last_ring) do                                                              # yellow

    state =                                                                           # yellow
      receive do                                                                      # green
        {:doorbell, _id, :pressed, :front_door} ->                                    # green
          IO.puts("doorbell_pressed")
          case Timex.before?(Timex.shift(last_ring, seconds: 30), Timex.now()) do     # blue
              true ->
                IO.puts "Ring"
                Timex.now()                                                           # yellow
              false -> last_ring                                                      # yellow
          end                                                                        
      end

    loop(state)                                                                       # yellow
  end
end
