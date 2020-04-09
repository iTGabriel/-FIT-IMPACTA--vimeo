from vimeo.upload import UploadVideoMixin


def test_apply_chunk_size_rules():
    """
    Test ensures that the expected behavior for
    `UploadVideoMixin.apply_chunk_size_rules` follows the general rule, that
    any proposed `chunk_size` is fine as long as it does not result in more
    than 1024 `chunks`. This is important because as the number of `chunks`
    increases the likely hood of various TUS server errors increases as well.
    """

    # The following cases result in < 1024 and as such should be allowed
    assert UploadVideoMixin.apply_chunk_size_rules(1, 1024) == 1
    assert UploadVideoMixin.apply_chunk_size_rules(3, 1024) == 3

    # A `chunk_size` larger than `file_size` is ok
    assert UploadVideoMixin.apply_chunk_size_rules(3, 1) == 3
    assert UploadVideoMixin.apply_chunk_size_rules(1024, 1) == 1024

    # A `chunk_size` <= 0 is equivalent to 1 byte.
    assert UploadVideoMixin.apply_chunk_size_rules(0, 1024) == 1
    assert UploadVideoMixin.apply_chunk_size_rules(-1000, 1024) == 1

    # The following cases all result in > 1024 chunks.
    assert UploadVideoMixin.apply_chunk_size_rules(1, 1025) == 2

    # 20 MB chunks for a 100000 MB file (100GB)
    assert UploadVideoMixin.apply_chunk_size_rules(
        (20 * 1024 * 1024),
        (100000 * 1024 * 1024)
    ) == 102400001
