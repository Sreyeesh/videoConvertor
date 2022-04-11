rom dependency_injector.wiring import Provide, inject

from src.Container.Container import Container
from src.Services.SettingsService.SettingsService import SettingsService


@inject
def test(settings: SettingsService = Provide[Container.settings_service]):
    print(settings.get())


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    test()