# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
from _pytest.config import ExitCode


@pytest.fixture
def testdir(testdir):
    # testdir.makeconftest("""
    #     pytest_plugins = 'pytest_aspec.plugin'
    # """)
    return testdir

def test_should_print_a_short_passing_test(testdir):
    testdir.makepyfile("""
        def test_a_feature_is_working():
            assert True
    """)

    result = testdir.runpytest('--pspec')

    expected = 'test_should_print_a_short_passing_test.py \N{cherry blossom}'
    assert expected in result.stdout.str()


def test_should_print_a_verbose_passing_test(testdir):
    testdir.makepyfile("""
        def test_a_feature_is_working():
            assert True
    """)

    result = testdir.runpytest('--pspec', '-v')

    expected = 'test_a_feature_is_working'
    assert expected in result.stdout.str()
    expected = '\N{cherry blossom}'
    assert expected in result.stdout.str()

    # def test_should_not_modify_nodeid_when_disabled_test(testdir):
    #     testdir.makepyfile("""
    #         def test_a_feature_is_working():
    #             assert True
    #     """)
    #
    #     result = testdir.runpytest('-v')
    #
    #     expected = 'test_should_not_modify_nodeid_when_disabled_test.py::test_a_feature_is_working'
    #     assert expected in result.stdout.str()
    #
    # def test_should_print_a_red_failing_test(testdir):
    #     testdir.makepyfile("""
    #         def test_a_failed_test_of_a_feature():
    #             assert False
    #     """)
    #
    #     result = testdir.runpytest('--pspec')
    #     expected = ' \N{wilted flower} a failed test of a feature'
    #
    #     assert expected in result.stdout.str()
    #
    # def test_should_print_a_yellow_skipped_test(testdir):
    #     testdir.makepyfile("""
    #         import pytest
    #
    #         @pytest.mark.skip
    #         def test_a_skipped_test():
    #             pass
    #     """)
    #
    #     result = testdir.runpytest('--pspec')
    #     expected = ' \N{warning sign}\N{vs16} a skipped test'
    #
    #     assert expected in result.stdout.str()
    #
    # def test_should_output_plaintext_using_a_config_option(testdir):
    #     testdir.makeini("""
    #         [pytest]
    #         pspec_passed=[x]
    #     """)
    #     testdir.makepyfile("""
    #         def test_a_feature_is_working():
    #             assert True
    #     """)
    #     result = testdir.runpytest('--pspec')
    #
    #     expected = ' [x] a feature is working'
    #     assert expected in result.stdout.str()
    #

def test_custom_short_failed(testdir):
    """
    can we specify custom failed characters in our ini?
    """
    testdir.makeini("""
        [pytest]
        pspec_short_passed=\N{snowman}\N{vs16}
        pspec_short_failed=\N{snowflake}\N{vs16}
        pspec_short_skipped=\N{avocado}
    """)
    testdir.makepyfile("""
        import pytest

        def test_failed_char():
            "did we fail?"
            assert False
    """)
    result = testdir.runpytest('--pspec')

    expected = '\N{snowflake}\N{vs16}'
    assert expected in result.stdout.str()

def test_custom_failed(testdir):
    """
    can we specify custom failed characters in our ini?
    """
    testdir.makeini("""
        [pytest]
        pspec_passed=\N{snowman}\N{vs16}
        pspec_failed=\N{snowflake}\N{vs16}
        pspec_skipped=\N{avocado}
    """)
    testdir.makepyfile("""
        import pytest

        def test_failed_char():
            "did we fail?"
            assert False
    """)
    result = testdir.runpytest('--pspec', '-v')

    expected = '\N{snowflake}\N{vs16}'
    assert expected in result.stdout.str()


