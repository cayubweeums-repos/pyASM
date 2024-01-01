import objects.targets


#---------- Object Test Suite ----------#

def test_target_creation():
    assert objects.targets.Target('server1', 'ip') == objects.targets.Target('server1', 'ip')
    assert objects.targets.Target('server1', '192.168.2.2') < objects.targets.Target('server2', '192.168.2.3')

def test_target_saving():
    objects.targets.save_object([objects.targets.Target('server1', '192.168.2.2'), objects.targets.Target('server2', '192.168.2.3')], 'data/objects/test_target_data.pkl')
    assert objects.targets.pickle_loader('data/objects/test_target_data.pkl')[0] == objects.targets.Target('server1', '192.168.2.2')