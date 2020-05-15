defmodule Automation5 do
  require Timex

  def start do
    old_time = Timex.shift(Timex.now(), hours: -24)
    pid = spawn(Automation5, :loop, [{old_time, old_time, old_time}])

    #Test messages
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

  def loop({m_door, m_hall, c_door}) do
    # IO.puts "Waiting for new messages ..."
    state =
      receive do
        {:motion, _id, :on, :front_door, m_door_dt} ->
          IO.puts "motion_front_door"
          if Timex.before?(Timex.shift(m_door_dt, seconds: -60), m_hall)  do
            if Timex.after?(m_door_dt, c_door) and Timex.after?(c_door, m_hall) do
              IO.puts "code logic for leaving home"
            end
          end
          {m_door_dt, m_hall, c_door}

        {:motion, _id, :on, :entrance_hall, m_hall_dt} ->
          IO.puts "motion_entrance_hall"
          if Timex.before?(Timex.shift(m_hall_dt, seconds: -60), m_door)  do
            if Timex.after?(m_hall_dt, c_door) and Timex.after?(c_door, m_door) do
              IO.puts "code logic for arriving home"
            end
          end

          {m_door, m_hall_dt, c_door}

        {:contact, _id, :open, :front_door, dt} ->
          IO.puts "contact_front_door"
          {m_door, m_hall, dt}
      end

    loop(state)
  end
end

