import targets
from targets import Target

def test_target_creation():
    assert Target('server1', 'ip') == Target('server1', 'ip')
    assert Target('server1', '192.168.2.2') < Target('server2', '192.168.2.3')

def test_target_saving():
    targets.save_object([Target('server1', '192.168.2.2'), Target('server2', '192.168.2.3')], 'data/objects/test_target_data.pkl')
    assert targets.pickle_loader('data/objects/test_target_data.pkl')[0] == Target('server1', '192.168.2.2')