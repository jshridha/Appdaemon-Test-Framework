from pytest import fixture

from appdaemontestframework import patch_hass, AssertThatWrapper, GivenThatWrapper, TimeTravelWrapper

pytest_plugins = 'pytester'


@fixture
def hass_functions():
    patched_hass_functions, unpatch_callback = patch_hass()
    yield patched_hass_functions
    unpatch_callback()


@fixture
def given_that(hass_functions):
    return GivenThatWrapper(hass_functions)


@fixture
def assert_that(hass_functions):
    return AssertThatWrapper(hass_functions)


@fixture
def time_travel(hass_functions):
    return TimeTravelWrapper(hass_functions)


@fixture
def configure_appdaemontestframework_for_pytester(testdir):
    testdir.makeconftest(
        """
        from pytest import fixture
        from appdaemontestframework import patch_hass, AssertThatWrapper, GivenThatWrapper, TimeTravelWrapper
        
        
        @fixture
        def hass_functions():
            patched_hass_functions, unpatch_callback = patch_hass()
            yield patched_hass_functions
            unpatch_callback()
        
        
        @fixture
        def given_that(hass_functions):
            return GivenThatWrapper(hass_functions)
        
        
        @fixture
        def assert_that(hass_functions):
            return AssertThatWrapper(hass_functions)
        
        
        @fixture
        def time_travel(hass_functions):
            return TimeTravelWrapper(hass_functions)
    """)
