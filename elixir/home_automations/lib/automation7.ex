defmodule Automation7 do
  require Timex
  @codes [:fhs_failure, :is_failure]

  def start do
    old_time = Timex.shift(Timex.now(), hours: -24)
    pid = spawn(Automation7, :loop, [{%{:fhs_failure => 0, :is_failure => 0}, old_time}])
    IO.puts "Waiting for new messages ..."

    # Test messages
    Task.start_link(fn ->
      Process.sleep(3000)
      send(pid, {:boiler, 1, :is_failure})
      send(pid, {:boiler, 1, :fhs_failure})
      send(pid, {:boiler, 1, :fhs_failure})
      send(pid, {:boiler, 1, :fhs_failure})
      Process.sleep(2000)
      send(pid, {:boiler, 1, :is_failure})
      send(pid, {:boiler, 1, :fhs_failure})
      send(pid, {:boiler, 1, :fhs_failure})
      send(pid, {:boiler, 1, :fhs_failure})
      Process.sleep(12000)
      send(pid, {:boiler, 1, :is_failure})
      send(pid, {:boiler, 1, :fhs_failure})
      send(pid, {:boiler, 1, :fhs_failure})
      send(pid, {:boiler, 1, :fhs_failure})
      # Process.sleep(35000)
      # send(pid, {:doorbell, 1, :pressed, :front_door})
    end)
  end


  def loop({counter, last_notif}) do                                      # yellow

    state =                                                               # yellow
      receive do                                                          # green
        {:boiler, _id, code} when code in @codes ->                       # green
          IO.puts("boiler_event #{code}")
          {_, counter} = Map.get_and_update(counter, code, fn val -> {val, val+1} end)      # yellow
          Process.send_after(self(), {:timer, code}, 5000) # 1 hour = 3.600.000 ms          # blue
          last_notif = check_constraints(counter, last_notif)                               # yellow
          {counter, last_notif}                                                             # yellow
        {:timer, code} ->                                                                   # blue
          {_, counter} = Map.get_and_update(counter, code, fn val -> {val,  val-1 } end)     # yellow
          {counter, last_notif}                                                             # yellow
      end                                                                                   # green

    loop(state)                                                                             # yellow
  end

  defp check_constraints(counter, last_notif) do                                      # green
    case counter.fhs_failure >= 3 and counter.is_failure >= 1 do                      # green
      true ->
        case Timex.before?(last_notif, Timex.shift(Timex.now(), seconds: -10)) do  #10 -> 60  # blue
          true ->
            IO.puts "Sending notification..."
            Timex.now()                                                               # yellow
          false -> last_notif                                                         # yellow
        end                                                                           # blue
      false -> last_notif                                                             # yellow
    end                                                                               # green                                                                   # green
  end                                                                                 # green

end
