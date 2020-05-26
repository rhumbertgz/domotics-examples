defmodule Automation1 do
  def start do
    pid = spawn(Automation1, :loop, [{100, :off}])
    IO.puts("Waiting for new messages ...")
    # Test messages
    Task.start_link(fn ->
      send(pid, {:ambient_light, 1, 50, :bathroom})
      Process.sleep(2000)
      send(pid, {:motion, 1, :on, :bathroom})
      Process.sleep(2000)
      send(pid, {:ambient_light, 1, 40, :bathroom})
      Process.sleep(2000)
      send(pid, {:light, 1, :on, :bathroom})
      Process.sleep(2000)
      send(pid, {:motion, 1, :on, :bathroom})
      Process.sleep(2000)
      send(pid, {:light, 1, :off, :bathroom})
      Process.sleep(2000)
      send(pid, {:motion, 1, :on, :bathroom})
    end)
  end


  def loop({ambient_light, light_status}) do                      # yellow

    state =                                                       # yellow
      receive do                                                  # green
        {:motion, _id, :on, :bathroom} ->                         # green
          IO.puts("motion_bathroom")

          case ambient_light <= 40 and light_status == :off do    # green
              true ->
                IO.puts(">>> Turning on the light")
                 # Turn on the light
                {ambient_light, :on}                              # yellow

              false -> {ambient_light, :off}                      # yellow
          end                                                     # green

        {:ambient_light, _id, value, :bathroom} ->                # green
          IO.puts("ambient_light_bathroom")
          {value, light_status}                                   # yellow

        {:light, _id, value, :bathroom} ->                        # green
          IO.puts("ambient_light_bathroom")
          {ambient_light, value}                                   # yellow
      end                                                         # green

    loop(state)                                                   # yellow
  end
end
