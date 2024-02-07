import u2py

cmd = u2py.Command("WHO")
cmd_output = cmd.run(capture=False)

print(cmd_output)
