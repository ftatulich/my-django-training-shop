from .wishlist import Wishlist


def context(request) -> dict[str: Wishlist]:
    """Препроцесор для списку уподобань"""
    wishlist = Wishlist(request)
    return {'wishlist': wishlist}
