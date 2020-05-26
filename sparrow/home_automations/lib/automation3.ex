defmodule Automation3 do
  use Sparrow.Actor

  pattern send_alert as not {:contact, :open, room} [window: {60, :secs}], options: [last]# green blue

end
