defmodule Automation7 do
  use Sparrow.Actor

  pattern heating_failure as {:heating_f, id, :fhs_failure}[every: 3] and {:heating_f, id, :is_failure}, # green
                          options: [debounce: {60, :mins}]                                               # blue

end
