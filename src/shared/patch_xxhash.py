import sys
import types
import hashlib


def apply_xxhash_patch():
    """Aplica un parche pure-python para xxhash si la DLL nativa está bloqueada por políticas de seguridad de Windows."""
    try:
        import xxhash  # noqa: F401
    except ImportError:
        mock_xxhash = types.ModuleType("xxhash")

        def _digest(data, length=16):
            b_data = data if isinstance(data, bytes) else str(data).encode("utf-8")
            return hashlib.md5(b_data).digest()[:length]

        def _hexdigest(data, seed=0):
            b_data = data if isinstance(data, bytes) else str(data).encode("utf-8")
            return hashlib.md5(b_data).hexdigest()

        mock_xxhash.xxh3_128_hexdigest = _hexdigest
        mock_xxhash.xxh3_64_hexdigest = _hexdigest
        mock_xxhash.xxh64_hexdigest = _hexdigest
        mock_xxhash.xxh32_hexdigest = _hexdigest
        mock_xxhash.xxh3_128digest = lambda d, s=0: _digest(d, 16)
        mock_xxhash.xxh3_64digest = lambda d, s=0: _digest(d, 8)
        mock_xxhash.xxh64_digest = lambda d, s=0: _digest(d, 8)
        mock_xxhash.xxh32_digest = lambda d, s=0: _digest(d, 4)

        class MockHasher:
            def __init__(self, data=b"", seed=0):
                self._data = bytearray(data if isinstance(data, bytes) else str(data).encode())

            def update(self, data):
                self._data.extend(data if isinstance(data, bytes) else str(data).encode())

            def intdigest(self):
                return int(hashlib.md5(self._data).hexdigest(), 16)

            def hexdigest(self):
                return hashlib.md5(self._data).hexdigest()

            def digest(self):
                return hashlib.md5(self._data).digest()

        mock_xxhash.xxh3_128 = MockHasher
        mock_xxhash.xxh3_64 = MockHasher
        mock_xxhash.xxh64 = MockHasher
        mock_xxhash.xxh32 = MockHasher

        sys.modules["xxhash"] = mock_xxhash


apply_xxhash_patch()
