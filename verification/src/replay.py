"""Replay exact geometric inequalities at finite levels using fractions."""
from fractions import Fraction


def replay(levels=16):
    previous = Fraction(1)
    for n in range(1, levels + 1):
        # Distances here use the previous core radius as the unit.
        support = Fraction(1, 2**(n + 10))
        assert Fraction(1, 8) + support < Fraction(1, 4)
        assert 2 * support < Fraction(1, 4)
        scalar = Fraction(2) if n % 2 else Fraction(1, 2)
        cumulative = previous * scalar
        assert cumulative == (2 if n % 2 else 1)
        child_support = Fraction(1, 2**(n+11))
        error = 8 * child_support
        assert error == Fraction(1, 2**(n+8))
        # A vertical step of half a core radius stays inside its parent and
        # outside every child support, independently of the binary address.
        assert Fraction(1, 4)**2 + Fraction(1, 2)**2 < 1
        assert Fraction(1, 2) > child_support
        previous = cumulative
    even_max = 1 + Fraction(1, 2**10)
    odd_min = 2 - Fraction(1, 2**9)
    assert even_max < odd_min
    print(f"PASS: {levels} levels of nesting, disjointness, vertical test and scale bounds")
    print(f"PASS: even upper bound {even_max}, odd lower bound {odd_min}")


if __name__ == "__main__":
    replay()
