defmodule Automation3 do

  def start do
    pid = spawn(Automation3, :loop, [{nil, :open}])
    IO.puts("Waiting for new messages ...")
    # Test messages
    Task.start_link(fn ->
      send(pid, {:contact, 1, :open, :bathroom})
      Process.sleep(7000)
      send(pid, {:contact, 1, :open, :bathroom})
      Process.sleep(3000)
      send(pid, {:contact, 1, :closed, :bathroom})
    end)
  end

  def loop({timer_ref, window_status}) do                             # yellow

    state =                                                           # yellow
      receive do                                                      # green
        {:contact, _id, :open, :bathroom} ->                          # green
          IO.puts("window_bathroom_open")
          timer_ref = Process.send_after(self(), :time_alert, 5000)   # blue
          {timer_ref, :open}                                          # yellow

        {:contact, _id, :closed, :bathroom} ->                         # green
          IO.puts("window_bathroom_closed")
          Process.cancel_timer(timer_ref)                             # blue
          {nil, :close}                                               # yellow

        :time_alert ->                                                # green
          IO.puts("time_alert_window_opened_bathroom")
          {nil, window_status}                                        # yellow
      end                                                             

    loop(state)                                                       # yellow
  end

end
