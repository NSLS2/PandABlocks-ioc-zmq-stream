from pandablocks_ioc_zmq_stream import ZMQBuffer


def test_one():
    zb = ZMQBuffer()
    assert zb is not None
