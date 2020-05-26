automations = ['automation1', 'automation2', 'automation3', 'automation4', 'automation5', 'automation6',  'automation7']

stats = %{:yellow => 0, :purple => 0, :blue => 0, :green => 0}

update_acc = fn (line, acc) ->
  Enum.map(acc, fn {k, v} ->
    case String.contains?(line, Atom.to_string(k)) do
      true -> {k, v+1}
      false -> {k, v}
    end
  end)
end

Enum.each(automations, fn automation ->
  output =
    File.read("lib/#{automation}.ex")
    |> elem(1)
    |> String.split("\n", trim: true)
    |> Enum.reduce(stats, fn line, acc -> update_acc.(line, acc) end)
    |> Map.new

  IO.puts "[#{automation}] #{output.yellow}, #{output.purple}, #{output.blue}, #{output.green}"
end)


