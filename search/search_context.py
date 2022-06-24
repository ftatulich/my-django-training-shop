from .forms import SearchForm


def context(request) -> dict[str: SearchForm]:
    form = SearchForm()
    return {'search_form': form}

