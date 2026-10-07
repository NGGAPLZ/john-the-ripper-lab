"""Verify public, synthetic lab fixtures without running a cracking tool."""
import hashlib
from pathlib import Path

def main():
    root = Path(__file__).resolve().parent / 'samples'
    words = (root / 'demo-words.txt').read_text(encoding='utf-8').splitlines()
    for algorithm, expected_word, filename in [
        ('md5', 'cookies', 'md5.txt'),
        ('sha256', '111111111111', 'sha256.txt'),
    ]:
        expected_hash = (root / filename).read_text(encoding='utf-8').strip()
        assert hashlib.new(algorithm, expected_word.encode()).hexdigest() == expected_hash
        matches = [word for word in words if hashlib.new(algorithm, word.encode()).hexdigest() == expected_hash]
        assert matches == [expected_word], (algorithm, matches)
        print(f'{algorithm}: fixture and expected candidate verified')

if __name__ == '__main__':
    main()
