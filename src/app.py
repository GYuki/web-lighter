from src.container import Container
from src.mediator_setup import set_up


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    set_up()
