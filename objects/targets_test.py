from targets import Target

def test_target_creation():
    assert Target('server1', 'ip') == Target('server1', 'ip')
    assert Target('server1', '192.168.2.2') > Target('server2', '192.168.2.3')