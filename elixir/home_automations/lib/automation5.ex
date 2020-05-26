defmodule Automation5 do
  require Timex

  def start do
    old_time = Timex.shift(Timex.now(), hours: -24)
    pid = spawn(Automation5, :loop, [{old_time, old_time, old_time}])
    IO.puts "Waiting for new messages ..."

    # Test messages
    Task.start_link(fn ->
      Process.sleep(5000)
      send(pid, {:motion, 1, :on, :front_door, Timex.now()})
      Process.sleep(5000)
      send(pid, {:contact, 1, :open, :front_door, Timex.now()})
      Process.sleep(5000)
      send(pid, {:motion, 2, :on, :entrance_hall, Timex.now()})
      Process.sleep(5000)
      send(pid, {:contact, 1, :open, :front_door, Timex.now()})
      Process.sleep(5000)
      send(pid, {:motion, 1, :on, :front_door, Timex.now()})
    end)
  end


  def loop({m_door, m_hall, c_door}) do                                               # yellow

    state =                                                                           # yellow
      receive do                                                                      # green
        {:motion, _id, :on, :front_door, m_door_dt} ->                                # green
          IO.puts("motion_front_door")
          if Timex.before?(Timex.shift(m_door_dt, seconds: -60), m_hall) do           # blue
            if Timex.after?(m_door_dt, c_door) and Timex.after?(c_door, m_hall) do    # purple
              IO.puts("code logic for leaving home")
            end                                                                       # purple
          end                                                                         # blue

          {m_door_dt, m_hall, c_door}                                                 # yellow

        {:motion, _id, :on, :entrance_hall, m_hall_dt} ->                             # green
          IO.puts("motion_entrance_hall")
          if Timex.before?(Timex.shift(m_hall_dt, seconds: -60), m_door) do           # blue
            if Timex.after?(m_hall_dt, c_door) and Timex.after?(c_door, m_door) do    # purple
              IO.puts("code logic for arriving home")
            end                                                                       # purple
          end                                                                         # blue

          {m_door, m_hall_dt, c_door}                                                 # yellow

        {:contact, _id, :open, :front_door, dt} ->                                    # green
          IO.puts("contact_front_door")
          {m_door, m_hall, dt}                                                        # yellow
      end                                                                             # green

    loop(state)                                                                         # yellow
  end
end
