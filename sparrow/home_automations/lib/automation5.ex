defmodule Automation5 do
  use Sparrow.Actor

  pattern motion as {:motion, id, :on, location}                                # green
  pattern m_front_door as motion{location= :front_door}                         # green
  pattern m_entrance_hall as motion{location= :entrance_hall, id~> mid}         # green
  pattern c_front_door as {:contact, cid, :open, :front_door}                   # green

  pattern occupied_home as m_front_door and c_front_door and m_entrance_hall,   # green
                                            options: [ interval: {60, :secs},   # blue
                                                       seq: true,               # purple
                                                       last: true ]

  pattern empty_home as m_entrance_hall and c_front_door and m_front_door,      # green
                                      options: [ interval: {60, :secs},         # blue
                                                 seq: true,                     # purple
                                                 last: true ]

  reaction activate_home_scene(l, i, t), do: # code logic for arriving home
  reaction activate_leave_scene(l, i, t), do:  # code logic for leaving home

  react_to occupied_home, with: activate_home_scene
  react_to empty_home, with: activate_leave_scene

end
