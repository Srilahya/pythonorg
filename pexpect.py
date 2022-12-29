import pexpect
#print(pexpect.run('echo hello'))
child=pexpect.spawn("echo myworld")
print(child.expect(["Hello","myworld","lahya"]))