defmodule Automation2 do

  def start do
    pid = spawn(Automation2, :loop, [{nil, :off}])
    IO.puts("Waiting for new messages ...")
    # Test messages
    Task.start_link(fn ->
      send(pid, {:light, 1, :on, :bathroom})
      Process.sleep(2000)
      send(pid, {:motion, 1, :on, :bathroom})
    end)
  end

  def loop({timer_ref, light_status}) do                          # yellow

    state =                                                       # yellow
      receive do                                                  # green
        {:motion, _id, :on, :bathroom} ->                         # green
          IO.puts("motion_bathroom")

          timer_ref =                                             # yellow
            case light_status == :on do                           # green
             true -> set_timer(timer_ref)
             false -> timer_ref                                   # yellow
            end
          {timer_ref, light_status}                               # yellow

        {:light, _id, value, :bathroom} ->                        # green
          IO.puts("light_bathroom")
          timer_ref =                                             # yellow
            case value == :on do                                  # green
              true -> set_timer(timer_ref)
              false -> timer_ref                                  # yellow
            end
          {timer_ref, value}                                      # yellow

        :no_motion ->                                             # green
          IO.puts("no_motion_bathroom")
          # Turn off the lights
          {nil, :off}                                             # yellow
      end

    loop(state)                                                   # yellow
  end

  def set_timer(nil), do: Process.send_after(self(), :no_motion, 5000) # two minutes 120000   # blue
  def set_timer(timer_ref) do                                                                 # blue
    IO.puts "reset timer"
    Process.cancel_timer(timer_ref)                                                           # blue
    Process.send_after(self(), :no_motion, 5000)                                              # blue
  end                                                                                        
end
