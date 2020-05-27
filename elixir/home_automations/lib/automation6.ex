defmodule Automation6 do
  require Timex


  def start do

    pid = spawn(Automation6, :loop, [{0, []}])
    IO.puts "Waiting for new messages ..."

    # Test messages
    Task.start_link(fn ->
      Process.sleep(3000)
      send(pid, {:daily_consumption, 1, 20})
      send(pid, {:daily_consumption, 1, 30})
      send(pid, {:daily_consumption, 1, 30})
      send(pid, {:daily_consumption, 1, 30})
      send(pid, {:daily_consumption, 1, 70})
      # Process.sleep(5000)
      send(pid, {:daily_consumption, 1, 70})
      # Process.sleep(35000)
      # send(pid, {:doorbell, 1, :pressed, :front_door})
    end)
  end


  def loop({counter, values}) do                                        # yellow

    state =                                                              # yellow
      receive do                                                         # green
        {:daily_consumption, _id, value} when counter <=4 -> # 20 reads  # green
          { counter+1, values ++ [value]}                                # yellow

        {:daily_consumption, _id, value} when counter < 5 -> # 21 reads  # green
          values = values ++ [value]                                     # yellow
          check_consumption(values)
          {counter+1, values}                                             # yellow

        {:daily_consumption, _id, value} ->                               # green
          [_first | rest] = values                                        # yellow
          values = rest ++ [value]                                        # yellow
          check_consumption(values)
          {counter, values}                                               # yellow
      end

    loop(state)                                                           # yellow
  end

  def check_consumption(values) do                                        #green
    consumption = Enum.reduce(values, 0, fn i, acc -> i+acc end)          # yellow
    if consumption > 200 do                                               #green
      IO.puts "send notification"
    end
  end


end