def test_custom_short_skipped(testdir):
    """
    can we specify custom failed characters in our ini?
    """
    testdir.makeini("""
        [pytest]
        pspec_passed=\N{snowman}\N{vs16}
        pspec_failed=\N{snowflake}\N{vs16}
        pspec_skipped=\N{avocado}
        pspec_short_passed=\N{snowman}\N{vs16}
        pspec_short_failed=\N{snowflake}\N{vs16}
        pspec_short_skipped=\N{avocado}
    """)
    testdir.makepyfile("""
        import pytest

        @pytest.mark.skip
        def test_failed_char():
            "did we skip?"
            assert False
    """)
    result = testdir.runpytest('--pspec')

    expected = '\N{avocado}'
    assert expected in result.stdout.str()


def test_custom_skipped(testdir):
    """
    can we specify custom failed characters in our ini?
    """
    testdir.makeini("""
        [pytest]
        pspec_passed=\N{snowman}\N{vs16}
        pspec_failed=\N{snowflake}\N{vs16}
        pspec_skipped=\N{avocado}
        pspec_short_passed=\N{snowman}\N{vs16}
        pspec_short_failed=\N{snowflake}\N{vs16}
        pspec_short_skipped=\N{avocado}
    """)
    testdir.makepyfile("""
        import pytest

        @pytest.mark.skip
        def test_failed_char():
            "did we skip?"
            assert False
    """)
    result = testdir.runpytest('--pspec', '-v')

    expected = 'did we skip?'
    assert expected in result.stdout.str()
    expected = '\N{avocado}'
    assert expected in result.stdout.str()

    # def test_should_print_the_test_class_name(testdir):
    #     testdir.makepyfile("""
    #         class TestFoo(object):
    #             def test_foo(self):
    #                 pass
    #
    #         class TestBar(object):
    #             def test_bar(self):
    #                 pass
    #     """)
    #     result = testdir.runpytest('--pspec')
    #
    #     lines = result.stdout.get_lines_after('Foo')
    #     assert '\N{cherry blossom} foo' in lines[0]
    #
    #     lines = result.stdout.get_lines_after('Bar')
    #     assert '\N{cherry blossom} bar' in lines[0]
    #
    # def test_should_print_the_module_name_of_a_test_without_class(
    #     self,
    #     testdir
    # ):
    #     testdir.makefile('.py', test_module_name="""
    #         def test_a_failed_test_of_a_feature():
    #             assert False
    #     """)
    #
    #     result = testdir.runpytest('--pspec')
    #     result.stdout.fnmatch_lines(['module name'])
    #


def test_nopspec(testdir):
    testdir.makefile('.py', test_module_name="""
        def test_a_passing_test():
            assert True
    """)

    result = testdir.runpytest()
    assert '1 passed' in result.stdout.str()
    assert 'test_module_name.py .' in result.stdout.str()


def test_two_tests(testdir):
    testdir.makefile('.py', test_two_tests="""
        def test_01():
            assert True
            
        def test_02():
            assert True
    """)

    result = testdir.runpytest()
    assert '2 passed' in result.stdout.str()
    assert 'test_two_tests.py ..' in result.stdout.str()

    result = testdir.runpytest('--pspec', '-v')
    assert '2 passed' in result.stdout.str()
    assert 'test_two_tests.py\n  test_01' in result.stdout.str()
    assert '\n  test_02' in result.stdout.str()

    # def test_should_use_python_patterns_configuration(testdir):
    #     testdir.makeini("""
    #         [pytest]
    #         python_classes=Describe*
    #         python_files=*spec.py
    #         python_functions=it*
    #     """)
    #     testdir.makefile('.py', module_spec="""
    #         class DescribeTest(object):
    #             def it_runs(self):
    #                 pass
    #     """)
    #
    #     result = testdir.runpytest('--pspec')
    #
    #     lines = result.stdout.get_lines_after('Test')
    #     assert '\N{cherry blossom} runs' in lines[0]
    #
def test_should_print_doc_string_if_present(testdir):
    testdir.makepyfile("""
        def test_a_feature_is_working():
            "test must return as header"
            assert True
    """)

    result = testdir.runpytest('--pspec', '-v')

    expected = 'test must return as header'
    assert expected in result.stdout.str()
    expected = '\N{cherry blossom}'
    assert expected in result.stdout.str()

